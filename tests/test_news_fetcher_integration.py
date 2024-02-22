
import pytest
import news_fetcher

def test_get_news_integration():
    response = news_fetcher.get_news('test_api_key', 'us', 'en')
    assert 'data' in response
