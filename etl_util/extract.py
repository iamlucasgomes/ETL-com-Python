import pandas as pd


def extract(csv_file_path: str):
    try:
        df = pd.read_csv(csv_file_path)
        user_id = df["UserID"].tolist()
        return user_id
    except Exception as e:
        print(f"An error occurred: {e}")
