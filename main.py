import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import os
from dotenv import load_dotenv
import eyed3
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext


load_dotenv()
os.system("spotdl --download-ffmpeg")

clientId = os.getenv("CLIENTID")
clientSecret = os.getenv("CLIENTSECRET")
TOKEN = os.getenv("BOT_TOKEN")

clientCredentialsManager = SpotifyClientCredentials(client_id=clientId, client_secret=clientSecret)
sp = spotipy.Spotify(client_credentials_manager=clientCredentialsManager)


def findTrackId(trackTitle):
    results = sp.search(q=trackTitle, type='track', limit=1)

    if results['tracks']['items']:
        track_id = results['tracks']['items'][0]['id']
        return track_id
    else:
        return None
    
def downloadSong(trackId):
    url = f"spotdl https://open.spotify.com/intl-fr/track/{trackId}"
    os.system(url)

def rename():
    for file in os.listdir():
        if  file.endswith(".mp3"):

            mp3 = eyed3.load(file)
            os.rename(file, f"{mp3.tag.title}.mp3" )

def start(update: Update, context: CallbackContext):
    update.message.reply_text("🎵 Welcome to Spotdown bot! 🎶\n\nSend me the name of a song or the URL of a Tikok video, and I'll provide you with a download link for the music.")

def getSong(update: Update, context: CallbackContext):
    trackId = findTrackId(update.message.text)

    downloadSong(trackId)
    rename()

    for file in os.listdir():
        if  file.endswith(".mp3"):
            chat_id = update.message.chat_id
            context.bot.send_audio(chat_id=chat_id, audio=open(file, 'rb'))

            os.remove(file)

def main():
    updater = Updater(TOKEN, use_context=True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, getSong))

    updater.start_polling()
    updater.idle()

for file in os.listdir():
    if  file.endswith(".mp3"):
        print(file)

if __name__ == '__main__':
    main()
