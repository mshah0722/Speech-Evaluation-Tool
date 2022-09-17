import moviepy.editor as mp

def extractAudioFromMP4(_path):
    my_clip = mp.VideoFileClip(_path)
    audio_path = "audio/" + _path.split('/')[-1][:-4] + ".mp3"
    my_clip.audio.write_audiofile(audio_path)
    
def test():
    extractAudioFromMP4("./video/test.mp4")

test()

