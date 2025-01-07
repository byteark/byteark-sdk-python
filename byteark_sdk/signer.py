import base64
import hashlib
import urllib.parse
from collections import OrderedDict
from urllib.parse import urlparse


class MissingOptions(Exception):
    pass


class ByteArkSigner:
    def __init__(self, **options):
        self.access_key = options.get('access_key')
        self.access_secret = options.get('access_secret')
        self.default_age = options.get('default_age', 900)
        self.skip_url_encode = options.get('skip_url_encode', False)

        self._check_options()

    def _check_options(self):
        if not self.access_key:
            raise MissingOptions('access_key is required')
        if not self.access_secret:
            raise MissingOptions('access_secret is required')

    def _make_string_to_sign(self, url: str, expire: int, options: dict = {}):
        parsed_url = urlparse(url)
        host = parsed_url.netloc
        method = options.get("method", "GET")

        elements = []
        elements.append(method)
        elements.append(host)

        if "path_prefix" in options:
            elements.append(options["path_prefix"])
        else:
            elements.append(parsed_url.path)

        if "client_ip" in options:
            elements.append(f"client_ip:{options['client_ip']}")

        if "user_agent" in options:
            elements.append(f"user_agent:{options['user_agent']}")

        elements.append(str(expire))
        elements.append(self.access_secret)

        return "\n".join(elements)

    def _make_signature(self, string_to_sign: str):
        h = hashlib.md5()
        h.update(string_to_sign.encode('utf-8'))
        hash_str = base64.b64encode(h.digest()).decode('utf-8')

        hash_str = hash_str.replace("+", "-")
        hash_str = hash_str.replace("/", "_")
        hash_str = hash_str.rstrip("=")
        return hash_str

    def sign(self, url: str, expire: int, options: dict = {}) -> str:
        if expire == 0:
            expire = self.default_age

        options_ = {}
        for k in options:
            v = options[k]
            k = k.lower().replace("-", "_")
            options_[k] = v
        options = options_

        params = OrderedDict([
            ("x_ark_access_id", self.access_key),
            ("x_ark_auth_type", "ark-v2"),
            ("x_ark_expires", expire),
            ("x_ark_signature", self._make_signature(self._make_string_to_sign(url, expire, options))),
        ])

        if "path_prefix" in options:
            params["x_ark_path_prefix"] = options["path_prefix"]

        if "client_ip" in options:
            params["x_ark_client_ip"] = "1"

        if "user_agent" in options:
            params["x_ark_user_agent"] = "1"

        params = OrderedDict(sorted(params.items()))
        query_string = urllib.parse.urlencode(params)
        signed_url = f"{url}?{query_string}"

        return signed_url


__all__ = ['ByteArkSigner']
