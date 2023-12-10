# This contains functions that should only be used inside the BeReal class. Please instantiate a BeReal class and use its implementation of these functions

import requests
from .constants import GOOGLE_API_KEY, HEADERS, BEREAL_HEADERS


def request_code(phone_number: str, device_id: str, base_url: str):
    receipt = requests.post(
        "https://www.googleapis.com/identitytoolkit/v3/relyingparty/verifyClient",
        params={"key": GOOGLE_API_KEY},
        json={
            "appToken": "54F80A258C35A916B38A3AD83CA5DDD48A44BFE2461F90831E0F97EBA4BB2EC7"
        },
        headers={
            "x-client-version": "iOS/FirebaseSDK/9.6.0/FirebaseCore-iOS",
            "x-ios-bundle-identifier": "AlexisBarreyat.BeReal",
            "accept-language": "en",
            "user-agent": "FirebaseAuth.iOS/9.6.0 AlexisBarreyat.BeReal/0.31.0 iPhone/14.7.1 hw/iPhone9_1",
            "x-firebase-locale": "en",
            "x-firebase-gmpid": "1:405768487586:ios:28c4df089ca92b89",
            "Content-Type": "application/json",
        },
    )

    firebase_receipt = receipt.json()

    res = requests.post(
        "https://www.googleapis.com/identitytoolkit/v3/relyingparty/sendVerificationCode",
        params={"key": GOOGLE_API_KEY},
        data={"phoneNumber": phone_number, "iosReceipt": firebase_receipt["receipt"]},
        headers=HEADERS,
    )

    otp_response = res.json()

    return otp_response


def get_code(refresh_token: str):
    res = requests.post(
        "https://securetoken.googleapis.com/v1/token?key=" + GOOGLE_API_KEY,
        json={"refreshToken": refresh_token, "grantType": "refresh_token"},
        headers={
            "User-Agent": "BeReal/8586 CFNetwork/1240.0.4 Darwin/20.6.0",
            "x-ios-bundle-identifier": "AlexisBarreyat.BeReal",
            "Content-Type": "application/json",
        },
    )

    response = res.json()
    firebase_token = response["id_token"]

    bereal_access_res = requests.post(
        "https://auth.bereal.team/token?grant_type=firebase",
        json={
            "grant_type": "firebase",
            "client_id": "ios",
            "client_secret": "962D357B-B134-4AB6-8F53-BEA2B7255420",
            "token": firebase_token,
        },
        headers={
            "User-Agent": "BeReal/8586 CFNetwork/1240.0.4 Darwin/20.6.0",
            "x-ios-bundle-identifier": "AlexisBarreyat.BeReal",
            "Content-Type": "application/json",
        },
    )
    return bereal_access_res.json()


def verify_code(otp_session: str, otp: str):
    res = requests.post(
        "https://www.googleapis.com/identitytoolkit/v3/relyingparty/verifyPhoneNumber",
        params={"key": "AIzaSyDwjfEeparokD7sXPVQli9NsTuhT6fJ6iA"},
        data={"sessionInfo": otp_session, "code": otp, "operation": "SIGN_UP_OR_IN"},
        headers=HEADERS,
    )

    return res.json()


def refresh_session(refresh_token: str):
    res = requests.post(
        "https://auth.bereal.team/token?grant_type=refresh_token",
        params={"grant_type": "refresh_token"},
        data={
            "refresh_token": refresh_token,
            "grant_type": "refresh_token",
            "client_id": "ios",
            "client_secret": "962D357B-B134-4AB6-8F53-BEA2B7255420",
        },
        headers=BEREAL_HEADERS,
    )


    resp = res.json()
    return (resp["id_token"], resp["refresh_token"])
