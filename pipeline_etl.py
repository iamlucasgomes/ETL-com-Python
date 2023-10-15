# from util.save_response_in_json import save_response_in_json
# from util.extract_id_from_json_to_csv import extract_id_from_json_to_csv
from fetch.get_user import get_user
from fetch.update_user import update_user
from etl_util.extract import extract

from util.generate_ai_news import generate_ai_news

USERS_ENDPOINT = "https://sdw-2023-prd.up.railway.app/users"
JSON_FILE = "data.json"
CSV_FILE = "users_id.csv"
DIRECTORY = "data"
CSV_DIRECTORY = f"{DIRECTORY}/{CSV_FILE}"
JSON_DIRECTORY = f"{DIRECTORY}/{JSON_FILE}"
DIO_REPOSITORIES_ENDPOINT = "https://digitalinnovationone.github.io"
SANTANDER_DEV_WEEK_ENDPOINT = "santander-dev-week-2023-api"
CREDIT_SVG_ICON = "icons/credit.svg"
ENDPOINT = f"{DIO_REPOSITORIES_ENDPOINT}/{SANTANDER_DEV_WEEK_ENDPOINT}"


# Funções desativadas, porque o csv gerado tem mais de 2500 ids
# e a api não esta suportando esse tanto de requisição,
# pensarei em uma solução para isso

# save_response_in_json(USERS_ENDPOINT, JSON_FILE, DIRECTORY)

# extract_id_from_json_to_csv(JSON_DIRECTORY, CSV_DIRECTORY)

user_ids = extract(CSV_DIRECTORY)

users = [user for id in user_ids if (user := get_user(id, USERS_ENDPOINT))]

for user in users:
    news = generate_ai_news(user)
    user["news"].append(
        {
            "icon": f"{ENDPOINT}/{CREDIT_SVG_ICON}",
            "description": news,
        }
    )
    sucess = update_user(user, USERS_ENDPOINT)
    print(f"User {user['id']} updated with sucess" if sucess else "Error")
    print(user)
