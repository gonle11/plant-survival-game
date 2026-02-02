import csv
from datetime import datetime
import os

FILE_NAME = "scores.csv"

def save_score(player_name, time_survived):
    file_exists = os.path.isfile(FILE_NAME)

    with open(FILE_NAME, mode="a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)

        if not file_exists:
            writer.writerow(["player", "time", "date"])

        writer.writerow([
            player_name,
            time_survived,
            datetime.now().isoformat()
        ])
