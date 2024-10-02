import json
import ffmpeg
import os
class SongBase:
    mp3Folder = "C:/Users/drake/AppData/Local/Programs/Python/Python311/Python Projects/SpotifyAtHome/AudioFiles/"
    dataFile = mp3Folder + "SongData.json"

songData = {}
for s in [x for x in os.listdir(SongBase.mp3Folder) if x[-3:] == "mp3"]:
    songData[s] = float(ffmpeg.probe(SongBase.mp3Folder + s)['format']['duration']) * 1000

print(songData)
with open(SongBase.dataFile, 'w') as f:
    json.dump(songData, f, ensure_ascii = False, indent = 4)
