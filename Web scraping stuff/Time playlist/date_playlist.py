from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import requests

CLIENT_ID = "a8264d2955eb4f9b84fb559eb0732c84"
CLIENT_SECRET = "823e48e6a86748fdb2972f00e3103d59"

def get_track_uri(track_name):
    result = sp.search(q=track_name, type='track', limit=1)
    if result['tracks']['items']:
        track_uri = result['tracks']['items'][0]['uri']
        return track_uri
    else:
        print(f"Track not found: {track_name}")
        return None

date = input("What date's playlist would you like to be created?(YYYY-MM-DD)\n")
url = f"https://www.billboard.com/charts/hot-100/{date}/"

response = requests.get(url).text
soup = BeautifulSoup(response,"html.parser")
songs = soup.select("li ul li h3")

song_names  = [song.getText().strip() for song in songs]

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                               client_secret=CLIENT_SECRET,
                                               redirect_uri='http://example.com/',
                                               scope='playlist-modify-private',
                                               cache_path="token.txt",
                                               show_dialog=True))

song_uris = []
year = date.split("-")[0]
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

user_id = sp.current_user()["id"]

playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)

