
# Keep this file private or use environment variables in production

CLIENT_ID = "YOUR_CLIENT_ID_HERE"          # ← replace this
CLIENT_SECRET = "YOUR_CLIENT_SECRET_HERE"  # ← replace this
REDIRECT_URI = "http://127.0.0.1:5000"     # keep exactly this

import spotipy
from spotipy.oauth2 import SpotifyOAuth

def create_spotify():
    return spotipy.Spotify(auth_manager=SpotifyOAuth(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        redirect_uri=REDIRECT_URI,
        scope="user-top-read user-read-recently-played",
        cache_path=".cache"   # saves your login token locally
    ))
