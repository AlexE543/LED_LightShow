import requests
from dotenv import load_dotenv
import os
load_dotenv()

# Step one of authorization: Call this function with your client id, scope, and redirect uri then copy and paste the url it
# returns into your browser to authorize.
def authorize():
    url = 'https://accounts.spotify.com/authorize'
    params = {
        "redirect_uri": os.getenv("REDIRECT_URI"),
        "scope": 'user-read-currently-playing user-top-read user-read-recently-played user-read-playback-state user-modify-playback-state streaming app-remote-control',
        "client_id": os.getenv("CLIENT_ID"),
        "response_type": "code",
        "show_dialog": "true",
    }
    res = requests.get(url, params)
    print("Status Code: ", res.status_code)
    return res.url

# Step two of authorization: Take the code from the redirect uri that the previous part gives you and call this function
# with your client id, client secret, and redirect uri. This should give you and access token and a refresh token.
# Use the access token to make api calls and use the refresh token to get new authorization tokens every hour.
def part_2():
    url2 = 'https://accounts.spotify.com/api/token'
    payload = {
        "code": os.getenv("CODE"),
        "client_id": os.getenv("CLIENT_ID"),
        "client_secret": os.getenv("CLIENT_SECRET"),
        "grant_type": "authorization_code",
        "redirect_uri": os.getenv("REDIRECT_URI")
    }
    result = requests.post(url2, data=payload).json()
    access_token, refresh_token = result["access_token"], result["refresh_token"]
    return access_token, refresh_token

# Takes in a refresh token from earlier as well as base 64 encoded client_id:client_secret and returns a new
# authorization code
def use_refresh_token(refresh_token):
    url = "https://accounts.spotify.com/api/token"
    params = {
        "grant_type": "refresh_token",
        "refresh_token": refresh_token
    }
    header = {
        "Authorization": "Basic MDg2MGMzZjlkN2Y0NDQ5YzgxYTA2YjFlNTRlZDNkMTY6ZTVlYzMwMGMzNDM4NGJhYTljY2E5ZGE3YzM3MjA2MGQ="
    }
    res = requests.post(url, headers=header, data=params)
    print(res.status_code)
    return res.json()["access_token"]

if __name__ == "__main__":
    # print(authorize())
    access_token, refresh_token = part_2()
    print(access_token)
    print(refresh_token)
    # use_refresh_token(refresh_token)
