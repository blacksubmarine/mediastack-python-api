
import requests

def get_news(api_key: str, countries: str = 'us', languages: str = 'en'):
    base_url = 'http://api.mediastack.com/v1/news'
    params = {
        'access_key': api_key,
        'countries': countries,
        'languages': languages,
    }
    response = requests.get(base_url, params=params)
    return response.json()
