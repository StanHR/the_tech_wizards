import newsapi
import json
import requests

def get_json_response(apiKey, resource='the-times-of-india'):
    url = 'https://newsapi.org/v1/articles/'
    params = {'source': resource,
              'apiKey': 'e9ee0a55cc184d7abb5495457a625bb3'}
    r = requests.get(url, params=params)
    print(r.status_code)
    print(r.text)
    # etc.
print(get_json_response('e9ee0a55cc184d7abb5495457a625bb3'))