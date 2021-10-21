from flask import Flask
from flask import request
from flask import json
from playsound import playsound

app = Flask(__name__)


@app.route('/sound_alert', methods=['GET', 'POST'])
def sound_alert():
    sound_path = "alert.mp3"
    playsound(sound_path)
    return 'OK'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
