from byteark_sdk import ByteArkSigner


def test_byteark_signer():
    signer = ByteArkSigner(
        access_key="2Aj6Wkge4hi1ZYLp0DBG",
        access_secret="31sX5C0lcBiWuGPTzRszYvjxzzI3aCZjJi85ZyB7",
    )
    signed_url = signer.sign("http://inox.qoder.byteark.com/video-objects/QDuxJm02TYqJ/playlist.m3u8", 1514764800)
    assert (
            signed_url ==
            "http://inox.qoder.byteark.com/video-objects/QDuxJm02TYqJ/playlist.m3u8"
            "?x_ark_access_id=2Aj6Wkge4hi1ZYLp0DBG&x_ark_auth_type=ark-v2&x_ark_expires=1514764800"
            "&x_ark_signature=cLwtn96a-YPY7jt8ZKSf_Q"
    )
