from moviepy.editor import *


def extractAudioFromMP4(mp4_path, wav_path):

    videoclip = VideoFileClip(mp4_path)
    audioclip = videoclip.audio
    audioclip.write_audiofile(wav_path)

    audioclip.close()
    videoclip.close()
