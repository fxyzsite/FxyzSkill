import requests

staticmethod


def request(url: str, method: str = "get", params=None):
    if method == 'post':
        response = requests.post(url, params=params)
        return response.content.decode('utf-8')
    else:
        response = requests.get(url, params=params)
        return response.content.decode('utf-8')
