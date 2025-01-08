# ByteArk SDK for Python

## Usage

```python
from byteark_sdk import ByteArkSigner

signer = ByteArkSigner(
    access_key="2Aj6Wkge4hi1ZYLp0DBG",
    access_secret="31sX5C0lcBiWuGPTzRszYvjxzzI3aCZjJi85ZyB7"
)
signed_url = signer.sign(
    'https://example.cdn.byteark.com/path/to/file.png',
    1514764800
)
print(signed_url)

# Output:
#    https://example.cdn.byteark.com/path/to/file.png
#       ?x_ark_access_id=2Aj6Wkge4hi1ZYLp0DBG
#       &x_ark_auth_type=ark-v2
#       &x_ark_expires=1514764800
#       &x_ark_signature=OsBgZpn9LTAJowa0UUhlYQ
```
