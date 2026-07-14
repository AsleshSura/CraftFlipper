import requests
import json

from datetime import datetime, timezone
import os

import shutil


def BazaarRequest():
    response = requests.get("https://api.hypixel.net/v2/skyblock/bazaar")
    data = response.json()

    return data

def DataStorage(data):
    unix_timestamp = data['lastUpdated']
    
    date = datetime.fromtimestamp(unix_timestamp/1000, tz=timezone.utc)
    folder_date = date.strftime("%Y-%m-%d")
    filename = date.strftime("%H-%M-%S.json")

    target_folder = os.path.join("Data", folder_date)

    os.makedirs(target_folder, exist_ok=True)

    full_filepath = os.path.join(target_folder, filename)


    with open(full_filepath, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)

def ClearStorage():
    folder_path = "Data"

    if os.path.exists(folder_path):
        shutil.rmtree(folder_path)
    
    os.makedirs(folder_path, exist_ok=True)

