from moviepy.editor import *

def extractAudioFromMP4(mp4_path = "assets/test.mp4", wav_path = "audio/gen_audio.wav"):

    videoclip = VideoFileClip(mp4_path)
    audioclip = videoclip.audio
    audioclip.write_audiofile(wav_path)

    audioclip.close()
    videoclip.close()

extractAudioFromMP4()


