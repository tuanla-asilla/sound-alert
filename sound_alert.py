from flask import Flask
from flask import request
from flask import json
from playsound import playsound

app = Flask(__name__)

SOUND_FILE_PATH = "alert.mp3"

@app.route('/sound_alert', methods=['GET', 'POST'])
def sound_alert():
    print("Play sound file: ")
    playsound(SOUND_FILE_PATH)
    return 'OK'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
