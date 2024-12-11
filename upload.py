import pandas as pd
import pandas_gbq

from config import DATA_DIR, PROJECT_ID, DATASET_NAME, TABLE_NAME, LOCATION


def upload():
    table = pd.read_csv(f"{DATA_DIR}/industry_keywords.csv", dtype=str)
    print("Uploading...")
    pandas_gbq.to_gbq(table, f"{DATASET_NAME}.{TABLE_NAME}", project_id=PROJECT_ID, if_exists='replace', location=LOCATION)


if __name__ == "__main__":
    upload()