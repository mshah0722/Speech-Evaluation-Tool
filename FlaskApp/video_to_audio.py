from moviepy.editor import *

<<<<<<< HEAD
def extractAudioFromMP4(mp4_path = "assets/test.mp4", wav_path = "audio/gen_audio.wav"):
=======

def extractAudioFromMP4(mp4_path, wav_path):
>>>>>>> ffe5624925465cd3388c0d2c3a45e62ba75bb3f7

    videoclip = VideoFileClip(mp4_path)
    audioclip = videoclip.audio
    audioclip.write_audiofile(wav_path)

    audioclip.close()
    videoclip.close()
<<<<<<< HEAD



=======
>>>>>>> ffe5624925465cd3388c0d2c3a45e62ba75bb3f7
