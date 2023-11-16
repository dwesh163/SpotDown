import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import os
from dotenv import load_dotenv

load_dotenv()

clientId = os.getenv("CLIENTID")
clientSecret = os.getenv("CLIENTSECRET")

clientCredentialsManager = SpotifyClientCredentials(client_id=clientId, client_secret=clientSecret)
sp = spotipy.Spotify(client_credentials_manager=clientCredentialsManager)


def findTrackId(trackTitle):
    results = sp.search(q=trackTitle, type='track', limit=1)

    if results['tracks']['items']:
        track_id = results['tracks']['items'][0]['id']
        return track_id
    else:
        return None
    

trackTitle = input("Enter a track title : ")
trackId = findTrackId(trackTitle)
print(trackId)