from unittest.mock import patch, Mock

from src.public_ip import get_public_ip


def _make_response(ip):
    r = Mock()
    r.text = ip
    r.raise_for_status = Mock()
    return r


class TestPrimarySourceSuccess:
    @patch("src.public_ip.requests.get")
    def test_primary_source_returns_ip(self, mock_get):
        mock_get.return_value = _make_response("203.0.113.1")
        assert get_public_ip() == "203.0.113.1"


class TestFallback:
    @patch("src.public_ip.requests.get")
    def test_fallback_to_secondary_when_primary_fails(self, mock_get):
        mock_get.side_effect = [Exception("primary down"), _make_response("198.51.100.2")]
        result = get_public_ip()
        assert result == "198.51.100.2"


class TestAllSourcesFail:
    @patch("src.public_ip.requests.get")
    def test_returns_none_when_all_sources_fail(self, mock_get):
        mock_get.side_effect = Exception("all down")
        assert get_public_ip() is None


class TestTimeout:
    @patch("src.public_ip.requests.get")
    def test_timeout_is_handled(self, mock_get):
        import requests as req
        mock_get.side_effect = req.exceptions.Timeout("timed out")
        assert get_public_ip() is None


class TestIPFormatValidation:
    @patch("src.public_ip.requests.get")
    def test_invalid_ip_format_treated_as_failure(self, mock_get):
        mock_get.return_value = _make_response("not-an-ip")
        assert get_public_ip() is None

    @patch("src.public_ip.requests.get")
    def test_valid_ipv6_accepted(self, mock_get):
        mock_get.return_value = _make_response("2001:db8::1")
        result = get_public_ip()
        assert result == "2001:db8::1"


class TestRetry:
    @patch("src.public_ip.requests.get")
    def test_retries_at_least_once_on_failure(self, mock_get):
        mock_get.side_effect = [Exception("first attempt"), _make_response("203.0.113.5")]
        result = get_public_ip()
        assert result == "203.0.113.5"
        assert mock_get.call_count >= 2
