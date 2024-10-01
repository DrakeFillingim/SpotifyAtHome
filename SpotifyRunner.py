from SongDownloader import SongDownloader
from SongPlayer import SongPlayer

SongDownloader.DownloadSong("https://www.youtube.com/watch?v=X_5D1t8Qkus",
                                "HOT TO GO!",
                                "Chappell Roan",
                                SongDownloader.defaultOptions)
SongPlayer.PlaySong("HOT TO GO!", "Chappell Roan")
