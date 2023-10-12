import requests


def get_user(id: int, endpoint: str):
    response = requests.get(f"{endpoint}/{id}")
    return response.json() if response.status_code == 200 else None
