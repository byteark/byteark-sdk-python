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
            "?x_ark_access_id=2Aj6Wkge4hi1ZYLp0DBG&x_ark_auth_type=ark-v2&x_ark_expires=1514764800"
            "&x_ark_signature=cLwtn96a-YPY7jt8ZKSf_Q"
    )


def test_byteark_signer_sign_with_HEAD_method(signer: ByteArkSigner):
    signed_url = signer.sign("http://inox.qoder.byteark.com/video-objects/QDuxJm02TYqJ/playlist.m3u8",
                             1514764800,
                             {"method": "HEAD"})
    assert (
            signed_url ==
            "http://inox.qoder.byteark.com/video-objects/QDuxJm02TYqJ/playlist.m3u8"
            "?x_ark_access_id=2Aj6Wkge4hi1ZYLp0DBG&x_ark_auth_type=ark-v2&x_ark_expires=1514764800"
            "&x_ark_signature=QULE8DQ08f8fhFC-1gDUWQ"
    )


def test_byteark_signer_sign_with_path_prefix(signer: ByteArkSigner):
    signed_url = signer.sign("http://inox.qoder.byteark.com/video-objects/QDuxJm02TYqJ/playlist.m3u8",
                             1514764800,
                             {"path_prefix": "/video-objects/QDuxJm02TYqJ/"})
    assert (
            signed_url ==
            "http://inox.qoder.byteark.com/video-objects/QDuxJm02TYqJ/playlist.m3u8"
            "?x_ark_access_id=2Aj6Wkge4hi1ZYLp0DBG&x_ark_auth_type=ark-v2&x_ark_expires=1514764800"
            "&x_ark_path_prefix=%2Fvideo-objects%2FQDuxJm02TYqJ%2F"
            "&x_ark_signature=334wInm0jKfC6LCm23zndA"
    )
