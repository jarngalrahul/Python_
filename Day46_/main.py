from spotipy.oauth2 import SpotifyOAuth
from bs4 import BeautifulSoup
import requests
import spotipy
import pprint
from data import SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET

REDIRECT_URI = "http://example.com"
spotify_auth = SpotifyOAuth(
    client_id=SPOTIPY_CLIENT_ID,
    client_secret=SPOTIPY_CLIENT_SECRET,
    redirect_uri=REDIRECT_URI,
    scope="playlist-modify-private",
    cache_path="token.txt"
)
# -----------Getting a date from user to find top 100 songs--------------#
date = input("Enter the date in the yyyy-mm-dd format: ")
URL = f"https://www.billboard.com/charts/hot-100/{date}"

content = requests.get(URL)
website_text = content.text
soup = BeautifulSoup(website_text, "html.parser")
# list of songs
lst = []
songs = soup.select(
    selector=".o-chart-results-list__item .c-title")
for song_name in songs:
    song = song_name.getText().strip()
    if song != "":
        lst.append(song)


sp = spotipy.Spotify(auth_manager=spotify_auth)
user_id = sp.current_user()['id']

spotify_song_list = []
# -------------------Searching songs in the list--------------------#
for val in lst:
    res = sp.search(q=f"track:{val}", type="track")
    try:
        new_song = res['tracks']['items'][0]['uri']
        spotify_song_list.append(new_song)
    except IndexError:
        print("query failed")
print("Total songs found: ", len(spotify_song_list))

result = sp.user_playlist_create(
    user=user_id,
    name=f"{date.split('-')[0]} Top hits",
    public=False,
    description=f"Playlist of top songs for date {date}")

# pprint.pprint(result)

# -----------Creating a new playlist--------------------#
playlist_id = result['id']
# ---------------Adding data to playlist------------#
sp.user_playlist_add_tracks(
    user="kitkat", playlist_id=playlist_id, tracks=spotify_song_list)
