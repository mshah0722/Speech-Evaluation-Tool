import moviepy.editor as mp


def extractAudioFromMP4(filename):
    videoFolder = "./video/"
    my_clip = mp.VideoFileClip(videoFolder+filename)
    audio_path = "audio/" + filename[:-4] + ".mp3"
    my_clip.audio.write_audiofile(audio_path)


# def test():
#     extractAudioFromMP4("./video/test.mp4")

# test()
