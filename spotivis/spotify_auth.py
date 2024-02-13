import os
from spotipy import Spotify
from spotipy.oauth2 import SpotifyOAuth

def create_spotify_client():
    # Load the Client ID and Client Secret from environment variables
    client_id = os.getenv('SPOTIPY_CLIENT_ID')
    client_secret = os.getenv('SPOTIPY_CLIENT_SECRET')
    redirect_uri = "http://localhost:8888/callback"
    scope = "user-library-read user-top-read playlist-read-private"

    # Authenticate and create a Spotify client
    auth_manager = SpotifyOAuth(client_id=client_id,
                                client_secret=client_secret,
                                redirect_uri=redirect_uri,
                                scope=scope)
    spotify_client = Spotify(auth_manager=auth_manager)
    return spotify_client
