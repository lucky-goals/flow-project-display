import ipaddress
import requests

_SOURCES = [
    "https://api.ipify.org",
    "https://api4.my-ip.io/ip",
    "https://checkip.amazonaws.com",
]
_TIMEOUT = 3


def _is_valid_ip(text: str) -> bool:
    try:
        ipaddress.ip_address(text.strip())
        return True
    except ValueError:
        return False


def _fetch(url: str) -> str | None:
    for _ in range(2):
        try:
            r = requests.get(url, timeout=_TIMEOUT)
            r.raise_for_status()
            ip = r.text.strip()
            if _is_valid_ip(ip):
                return ip
        except Exception:
            pass
    return None


def get_public_ip() -> str | None:
    for source in _SOURCES:
        result = _fetch(source)
        if result:
            return result
    return None
