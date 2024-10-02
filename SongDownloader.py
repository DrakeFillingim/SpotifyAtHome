import os
import ffmpeg
import yt_dlp
import json
from SongBase import SongBase

#file name convention

class SongDownloader:
    defaultOptions = {
        "quiet" : True,
        "getthumbnail" : True,
        "noprogress" : True,
        "noplaylist" : True
        }

    def DownloadSong(songURL, songName, songArtist, downloadOptions = None):
        targetName = SongBase.mp3Folder + songArtist + " - " + songName + ".mp3"
        if os.path.isfile(targetName):
            return

        if downloadOptions is None:
            downloadOptions = SongDownloader.defaultOptions
        
        with yt_dlp.YoutubeDL(downloadOptions) as ytdl:
            info = ytdl.extract_info(songURL)
            fileName = info["title"] + " [" + info["id"] + "]." + info["ext"]
            SongDownloader.ExtractAudio(fileName, targetName)

            #save thumbnail?
            #response = requests.get(info["thumbnail"])
            #img = Image.open(BytesIO(response.content))
            #img.save("test.png")

    def ExtractAudio(input_file, output_mp3):
        ffmpeg.input(input_file).output(output_mp3).run()
        os.remove(input_file)
