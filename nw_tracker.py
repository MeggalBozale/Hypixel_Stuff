# Tracks my networth over time.
import json
import time, datetime

data_dict = {
    "coins" : 0,
    "timestamp": time.time()
}

def ask_user():
    while True:
        try:
            return float(input("Coins: "))
        except:
            print("Invalid input, try again or use keyboard interrupt to exit")
            pass

def record_data(file_to_write, data):
    with open(file_to_write,'a') as file:
        file.write(json.dumps(data) + '\n')

data_dict["coins"] = ask_user()
record_data("networth.json", data_dict)