import os
import yt_dlp
from SongDownloader import SongDownloader
from SongPlayer import SongPlayer

class SpotifyRunner:
    def __init__(self):
        self.allSongs = os.listdir("C:/Users/drake/AppData/Local/Programs/Python/Python311/Python Projects/SpotifyAtHome/AudioFiles")
        self.currentSong = 0
        self.maxSongs = len(self.allSongs)
        self.queue = []
    
    def Run(self):
        while True:
            com = input(">")
            self.HandleInput(com)

    def HandleInput(self, enteredString):
        match enteredString.lower():
            case "exit":
                os.exit()
            case "skip":
                self.currentSong += 1
                SongPlayer.PlaySong(

runner = SpotifyRunner()
runner.Run()
