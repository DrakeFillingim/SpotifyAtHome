import pygame
pygame.init()
pygame.mixer.init()

class SongPlayer:
    sound = None
    mp3Folder = "AudioFiles/"

    def PlaySong(songName, songArtist):
        sound = pygame.mixer.Sound(SongPlayer.GetFile(songName, songArtist))
        sound.play()
        while pygame.mixer.get_busy():
            pass

    def GetFile(songName, songArtist):
        return SongPlayer.mp3Folder + songArtist + " - " + songName + ".mp3"
