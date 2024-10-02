import pygame
import os
from SongBase import SongBase
from threading import Thread
import sys
pygame.init()
pygame.mixer.init()

class SongPlayer:
    def __init__(self):
        self.sound = None
        self.volume = 1.0
        self.allSongs = os.listdir(SongBase.mp3Folder)
        self.currentSong = 23
        self.maxSongs = len(self.allSongs)

        self.RunThread = Thread(target = self.Run)
        self.InputThread = Thread(target = self.GetInput)
        self.PlaySongByFile(self.allSongs[self.currentSong])

        self.changingSong = False

        self.RunThread.start()
        self.InputThread.start()
        

        self.InputThread.join()
        self.RunThread.join()
        

    def Run(self):
        while True:
            print("in run thread", flush=True)
            if not pygame.mixer.get_busy() and not self.changingSong:
                print("not busy")
                sys.stdout.flush()
                self.currentSong += 1
                self.PlaySongByFile(self.allSongs[self.currentSong])

    def GetInput(self):
        while True:
            com = input(">")
            #com = ''
            self.HandleInput(com)

    def HandleInput(self, enteredString):
        self.changingSong = True
        match enteredString.lower():
            case "exit":
                quit()
            case "skip":
                self.currentSong += 1
                self.PlaySongByFile(self.allSongs[self.currentSong])
            case "back":
                self.currentSong -= 1
                self.PlaySongByFile(self.allSongs[self.currentSong])
            case "volume":
                self.volume = input("Current Volume: " + str(pygame.mixer.Sound.get_volume(self.sound)) + "\nNew Volume: ")
                pygame.mixer.Sound.set_volume(self.sound, float(self.volume))
            case "play":
                name = input("Song Name: ")
                artist = input("Song Artist: ")
                self.PlaySongByName(name, artist)
            case "status":
                print(pygame.mixer.get_busy())
        self.changingSong = False

    def PlaySongByName(self, songName, songArtist):
        pygame.mixer.stop()
        self.sound = pygame.mixer.Sound(SongPlayer.GetFile(songName, songArtist))
        pygame.mixer.Sound.set_volume(self.sound, float(self.volume))
        self.sound.play()

    def PlaySongByFile(self, songFile):
        pygame.mixer.stop()
        self.sound = pygame.mixer.Sound(SongBase.mp3Folder + songFile)
        pygame.mixer.Sound.set_volume(self.sound, float(self.volume))
        self.sound.play()

    def GetFile(songName, songArtist):
        return SongBase.mp3Folder + songArtist + " - " + songName + ".mp3"

player = SongPlayer()
#player.Run()
