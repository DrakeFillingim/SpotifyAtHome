import ffmpeg
import os

def ExtractAudio(input_vid, output_mpf):
    with open(input_vid) as f:
        print(f)
    try:
        inp = ffmpeg.input(input_vid)
        outp = inp.output(output_mpf)
        run = outp.run(capture_stdout=True, capture_stderr=True)
    except ffmpeg.Error as e:
        print(e)

ExtractAudio(
    "RNPD9722.mp4",
    "output_audio.mp3"
    )
