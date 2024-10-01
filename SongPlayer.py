import pygame
from SongBase import SongBase
pygame.init()
pygame.mixer.init()

class SongPlayer:
    sound = None

    def PlaySong(songName, songArtist):
        sound = pygame.mixer.Sound(SongPlayer.GetFile(songName, songArtist))
        sound.play()
        while pygame.mixer.get_busy():
            pass

    def GetFile(songName, songArtist):
        return SongBase.mp3Folder + songArtist + " - " + songName + ".mp3"
