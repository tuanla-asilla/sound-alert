# Setup Sound Alert service
- install python 
```cmd
$ sudo apt-get install python3-pip 
$ pip3 install flask
$ pip3 install playsound
```

- created file soundalert service
crontab -e
```cmd

@reboot export XDG_RUNTIME_DIR="/run/user/1000" && cd /home/asilla/sound_alert && nohup python3 sound_alert.py >> sound_alert_service.log &

```

$ sudo nano /etc/systemd/system/soundalert.service


```cmd
[Unit]
Description=Sound Alert Service

[Service]
User=asilla
WorkingDirectory=/home/asilla/sound_alert
ExecStart=/usr/bin/python3 sound_alert.py
Restart=on-failure
Environment=XDG_RUNTIME_DIR="/run/user/1000"

[Install]
WantedBy=default.target

```
- Debug sound alert service
```cmd
# command systemd to refresh its configuration:

sudo systemctl daemon-reload
sudo systemctl restart soundalert
sudo systemctl status soundalert
# command to start, stop, restart or obtain status for your service
$ sudo systemctl start soundalert
$ sudo systemctl stop soundalert
$ sudo systemctl restart soundalert
$ sudo systemctl status soundalert
# enable auto start after reboot
$ sudo systemctl enable soundalert
journalctl -u soundalert -n 25

```
