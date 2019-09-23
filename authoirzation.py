import requests

auth_url = 'https://accounts.spotify.com/authorize?' + 'client_id=' + '65b4c22ec2644e11abf6b37d8fec5fbd' + \
            '&response_type=' + 'token' + '&redirect_uri=' + 'http://localhost:8000/callback/' + '&show_dialog=true' + \
           '&scope=' + 'user-read-currently-playing user-top-read user-read-recently-played user-read-playback-state user-modify-playback-state streaming app-remote-control'

r = requests.get(auth_url)
print(r.status_code)
print(r.text)

