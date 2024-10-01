import os
import ffmpeg
import yt_dlp

#file name convention

class SongDownloader:
    mp3Folder = "AudioFiles/"
    defaultOptions = {
        "quiet" : True,
        "getthumbnail" : True,
        "noprogress" : True
        }

    def DownloadSong(songURL, songName, songArtist, downloadOptions):
        with yt_dlp.YoutubeDL(downloadOptions) as ytdl:
            info = ytdl.extract_info(songURL)
            fileName = info["title"] + " [" + info["id"] + "]." + info["ext"]
            targetName = SongDownloader.mp3Folder + songArtist + " - " + songName + ".mp3"
            SongDownloader.ExtractAudio(fileName, targetName)

            #save thumbnail?
            #response = requests.get(info["thumbnail"])
            #img = Image.open(BytesIO(response.content))
            #img.save("test.png")

    def ExtractAudio(input_file, output_mp3):
        ffmpeg.input(input_file).output(output_mp3).run()
        os.remove(input_file)
