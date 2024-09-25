import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

date = input("what year you would like to travel to in YYY-MM-DD format: ")

base_url = "https://www.billboard.com/charts/hot-100/"
url = base_url + date

response = requests.get(url).text

soup = BeautifulSoup(response, "html.parser")

name_of_song_html = soup.select("li ul li h3")
name_of_song_text = [song.text.strip() for song in name_of_song_html]


sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id= "7b6fbe9ffad046bf8cafdbed32797b9f",
        client_secret="b2fc889a470448d988f043aae7d648d3",
        show_dialog=True,
        cache_path="token.txt",
        username="Joseph", 
    )
)

user_id = sp.current_user()["id"]


song_names = name_of_song_text

song_uris = []
year = date.split("-")[0]
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")


#Creating a new private playlist in Spotify
playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)

#Adding songs found into the new playlist
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
