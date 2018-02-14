from newsapi import NewsApiClient
import os

api_key = os.getenv('api_key', "world")
api = NewsApiClient(api_key=api_key)
print(api.get_top_headlines(sources='bbc-news'))
