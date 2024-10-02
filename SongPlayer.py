import pygame
import os
from SongBase import SongBase
from SongDownloader import SongDownloader
from threading import Thread
import json
pygame.init()
pygame.mixer.init()

class SongPlayer:
    def __init__(self):
        self.volume = 0
        self.allSongs = [x for x in os.listdir(SongBase.mp3Folder) if x[-3:] == "mp3"]
        self.currentSong = 12
        self.maxSongs = len(self.allSongs)

        self.musicEnd = pygame.USEREVENT + 1
        self.PlaySongByFile(self.allSongs[self.currentSong])

        self.InputThread = Thread(target = self.GetInput)
        self.InputThread.start()

    def Run(self):
        while True:
            for event in pygame.event.get():
                if event.type == self.musicEnd:
                    self.currentSong += 1
                    if self.currentSong >= self.maxSongs:
                        self.currentSong = 0
                    self.PlaySongByFile(self.allSongs[self.currentSong])

    def GetInput(self):
        while True:
            com = input("> ")
            self.HandleInput(com.strip())

    def HandleInput(self, enteredString):
        match enteredString.lower():
            case "exit":
                
                quit()
            case "skip":
                self.currentSong += 1
                if self.currentSong >= self.maxSongs:
                    self.currentSong = 0
                self.PlaySongByFile(self.allSongs[self.currentSong])
            case "back":
                self.currentSong -= 1
                if self.currentSong < 0:
                    self.currentSong = self.maxSongs - 1
                self.PlaySongByFile(self.allSongs[self.currentSong])
            case "volume":
                self.volume = input("Current Volume: " + str(pygame.mixer.music.get_volume()) + "\nNew Volume: ")
                pygame.mixer.music.set_volume(float(self.volume))
            case "play":
                name = input("Song Name: ")
                artist = input("Song Artist: ")
                self.PlaySongByName(name, artist)
                self.currentSong = self.allSongs.index(SongPlayer.GetFile(name, artist))
            case "goto":
                i = int(input("Song Number: "))
                if i < 0:
                    i = 0
                if i >= self.maxSongs:
                    i = self.maxSongs - 1
                self.currentSong = i
                self.PlaySongByFile(self.allSongs[self.currentSong])
            case "pause":
                pygame.mixer.music.pause()
            case "unpause":
                pygame.mixer.music.unpause()
            case "download":
                url = input("URL: ")
                name = input("Song Name: ")
                artist = input("Song Artist: ")
                DownloadThread = Thread(target = self.DownloadSong, args = (url,name,artist))
                DownloadThread.start()
            case "playing":
                print(self.allSongs[self.currentSong][:-4])
                print(pygame.mixer.music.get_pos(), "/")

    def DownloadSong(self, url, name, artist):
        SongDownloader.DownloadSong(url, name, artist)

    def PlaySongByName(self, songName, songArtist):
        self.PlaySongByFile(SongPlayer.GetFile(songName, songArtist))

    def PlaySongByFile(self, songFile):
        pygame.mixer.stop()
        pygame.mixer.music.load(SongBase.mp3Folder + songFile)
        pygame.mixer.music.play()
        pygame.mixer.music.set_endevent(self.musicEnd)

    def GetFile(songName, songArtist):
        return  songArtist + " - " + songName + ".mp3"

    def UpdateData(self):
        userData = {
                    "volume" : self.volume,
                    "currentSong" : self.currentSong,
                    "currentPos" : pygame.mixer.music.get_pos()
                    }

player = SongPlayer()
player.Run()
