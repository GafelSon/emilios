import re
import logging
from urllib3 import PoolManager, encode_multipart_formdata
from concurrent.futures import ThreadPoolExecutor, as_completed
from config import settings

class SMSService:
    def __init__(self):
        self._setup_logging()
        self._http_client = PoolManager()
        self._targets = settings.SMS_TARGETS

    def _setup_logging(self):
        logging.basicConfig(
            level=getattr(logging, settings.LOG_LEVEL.upper()),
            format='%(asctime)s - %(levelname)s : %(message)s'
        )
        self.logger = logging.getLogger(__name__)

    def _validation(self, phone: str) -> bool:
        return bool(re.match(r'^9\d{9}$', phone))

    def _send(self, phone: str, url: str, offline: bool = False) -> dict:
        if offline:
            self.logger.info(f"OFFLINE: Send SMS -> +98{phone} via {url}")
            return {"url": url, "status": "offline", "success": True}
        try:
            meo = encode_multipart_formdata({"phone": f"0{phone}"})
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