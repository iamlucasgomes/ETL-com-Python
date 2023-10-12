import json
import csv


def extract_id_from_json_to_csv(json_file_path: str, csv_file_path: str):
    try:
        with open(json_file_path, "r") as json_file, open(
            csv_file_path, "w", newline=""
        ) as csv_file:
            data = json.load(json_file)
            user_field = "id"
            user_header = "UserID"

            writer = csv.DictWriter(csv_file, fieldnames=[user_header])
            writer.writeheader()

            for item in data:
                user_id = item.get(user_field)
                if user_id is not None:
                    writer.writerow({user_header: user_id})
    except Exception as e:
        print(f"An error occurred: {e}")
