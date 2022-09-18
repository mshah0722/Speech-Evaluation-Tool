import moviepy.editor as mp


def extractAudioFromMP4(videoFolder, filename):
    print(videoFolder+filename)
    my_clip = mp.VideoFileClip(videoFolder+filename)
    audio_path = videoFolder + filename[:-4] + ".mp3"
    my_clip.audio.write_audiofile(audio_path)
