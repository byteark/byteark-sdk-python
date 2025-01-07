from datetime import UTC, datetime, timedelta

import pytest
from byteark_sdk import ByteArkSigner


@pytest.fixture
def signer() -> ByteArkSigner:
    return ByteArkSigner(
        access_key="2Aj6Wkge4hi1ZYLp0DBG",
        access_secret="31sX5C0lcBiWuGPTzRszYvjxzzI3aCZjJi85ZyB7",
    )


def test_byteark_signer(signer: ByteArkSigner):
    signed_url = signer.sign("http://inox.qoder.byteark.com/video-objects/QDuxJm02TYqJ/playlist.m3u8", 1514764800)
    assert (
            signed_url ==
            "http://inox.qoder.byteark.com/video-objects/QDuxJm02TYqJ/playlist.m3u8"
            "?x_ark_access_id=2Aj6Wkge4hi1ZYLp0DBG"
            "&x_ark_auth_type=ark-v2"
            "&x_ark_expires=1514764800"
            "&x_ark_signature=cLwtn96a-YPY7jt8ZKSf_Q"
    )


def test_byteark_signer_sign_with_HEAD_method(signer: ByteArkSigner):
    signed_url = signer.sign("http://inox.qoder.byteark.com/video-objects/QDuxJm02TYqJ/playlist.m3u8",
                             1514764800,
                             {"method": "HEAD"})
    assert (
            signed_url ==
            "http://inox.qoder.byteark.com/video-objects/QDuxJm02TYqJ/playlist.m3u8"
            "?x_ark_access_id=2Aj6Wkge4hi1ZYLp0DBG"
            "&x_ark_auth_type=ark-v2"
            "&x_ark_expires=1514764800"
            "&x_ark_signature=QULE8DQ08f8fhFC-1gDUWQ"
    )


def test_byteark_signer_sign_with_path_prefix(signer: ByteArkSigner):
    signed_url = signer.sign("http://inox.qoder.byteark.com/video-objects/QDuxJm02TYqJ/playlist.m3u8",
                             1514764800,
                             {"path_prefix": "/video-objects/QDuxJm02TYqJ/"})
    assert (
            signed_url ==
            "http://inox.qoder.byteark.com/video-objects/QDuxJm02TYqJ/playlist.m3u8"
            "?x_ark_access_id=2Aj6Wkge4hi1ZYLp0DBG"
            "&x_ark_auth_type=ark-v2"
            "&x_ark_expires=1514764800"
            "&x_ark_path_prefix=%2Fvideo-objects%2FQDuxJm02TYqJ%2F"
            "&x_ark_signature=334wInm0jKfC6LCm23zndA"
    )


def test_byteark_signer_sign_with_client_ip_dash(signer: ByteArkSigner):
    signed_url = signer.sign("http://inox.qoder.byteark.com/video-objects/QDuxJm02TYqJ/playlist.m3u8",
                             1514764800,
                             {"client_ip": "103.253.132.65"})
    assert (
            signed_url ==
            "http://inox.qoder.byteark.com/video-objects/QDuxJm02TYqJ/playlist.m3u8"
            "?x_ark_access_id=2Aj6Wkge4hi1ZYLp0DBG"
            "&x_ark_auth_type=ark-v2"
            "&x_ark_client_ip=1"
            "&x_ark_expires=1514764800"
            "&x_ark_signature=Gr9T_ZdHDy8l8CCPxpFjNg"
    )


def test_byteark_signer_sign_with_client_ip_underscore(signer: ByteArkSigner):
    signed_url = signer.sign("http://inox.qoder.byteark.com/video-objects/QDuxJm02TYqJ/playlist.m3u8",
                             1514764800,
                             {"client-ip": "103.253.132.65"})
    assert (
            signed_url ==
            "http://inox.qoder.byteark.com/video-objects/QDuxJm02TYqJ/playlist.m3u8"
            "?x_ark_access_id=2Aj6Wkge4hi1ZYLp0DBG"
            "&x_ark_auth_type=ark-v2"
            "&x_ark_client_ip=1"
            "&x_ark_expires=1514764800"
            "&x_ark_signature=Gr9T_ZdHDy8l8CCPxpFjNg"
    )


def test_byteark_signer_sign_with_user_agent(signer: ByteArkSigner):
    user_agent = (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/58.0.3029.68 Safari/537.36"
    )
    signed_url = signer.sign("http://inox.qoder.byteark.com/video-objects/QDuxJm02TYqJ/playlist.m3u8",
                             1514764800,
                             {
                                 "client-ip": "103.253.132.65",
                                 "user-agent": user_agent,
                             })
    assert (
            signed_url ==
            "http://inox.qoder.byteark.com/video-objects/QDuxJm02TYqJ/playlist.m3u8"
            "?x_ark_access_id=2Aj6Wkge4hi1ZYLp0DBG"
            "&x_ark_auth_type=ark-v2"
            "&x_ark_client_ip=1"
            "&x_ark_expires=1514764800"
            "&x_ark_signature=yYFkwZolbxCarOLHuKjD7w"
            "&x_ark_user_agent=1"
    )


def test_byteark_signer_sign_with_client_ip_with_path_prefix(signer: ByteArkSigner):
    signed_url = signer.sign("http://inox.qoder.byteark.com/video-objects/QDuxJm02TYqJ/playlist.m3u8",
                             1514764800,
                             {
                                 "client-ip": "103.253.132.65",
                                 "path_prefix": "/video-objects/QDuxJm02TYqJ/",
                             })
    assert (
            signed_url ==
            "http://inox.qoder.byteark.com/video-objects/QDuxJm02TYqJ/playlist.m3u8"
            "?x_ark_access_id=2Aj6Wkge4hi1ZYLp0DBG"
            "&x_ark_auth_type=ark-v2"
            "&x_ark_client_ip=1"
            "&x_ark_expires=1514764800"
            "&x_ark_path_prefix=%2Fvideo-objects%2FQDuxJm02TYqJ%2F"
            "&x_ark_signature=2bkwVFSu6CzW7KmzXkwDbA"
    )


def test_byteark_signer_create_default_expire(signer: ByteArkSigner):
    now = datetime.now(UTC)
    expire = signer._create_default_expire()

    assert isinstance(expire, int)
    assert expire >= int((now + timedelta(seconds=signer.default_age)).timestamp())
