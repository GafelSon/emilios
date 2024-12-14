from typing_extensions import Any
from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Dict, Union

class Settings(BaseSettings):
    LOG_LEVEL: str = 'INFO'
    PROXY: list[str] = []
    SMS_BODY_TEMPLATES: Dict[str, Union[Dict[Any, Any], str]] = {
        'default': {'phone': '0{phone}'},

        'https://api.snapp.market/mart/v1/user/loginMobileWithNoPass': {
            'cellphone': '0{phone}',
        },
        'https://api.digikala.com/v1/user/authenticate/': {
            'force_send_otp': 'true',
            'otp_call': 'true',
            'username': '0{phone}'
        },
        'https://3tex.io/api/1/users/validation/mobile': {
            'receptorPhone': '0{phone}',
        },
        'https://deniizshop.com/api/v1/sessions/login_request': {
            'mobile_phone': '0{phone}',
        },
        'https://flightio.com/bff/Authentication/CheckUserKey': {
            'userKey': '0{phone}',
        },
        'https://app.snapp.taxi/api/api-passenger-oauth/v2/otp': {
            'cellphone': '0{phone}',
        },
        'https://bck.behtarino.com/api/v1/users/phone_verification/': {
            'phone': '0{phone}',
        },
        'https://abantether.com/users/register/phone/send/': {
            'phoneNumber': '0{phone}',
        },
        'https://novinbook.com/index.php?route=account/phone': {
            'phone': '0{phone}'
        },
        'https://www.azki.com/api/vehicleorder/api/customer/register/login-with-vocal-verification-code': {
            'phoneNumber': '0{phone}',
            'esfelurm': 'esfelurm'
        },
        'https://api.pooleno.ir/v1/auth/check-mobile': {
            'mobile': '0{phone}',
        },
        'https://agent.wide-app.ir/auth/token': {
            'grant_type': 'otp',
            'client_id': '62b30c4af53e3b0cf100a4a0',
            'phone': '0{phone}',
        },
        'https://tap33.me/api/v2/user': {
            'credential': {
                'phoneNumber': '{phone}',
                'role': 'PASSENGER'
            }
        },
        'https://web.emtiyaz.app/json/login': {
            'send': 1,
            'cellphone': '0{phone}'
        },
        'https://api.divar.ir/v5/auth/authenticate': {
            'phone': '0{phone}',
        },
        'https://messengerg2c4.iranlms.ir/': {
            'api_version': '3',
            'method': 'sendCode',
            'data':
                {
                    'phone_number': '0{phone}',
                    'send_type': 'SMS'
                }
        },
        'https://nx.classino.com/otp/v1/api/login': {
            'mobile': '0{phone}',
        },
        'https://bama.ir/signin-checkforcellnumber': {
            'cellNumber': '0{phone}',
        },
        'https://snappfood.ir/mobile/v2/user/loginMobileWithNoPass?lat=35.774&long=51.418&optionalClient=WEBSITE&client=WEBSITE&deviceType=WEBSITE&appVersion=8.1.0&UDID=39c62f64-3d2d-4954-9033-816098559ae4&locale=fa': {
            'cellphone': '0{phone}',
        },
        'https://ws.alibaba.ir/api/v3/account/mobile/otp': {
            'phoneNumber': '0{phone}',
        },
        'https://api.snapp.market/mart/v1/user/loginMobileWithNoPass?cellphone=0': {
            '': '{phone}',
        },
        'https://api.bitbarg.com/api/v1/authentication/registerOrLogin': {
            'phone': '0{phone}',
        },
        'https://api.bahramshop.ir/api/user/validate/username': {
            'username': '0{phone}',
        },
        'https://mobapi.banimode.com/api/v2/auth/request': {
            'phone': '0{phone}',
        },
        'https://takshopaccessorise.ir/api/v1/sessions/login_request': {
            'mobile_phone': '0{phone}',
        },
        'https://api.bitpin.ir/v1/usr/sub_phone/': {
            'phone': '0{phone}',
        },
        'https://chamedoon.com/api/v1/membership/guest/request_mobile_verification': {
            'mobile': '0{phone}',
        },
        'https://server.kilid.com/global_auth_api/v1.0/authenticate/login/realm/otp/start?realm=PORTAL': {
            'mobile': '0{phone}',
        },
        'https://pinket.com/api/cu/v2/phone-verification': {
            'phoneNumber': '0{phone}',
        },
        'https://core.otaghak.com/odata/Otaghak/Users/SendVerificationCode': {
            'userName': '0{phone}',
        },
        'https://www.shab.ir/api/fa/sandbox/v_1_4/auth/enter-mobile': {
            'mobile': '0{phone}',
        },
        'https://bit24.cash/app/api/auth/check-mobile': {
            'mobile': '0{phone}',
        },
        'https://app.itoll.ir/api/v1/auth/login': {
            'mobile': '0{phone}',
        },
        'https://api.raybit.net:3111/api/v1/authentication/register/mobile': {
            'mobile': '0{phone}',
        },
        'https://www.pubisha.com/login/checkCustomerActivation': {
            'mobile': '0{phone}',
        },
        'https://farvi.shop/api/v1/sessions/login_request': {
            'mobile_phone': '0{phone}',
        },
        'https://gw.taaghche.com/v4/site/auth/signup': {
            'contact': '0{phone}',
        },
        'https://www.namava.ir/api/v1.0/accounts/registrations/by-phone/request': {
            'UserName': '0{phone}',
        },
        'https://www.sheypoor.com/auth': {
            'username': '0{phone}',
        },
        'https://api.snapp.ir/api/v1/sms/link': {
            'phone': '0{phone}',
        },
        'https://a4baz.com/api/web/login': {
            'cellphone': '0{phone}',
        },
        'https://api.anargift.com/api/people/auth': {
            'user': '0{phone}',
        },
        'https://nobat.ir/api/public/patient/login/phone': {
            'mobile': '0{phone}',
        },
        'https://www.buskool.com/send_verification_code': {
            'phone': '0{phone}',
        },
        'https://application2.billingsystem.ayantech.ir/WebServices/Core.svc/requestActivationCode': {
            'Parameters':
                {'ApplicationType': 'Web',
                    'ApplicationUniqueToken': None,
                    'ApplicationVersion': '1.0.0',
                    'MobileNumber': '+98{phone}',
                }
        },
        'https://www.simkhanapi.ir/api/users/registerV2': {
            'mobileNumber': '0{phone}',
        },
        'https://sandbox.sibirani.ir/api/v1/user/invite': {
            'username': '0{phone}',
        },
        'https://shop.hyperjan.ir/api/users/manage': {
            'mobile': '0{phone}',
        },
        'https://api.digikala.com/v1/user/authenticate/': {
            'username': '0{phone}',
        },
        'https://hiword.ir/wp-json/otp-login/v1/login': {
            'identifier': '0{phone}',
        },
        'https://abantether.com/users/register/phone/send/': {
            'phoneNumber': '0{phone}',
        },
        'https://api.bit24.cash/api/v3/auth/check-mobile': {
            'mobile': '0{phone}',
        },
        'https://dicardo.com/main/sendsms': {
            'phone': '0{phone}',
        },
        'https://ghasedak24.com/user/ajax_register': {
            'username': '0{phone}',
        },
        'https://tikban.com/Account/LoginAndRegister': {
            'CellPhone': '0{phone}',
        },
        'https://www.digistyle.com/users/login-register/': {
            'loginRegister[email_phone]': '0{phone}',
        },
        'https://banankala.com/home/login': {
            'Mobile': '0{phone}',
        },
        'https://www.iranketab.ir/account/register': {
            'UserName': '0{phone}',
        },
        'https://ketabchi.com/api/v1/auth/requestVerificationCode': {
            'phoneNumber': '0{phone}',
        },
        'https://www.offdecor.com/index.php?route=account/login/sendCode': {
            'phone': '0{phone}',
        },
        'https://exo.ir/index.php?route=account/mobile_login': {
            'mobile_number': '0{phone}',
        },
        'https://shahrfarsh.com/Account/Login': {
            'phoneNumber': '0{phone}',
        },
        'https://takfarsh.com/wp-content/themes/bakala/template-parts/send.php': {
            'phone_email': '0{phone}',
        },
        'https://www.khanoumi.com/accounts/sendotp': {
            'mobile': '0{phone}',
        },
        'https://rojashop.com/api/auth/sendOtp': {
            'mobile': '0{phone}',
        },
        'https://dadpardaz.com/advice/getLoginConfirmationCode': {
            'mobile': '0{phone}',
        },
        'https://api.rokla.ir/api/request/otp': {
            'mobile': '0{phone}',
        },
        'https://khodro45.com/api/v1/customers/otp/': {
            'mobile': '0{phone}',
        },
        'https://mashinbank.com/api2/users/check': {
            'mobileNumber': '0{phone}',
        },
        'https://api.pezeshket.com/core/v1/auth/requestCode': {
            'mobileNumber': '0{phone}',
        },
        'https://virgool.io/api/v1.4/auth/verify': {
            'method': 'phone',
            'identifier': '0{phone}',
        },
        'https://api.timcheh.com/auth/otp/send': {
            'mobile': '0{phone}',
        },
        'https://client.api.paklean.com/user/resendCode': {
            'username': '0{phone}',
        },
        'https://mobogift.com/signin': {
            'username': '0{phone}',
        },
        'https://api.iranicard.ir/api/v1/register': {
            'mobile': '0{phone}',
        },
        'https://tj8.ir/auth/register': {
            'mobile': '0{phone}',
        },
        'https://mashinbank.com/api2/users/check': {
            'mobileNumber': '0{phone}',
        },
        'https://cinematicket.org/api/v1/users/signup': {
            'phone_number': '0{phone}',
        },
        'https://www.irantic.com/api/login/request': {
            'mobile': '0{phone}',
        },
        'https://kafegheymat.com/shop/getLoginSms': {
            'phone': '0{phone}',
        },
        'https://api.snapp.express/mobile/v4/user/loginMobileWithNoPass?client=PWA&optionalClient=PWA&deviceType=PWA&appVersion=5.6.6&optionalVersion=5.6.6&UDID=bb65d956-f88b-4fec-9911-5f94391edf85': {
            'cellphone': '0{phone}',
        },
        'https://www.delino.com/user/register': {
            'mobile': '0{phone}',
        },
        'https://alopeyk.com/api/sms/send.php': {
            'phone': '0{phone}',
        },
        'https://1401api.tamland.ir/api/user/signup': {
            'Mobile': '0{phone}',
        },
        'https://shop.opco.co.ir/index.php?route=extension/module/login_verify/update_register_code': {
            'telephone': '0{phone}',
        },
        'https://api.digikalajet.ir/user/login-register/': {
            'phone': '0{phone}',
        },
        'https://melix.shop/site/api/v1/user/otp': {
            'mobile': '0{phone}',
        },
        'https://safiran.shop/login': {
            'mobile': '0{phone}',
        },
        'https://restaurant.delino.com/user/register': {
            'apiToken':'VyG4uxayCdv5hNFKmaTeMJzw3F95sS9DVMXzMgvzgXrdyxHJGFcranHS2mECTWgq',
            'clientSecret':'7eVdaVsYXUZ2qwA9yAu7QBSH2dFSCMwq',
            'device':'web',
            'username': '0{phone}',
        },
        'https://garcon.tandori.ir/users/v1/main/login': {
            'phone': '0{phone}',
        },
        'https://dastkhat-isad.ir/api/v1/user/store': {
            'mobile': '0{phone}',
        },
        'https://irwco.ir/register': {
            'mobile': '0{phone}',
        },
        'https://api.sibbank.ir/v1/auth/login': {
            'phone_number': '0{phone}',
        },
        'https://api.snapp.ir/api/v1/sms/link': {
            'phone': '0{phone}',
        },
        'https://www.miare.ir/api/otp/driver/request/': {
            'phone_number': '0{phone}',
        },
        'https://api.arshiyan.com/send_code': {
            'country_code':'98',
            'phone_number': '0{phone}',
        },
        'https://backend.topnoor.ir/web/v1/user/otp': {
            'mobile': '0{phone}',
        },
        'https://api.alinance.com/user/register/mobile/send/': {
            'phone_number': '0{phone}',
        },
        'https://api.alopeyk.com/safir-service/api/v1/login': {
            'phone': '0{phone}',
        },
        'https://api.dadhesab.ir/user/entry': {
            'username': '0{phone}',
        },
        'https://app.dosma.ir/sendverify/': {
            'username': '0{phone}',
        },
        'https://api.ehteraman.com/api/request/otp': {
            'mobile': '0{phone}',
        },
        'https://api-ebcom.mci.ir/services/auth/v1.0/otp': {
            'msisdn': '0{phone}',
        },
        'https://api.hbbs.ir/authentication/SendCode': {
            'MobileNumber': '0{phone}',
        },
        'https://api.iranamlaak.net/authenticate/send/otp/to/mobile/via/sms': {
            'AgencyMobile': '0{phone}',
        },
        'https://api.kcd.app/api/v1/auth/login': {
            'mobile': '0{phone}',
        },
        'https://mazoocandle.ir/login': {
            'phone': '0{phone}',
        },
        'https://api.ostadkr.com/login': {
            'mobile': '0{phone}',
        },
        'https://api.paymishe.com/api/v1/otp/registerOrLogin': {
            'mobile': '0{phone}',
        },
        'https://api.rayshomar.ir/api/Register/RegistrMobile': {
            'MobileNumber': '0{phone}',
        },
        'https://refahtea.ir/wp-admin/admin-ajax.php': {
            'mobile': '0{phone}',
        },
        'https://digitalsignup.snapp.ir/oauth/drivers/api/v1/otp': {
            'cellphone': '0{phone}',
        },
        'https://mamifood.org/Registration.aspx/SendValidationCode': {
            'Phone': '0{phone}',
        },
        'https://server.uphone.ir/api/v1/login/otp/request': {
            'mobile': '0{phone}',
        },
        'https://abantether.com/users/register/phone/send/': {
            'phoneNumber': '0{phone}',
        },
        'https://www.glite.ir/wp-admin/admin-ajax.php': {
            'action': 'logini_first',
            'login':'0{phone}',
        },
        'https://novinbook.com/index.php?route=account/phone': {
            'phone': '0{phone}',
        },
        'https://api.offch.com/auth/otp': {
            'username': '0{phone}',
        },
        'https://sandbox.sibbazar.com/api/v1/user/invite': {
            'username': '0{phone}',
        },
        'https://sabziman.com/wp-admin/admin-ajax.php': {
            'action': 'newphoneexist',
            'phonenumber' : '0{phone}'
        },
        'https://api.watchonline.shop/api/v1/otp/request': {
            'mobile': '0{phone}',
        },
        'https://abantether.com/users/register/phone/send/': {
            'phoneNumber': '0{phone}',
            'email': ''
        },
        'https://flightio.com/bff/Authentication/CheckUserKey': {
            'userKey':'98-{phone}',
            'userKeyType': 1
        },
        'https://shadmessenger12.iranlms.ir/': {
            'api_version': '3',
            'method': 'sendCode',
            'data':
                {
                    'phone_number': '0{phone}',
                    'send_type': 'SMS'
                }
        },
        'https://agent.wide-app.ir/auth/token': {
            'grant_type':'otp',
            'client_id':'62b30c4af53e3b0cf100a4a0',
            'phone': '0{phone}'
        },
        'https://tap33.me/api/v2/user': {
            'credential':
                {
                    'phoneNumber': '0{phone}',
                    'role': 'PASSENGER'
                }
        },
        'https://apollo.digify.shop/graphql': {
            'operationName':'Mutation',
            'variables': {
                'content': {
                    'phone_number':'0{phone}',
                    'query':'mutation Mutation($content: MerchantRegisterOTPSendContent) {\n  merchantRegister {\n    otpSend(content: $content)\n    __typename\n  }\n}'
                }
            }
        },
        'https://api.snapp.market/mart/v1/user/loginMobileWithNoPass': {
            'cellphone': '0{phone}',
        },
        'https://auth.mrbilit.com/api/login/exists/v2': {
            'mobileOrEmail': '0{phone}',
            'source': 2,
            'sendTokenIfNot': 'true',
            'esfelurm': 'esfelurm'
        },
        'https://api.chartex.net/api/v2/user/validate': {
            'mobile': '0{phone}',
            'country_code': 'IR',
            'provider_code': 'RUBIKA'
        },
        'https://www.snapptrip.com/register': {
            'lang': 'fa',
            'country_id': '860',
            'password': 'snaptrippass',
            'mobile_phone': '0{phone}',
            'country_code': '+98',
            'email': 'example@gmail.com'
        },
        'https://api-v2.filmnet.ir/access-token/users/%v/phone}/otp': {
            'phone': '0{phone}',
        },
        'https://api.bitpin.ir/v1/usr/sub_phone/': {
            'phone': '0{phone}',
            'captcha_token': ''
        },
        'https://chamedoon.com/api/v1/membership/guest/request_mobile_verification': {
            'mobile': '0{phone}',
            'origin': '/',
            'referrer_id': ''
        },
        'https://www.shab.ir/api/fa/sandbox/v_1_4/auth/enter-mobile': {
            'mobile': '0{phone}',
            'country_code': '+98'
        },
        'https://api.raybit.net:3111/api/v1/authentication/register/mobile': {
            'mobile': '0{phone}',
            'side':'web'
        },
        'https://api.torob.com/a/phone/send-pin/': {
            'phone_number': '0{phone}',
            'esfelurm': 'esfelurm',
        },
        'https://www.namava.ir/api/v1.0/accounts/registrations/by-phone/request': {
            'UserName': '0{phone}',
        },
        'https://gw.taaghche.com/v4/site/auth/signup': {
            'contact': '0{phone}',
        },
        'https://core.gap.im/v1/user/add.json?mobile=%2B%s': {
            "esfelurm": "esfelurm",
        },
        'https://app.mydigipay.com/digipay/api/users/send-sms': {
            'cellNumber': '0{phone}',
            'device': {
                'deviceId': 'a16e6255-17c3-431b-b047-3f66d24c286f',
                'deviceModel': 'WEB_BROWSER', 'deviceAPI': 'WEB_BROWSER',
                'osName': 'WEB'
            }
        },
    }

    SMS_TARGETS: list[str] = [
        'https://api.digikala.com/v1/user/authenticate/'
        "https://3tex.io/api/1/users/validation/mobile",
        "https://deniishop.com/api/v1/sessions/login_request",
        "https://flightio.com/bff/Authentication/CheckUserKey",
        "https://app.snapp.taxi/api/api-passenger-oauth/v2/otp",
        "https://bck.behtarino.com/api/v1/users/phone_verification/",
        "https://abantether.com/users/register/phone/send/",
        "https://novinbook.com/index.php?route=account/phone",
        "https://www.azki.com/api/vehicleorder/api/customer/register/login-with-vocal-verification-code?phoneNumber=%s",
        "https://api.pooleno.ir/v1/auth/check-mobile",
        "https://agent.wide-app.ir/auth/token",
        "https://tap33.me/api/v2/user",
        "https://web.emtiyaz.app/json/login",
        "https://api.divar.ir/v5/auth/authenticate",
        "https://messengerg2c4.iranlms.ir/",
        "https://nx.classino.com/otp/v1/api/login",
        "https://bama.ir/signin-checkforcellnumber",
        "https://snappfood.ir/mobile/v2/user/loginMobileWithNoPass?lat=35.774&long=51.418&optionalClient=WEBSITE&client=WEBSITE&deviceType=WEBSITE&appVersion=8.1.0&UDID=39c62f64-3d2d-4954-9033-816098559ae4&locale=fa",
        "https://ws.alibaba.ir/api/v3/account/mobile/otp",
        "https://api.bitbarg.com/api/v1/authentication/registerOrLogin",
        "https://api.bahramshop.ir/api/user/validate/username",
        "https://mobapi.banimode.com/api/v2/auth/request",
        "https://takshopaccessorise.ir/api/v1/sessions/login_request",
        "https://api.bitpin.ir/v1/usr/sub_phone/",
        "https://chamedoon.com/api/v1/membership/guest/request_mobile_verification",
        "https://server.kilid.com/global_auth_api/v1.0/authenticate/login/realm/otp/start?realm=PORTAL",
        "https://pinket.com/api/cu/v2/phone-verification",
        "https://core.otaghak.com/odata/Otaghak/Users/SendVerificationCode",
        "https://www.shab.ir/api/fa/sandbox/v_1_4/auth/enter-mobile",
        "https://bit24.cash/app/api/auth/check-mobile",
        "https://app.itoll.ir/api/v1/auth/login",
        "https://api.raybit.net:3111/api/v1/authentication/register/mobile",
        "https://www.pubisha.com/login/checkCustomerActivation",
        "https://farvi.shop/api/v1/sessions/login_request",
        "https://gw.taaghche.com/v4/site/auth/signup",
        "https://www.namava.ir/api/v1.0/accounts/registrations/by-phone/request",
        "https://www.sheypoor.com/auth",
        "https://api.snapp.ir/api/v1/sms/link",
        "https://a4baz.com/api/web/login",
        "https://api.anargift.com/api/people/auth",
        "https://nobat.ir/api/public/patient/login/phone",
        "https://www.buskool.com/send_verification_code",
        "https://application2.billingsystem.ayantech.ir/WebServices/Core.svc/requestActivationCode",
        "https://www.simkhanapi.ir/api/users/registerV2",
        "https://sandbox.sibirani.ir/api/v1/user/invite",
        "https://shop.hyperjan.ir/api/users/manage",
        "https://api.digikala.com/v1/user/authenticate/",
        "https://hiword.ir/wp-json/otp-login/v1/login",
        "https://abantether.com/users/register/phone/send/",
        "https://api.bit24.cash/api/v3/auth/check-mobile",
        "https://dicardo.com/main/sendsms",
        "https://ghasedak24.com/user/ajax_register",
        "https://tikban.com/Account/LoginAndRegister",
        "https://www.digistyle.com/users/login-register/",
        "https://banankala.com/home/login",
        "https://www.iranketab.ir/account/register",
        "https://ketabchi.com/api/v1/auth/requestVerificationCode",
        "https://www.offdecor.com/index.php?route=account/login/sendCode",
        "https://exo.ir/index.php?route=account/mobile_login",
        "https://shahrfarsh.com/Account/Login",
        "https://takfarsh.com/wp-content/themes/bakala/template-parts/send.php",
        "https://shop.beheshticarpet.com/my-account/",
        "https://www.khanoumi.com/accounts/sendotp",
        "https://rojashop.com/api/auth/sendOtp",
        "https://dadpardaz.com/advice/getLoginConfirmationCode",
        "https://api.rokla.ir/api/request/otp",
        "https://khodro45.com/api/v1/customers/otp/",
        "https://mashinbank.com/api2/users/check",
        "https://api.pezeshket.com/core/v1/auth/requestCode",
        "https://virgool.io/api/v1.4/auth/verify",
        "https://api.timcheh.com/auth/otp/send",
        "https://client.api.paklean.com/user/resendCode",
        "https://mobogift.com/signin",
        "https://api.iranicard.ir/api/v1/register",
        "https://tj8.ir/auth/register",
        "https://mashinbank.com/api2/users/check",
        "https://cinematicket.org/api/v1/users/signup",
        "https://www.irantic.com/api/login/request",
        "https://kafegheymat.com/shop/getLoginSms",
        "https://api.snapp.express/mobile/v4/user/loginMobileWithNoPass?client=PWA&optionalClient=PWA&deviceType=PWA&appVersion=5.6.6&optionalVersion=5.6.6&UDID=bb65d956-f88b-4fec-9911-5f94391edf85",
        "https://www.delino.com/user/register",
        "https://alopeyk.com/api/sms/send.php",
        "https://1401api.tamland.ir/api/user/signup",
        "https://shop.opco.co.ir/index.php?route=extension/module/login_verify/update_register_code",
        "https://api.digikalajet.ir/user/login-register/",
        "https://melix.shop/site/api/v1/user/otp",
        "https://safiran.shop/login",
        "https://restaurant.delino.com/user/register",
        "https://garcon.tandori.ir/users/v1/main/login",
        "https://dastkhat-isad.ir/api/v1/user/store",
        "https://irwco.ir/register",
        "https://api.sibbank.ir/v1/auth/login",
        "https://api.snapp.ir/api/v1/sms/link",
        "https://www.miare.ir/api/otp/driver/request/",
        "https://api.arshiyan.com/send_code",
        "https://backend.topnoor.ir/web/v1/user/otp",
        "https://api.alinance.com/user/register/mobile/send/",
        "https://api.alopeyk.com/safir-service/api/v1/login",
        "https://api.dadhesab.ir/user/entry",
        "https://app.dosma.ir/sendverify/",
        "https://api.ehteraman.com/api/request/otp",
        "https://api-ebcom.mci.ir/services/auth/v1.0/otp",
        "https://api.hbbs.ir/authentication/SendCode",
        "https://api.iranamlaak.net/authenticate/send/otp/to/mobile/via/sms",
        "https://api.kcd.app/api/v1/auth/login",
        "https://mazoocandle.ir/login",
        "https://api.ostadkr.com/login",
        "https://api.paymishe.com/api/v1/otp/registerOrLogin",
        "https://api.rayshomar.ir/api/Register/RegistrMobile",
        "https://refahtea.ir/wp-admin/admin-ajax.php",
        "https://digitalsignup.snapp.ir/oauth/drivers/api/v1/otp",
        "https://mamifood.org/Registration.aspx/SendValidationCode",
        "https://server.uphone.ir/api/v1/login/otp/request",
        "https://abantether.com/users/register/phone/send/",
        "https://www.glite.ir/wp-admin/admin-ajax.php",
        "https://novinbook.com/index.php?route=account/phone",
        "https://api.offch.com/auth/otp",
        "https://sandbox.sibbazar.com/api/v1/user/invite",
        "https://sabziman.com/wp-admin/admin-ajax.php",
        "https://api.watchonline.shop/api/v1/otp/request",
        "https://abantether.com/users/register/phone/send/",
        "https://flightio.com/bff/Authentication/CheckUserKey",
        "https://shadmessenger12.iranlms.ir/",
        "https://agent.wide-app.ir/auth/token",
        "https://tap33.me/api/v2/user",
        "https://apollo.digify.shop/graphql",
        "https://api.snapp.market/mart/v1/user/loginMobileWithNoPass?cellphone=%v",
        "https://auth.mrbilit.com/api/login/exists/v2?mobileOrEmail=%v&source=2&sendTokenIfNot=true",
        "https://api.chartex.net/api/v2/user/validate",
        "https://www.snapptrip.com/register",
        "https://api-v2.filmnet.ir/access-token/users/%v/otp",
        "https://api.bitpin.ir/v1/usr/sub_phone/",
        "https://chamedoon.com/api/v1/membership/guest/request_mobile_verification",
        "https://www.shab.ir/api/fa/sandbox/v_1_4/auth/enter-mobile",
        "https://api.raybit.net:3111/api/v1/authentication/register/mobile",
        "https://api.torob.com/a/phone/send-pin/?phone_number=%s",
        "https://www.namava.ir/api/v1.0/accounts/registrations/by-phone/request",
        "https://gw.taaghche.com/v4/site/auth/signup",
        "https://core.gap.im/v1/user/add.json?mobile=%2B%s",
        "https://app.mydigipay.com/digipay/api/users/send-sms",
        "https://gateway.wisgoon.com/api/v1/auth/login/",
        "https://tagmond.com/phone_number",
        "https://api.doctoreto.com/api/web/patient/v1/accounts/register",
        "https://api.anargift.com/api/people/auth",
        "https://www.azki.com/api/core/app/user/checkLoginAvailability/%7B'phoneNumber':'azki_%v'%7D",
        "https://lendo.ir/register?",
        "https://www.olgoobooks.ir/sn/userRegistration/?&requestedByAjax=1&elementsId=userRegisterationBox",
        "https://www.pakhsh.shop/wp-admin/admin-ajax.php",
        "https://api.basalam.com/user",
        "https://crm.see5.net/api_ajax/sendotp.php",
        "https://www.simkhanapi.ir/api/users/registerV2",
        "https://my.limoome.com/api/auth/login/otp",
        "https://www.mihanpezeshk.com/ConfirmCodeSbm_Patient",
        "https://i.devslop.app/app/ifollow/api/otp.php/",
        "https://behzadshami.com/wp-admin/admin-ajax.php",
        "https://restaurant.delino.com/user/register",
        "http://shop.tnovin.com/login",
        "https://dastkhat-isad.ir/api/v1/user/store",
        "https://hamlex.ir/register.php",
        "https://moshaveran724.ir/m/pms.php",
        "https://account.api.balad.ir/api/web/auth/login/",
        "https://app.flightio.com/bff/Authentication/CheckUserKey",
        "https://www.foodcenter.ir/account/sabtmobile",
        "https://auth.homtick.com/api/V1/User/GetVerifyCode",
        "https://app.kardoon.ir:4433/api/users",
        "https://abantether.com/users/register/phone/send/",
        "https://amoomilad.demo-hoonammaharat.ir/api/v1.0/Account/Sendcode",
        "https://ashraafi.com/wp-admin/admin-ajax.php",
        "https://bandarazad.com/wp-admin/admin-ajax.php",
        "https://bazidone.com/wp-admin/admin-ajax.php",
        "https://www.bigtoys.ir/wp-admin/admin-ajax.php",
        "https://bitex24.com/api/v1/auth/sendSms?mobile=%s&dial_code=0",
        "https://farsgraphic.com/wp-admin/admin-ajax.php",
        "https://www.instagram.com/accounts/account_recovery_send_ajax/",
        "https://shop.hemat-elec.ir/wp-admin/admin-ajax.php",
        "https://www.mipersia.com/wp-admin/admin-ajax.php",
        "https://www.kodakamoz.com/wp-admin/admin-ajax.php",
        "https://tajtehran.com/RegisterRequest",
        "https://zivanpet.com/wp-admin/admin-ajax.php",
        "https://api-react.okala.com/C/CustomerAccount/OTPRegister",
        "https://client.api.paklean.com/user/resendVoiceCode",
        "https://web.raghamapp.com/api/users/code",
        "https://gateway.trip.ir/api/registers",
        "https://gateway.trip.ir/api/Totp"
    ]

    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8')

settings = Settings()
