import threading
import time
import requests


def call_play_sound_alert_api():
    start_time = time.time()
    response = requests.get("http://192.168.1.10:5000/sound_alert")
    print("Time:", time.time() - start_time, ":", response)
    time.sleep(1)

def play_sound_alert():
    threading.Thread(target=call_play_sound_alert_api).start()

start_time = time.time()
play_sound_alert()
print("Time:", time.time() - start_time,)

start_time = time.time()
response = requests.get("http://192.168.1.10:5000/sound_alert")
print("Time:", time.time() - start_time, ":", response)
print("Success play sound")

