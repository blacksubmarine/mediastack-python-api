import requests
from typing import Dict

def get_news(api_key: str, countries: str = 'us', languages: str = 'en') -> Dict:
    """
    Fetch news articles using the Mediastack API.

    Parameters:
    - api_key (str): Your Mediastack API key.
    - countries (str): Comma-separated country codes to filter news by country.
    - languages (str): Comma-separated language codes to filter news by language.

    Returns:
    - dict: A dictionary containing the API response.
    """
    base_url = 'http://api.mediastack.com/v1/news'
    params = {
        'access_key': api_key,
        'countries': countries,
        'languages': languages,
    }
    response = requests.get(base_url, params=params)
    return response.json()

# Example usage
if __name__ == '__main__':
    api_key = 'YOUR_API_KEY'  # Replace with your actual API key
    news_data = get_news(api_key, 'us', 'en')
    print(news_data)
