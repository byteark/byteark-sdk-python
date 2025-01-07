from .signer import ByteArkSigner


def test_create_signer():
    signer = ByteArkSigner()
    assert signer is not None
