import json
import os
from fetch.fetch_data import fetch_data


def save_response_in_json(endpoint: str, filename: str, directory: str):
    response = fetch_data(endpoint)

    if directory:
        os.makedirs(directory, exist_ok=True)

    full_path = os.path.join(directory, filename)
    with open(full_path, "w") as outfile:
        json.dump(response, outfile, indent=4)
