import requests
from dotenv import load_dotenv
import os
import time
import functions as func
import board
import neopixel
load_dotenv()

def get_current_track_id():
    url = "https://api.spotify.com/v1/me/player/currently-playing"
    header = {
        "Authorization": "Bearer " + os.getenv("ACCESS_TOKEN"),
        "Accept": "application/json",
        "Content-Type": "application/json",
        "market": "US"
    }
    res = requests.get(url, headers=header)
    print(res.status_code)
    return res.json()["item"]["id"]

def get_current_track_analysis(current_id):
    print(current_id)
    url = "https://api.spotify.com/v1/audio-analysis/" + current_id
    header = {
        "Authorization": "Bearer " + os.getenv("ACCESS_TOKEN"),
        "Accept": "application/json",
        "Content-Type": "application/json",
        "market": "US"
    }
    res = requests.get(url, headers=header)
    print(res.status_code)
    res = res.json()
    tempo = res["track"]["tempo"]
    time_sig = res["track"]["time_signature"]
    bars = res["bars"]
    segments = res["segments"]
    return tempo, time_sig, bars, segments

def start_song(bars):
    infourl = "https://api.spotify.com/v1/me/player"
    seekurl = "https://api.spotify.com/v1/me/player/seek"
    pauseurl = ""
    url = "https://api.spotify.com/v1/me/player/play"
    header = {
        "Authorization": "Bearer " + os.getenv("ACCESS_TOKEN"),
        "Accept": "application/json",
        "Content-Type": "application/json"
    }
    # Check Currently playing/loaded music
    res1 = requests.get(infourl, headers=header)
    print(res1.status_code)
    if res1.json()["is_playing"] != False or not res1.json()["device"]["is_active"] or res1.json()["progress_ms"] != 0:
        data = {
            "position_ms": "0"
        }
        res2 = requests.put(seekurl, headers=header, params=data)
        print(res2.status_code)
    res = requests.put(url, headers=header)
    pulse_to_bars(bars)
    print(res.status_code)



def pulse_to_bars(bars):
    strip = neopixel.NeoPixel(board.D18, 144, brightness=0.3, auto_write=False)
    print("Starting Song")
    time.sleep(bars[0]["start"] - .2)
    for bar in bars:
        print("BOOP")
        func.fade(strip, (255, 255, 255))
        time.sleep(bar["duration"] - .12)
    return


if __name__ == "__main__":
    current_id = get_current_track_id()
    tempo, time_sig, bars, segments = get_current_track_analysis(current_id)
    # pulse_to_bars(bars)
    start_song(bars)

