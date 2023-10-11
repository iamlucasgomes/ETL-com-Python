import json
import csv


def extract_json_to_csv(json_file_path, csv_file_path):
    try:
        with open(json_file_path, "r") as json_file, open(
            csv_file_path, "w", newline=""
        ) as csv_file:
            data = json.load(json_file)
            user_field = "id"

            writer = csv.DictWriter(csv_file, fieldnames=[user_field])
            writer.writeheader()

            for item in data:
                user_id = item.get(user_field)
                if user_id is not None:
                    writer.writerow({user_field: user_id})
    except Exception as e:
        print(f"An error occurred: {e}")


json_file_path = "data/data.json"
csv_file_path = "data/data.csv"

extract_json_to_csv(json_file_path, csv_file_path)
