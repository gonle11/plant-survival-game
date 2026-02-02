# score.py
import csv

def save_score(player_name, time_survived):
    with open("scores.csv", "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([player_name, time_survived])

def get_best_score():
    with open("scores.csv", newline="", encoding="utf-8") as f:
        reader = csv.reader(f)

        best_player = None
        best_time = -1

        for row in reader:
            player, time = row
            time = int(time)

            if time > best_time:
                best_time = time
                best_player = player

    return best_player, best_time
