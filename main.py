import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import os
from dotenv import load_dotenv

clientId = os.getenv("CLIENTID")
clientSecret = os.getenv("CLIENTSECRET")

clientCredentialsManager = SpotifyClientCredentials(client_id='', client_secret='')
sp = spotipy.Spotify(client_credentials_manager=clientCredentialsManager)