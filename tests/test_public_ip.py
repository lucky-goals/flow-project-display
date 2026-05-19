from unittest.mock import patch, Mock

from src.public_ip import get_public_ip


class TestGetPublicIpSuccess:
    @patch("src.public_ip.requests.get")
    def test_returns_valid_ipv4(self, mock_get):
        mock_response = Mock()
        mock_response.text = "203.0.113.1"
        mock_response.raise_for_status = Mock()
        mock_get.return_value = mock_response

        result = get_public_ip()
        assert result == "203.0.113.1"


class TestGetPublicIpFailure:
    @patch("src.public_ip.requests.get")
    def test_network_error_returns_none(self, mock_get):
        mock_get.side_effect = Exception("Network unreachable")

        result = get_public_ip()
        assert result is None
