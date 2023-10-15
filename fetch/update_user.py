import requests


def update_user(user: dict, endpoint: str):
    response = requests.put(f"{endpoint}/{user['id']}", json=user)
    return True if response.status_code == 200 else False
