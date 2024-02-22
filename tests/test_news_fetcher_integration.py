# test_news_fetcher.py
import pytest
from unittest.mock import patch, Mock
import news_fetcher  # Assuming your script is named news_fetcher.py

@patch('news_fetcher.requests.get')
def test_get_news(mock_get):
    # Mock response data
    mock_response = Mock()
    mock_response.json.return_value = {'data': 'mock_data'}
    mock_get.return_value = mock_response

    # Call the function
    response = news_fetcher.get_news('dummy_api_key', 'us', 'en')

    # Assertions
    assert response == {'data': 'mock_data'}
    mock_get.assert_called_once()
