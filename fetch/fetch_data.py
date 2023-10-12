import requests


def fetch_data(endpoint: str):
    request = requests.get(endpoint)
    return request.json()
