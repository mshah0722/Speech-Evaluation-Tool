import importlib.util as ilu
from werkzeug.utils import secure_filename
from flask import Flask, flash, request, redirect, url_for, render_template
import audio_to_text
import video_to_audio
import os
from doctest import REPORT_CDIFF
import requests
import time
from dotenv import load_dotenv


app = Flask(__name__, template_folder='template')
app.config['UPLOAD_FOLDER'] = "./video"


@app.route('/', methods=['GET'])
def homepage():
    return render_template('index.html')


@app.route('/', methods=["POST"])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file:
            filename = file.filename
            print(filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('display_video', name=filename))


@app.route('/<name>')
def display_video(name):

    def configure():
        load_dotenv()
    configure()
    video_to_audio.extractAudioFromMP4(name)
    # text = audio_to_text.audio_to_text(name)
    filename = name
    filepath = "./audio/"+filename[:-4]+".mp3"
    print(filepath)
    # authorization
    headers = {
        "authorization": os.getenv('assembly_api_key'),
        "content-type": "application/json"
    }

    def read_file(filename, chunk_size=5242880):
        with open(filename, 'rb') as _file:
            while True:
                data = _file.read(chunk_size)
                if not data:
                    break
                yield data

    response = requests.post('https://api.assemblyai.com/v2/upload',
                             headers=headers,
                             data=read_file(filepath))

    audio_url = response.json()['upload_url']

    # post transcription request
    postEndpoint = "https://api.assemblyai.com/v2/transcript"
    json = {
        "audio_url": audio_url
    }
    response = requests.post(postEndpoint, json=json, headers=headers)

    # store transcription id
    id = response.json()['id']
    print(id)

    # get transcription using id
    getEndpoint = "https://api.assemblyai.com/v2/transcript/"+id

    response = requests.get(getEndpoint, headers=headers)
    while not response.json()['status'] == "completed":
        response = requests.get(getEndpoint, headers=headers)
        print(response.json()['status'])
        time.sleep(1)

    print(response.json()['text'])

    return response.json()['text']


if __name__ == '__main__':
    app.run(debug=True)
