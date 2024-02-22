# test_news_fetcher.py
import unittest
from unittest.mock import patch
from news_fetcher import get_news  # Make sure this matches your module's name and function

class TestNewsFetcher(unittest.TestCase):

    @patch('news_fetcher.requests.get')
    def test_get_news(self, mock_get):
        # Dummy data simulating the API response
        mock_response = {
            "data": [{"title": "Test News", "description": "This is a test news description."}]
        }
        mock_get.return_value.json.return_value = mock_response

        api_key = 'dummy_api_key'
        response = get_news(api_key, 'us', 'en')
        self.assertEqual(response, mock_response)

if __name__ == '__main__':
    unittest.main()
