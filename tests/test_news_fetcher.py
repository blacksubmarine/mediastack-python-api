
import pytest
from unittest.mock import patch, Mock
import news_fetcher

@patch('news_fetcher.requests.get')
def test_get_news(mock_get):
    mock_response = Mock()
    mock_response.json.return_value = {'data': 'mock_data'}
    mock_get.return_value = mock_response

    response = news_fetcher.get_news('dummy_api_key', 'us', 'en')
    assert response == {'data': 'mock_data'}
    mock_get.assert_called_once()
