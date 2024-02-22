
unittest:
	pytest -k test_news_fetcher.py

integrationtest:
	pytest -k test_news_fetcher_integration.py
