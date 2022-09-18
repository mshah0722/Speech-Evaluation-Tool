import importlib.util as ilu
from re import template
from werkzeug.utils import secure_filename
from flask import Flask, send_from_directory, flash, jsonify, request, redirect, url_for, render_template, make_response
import audio_to_text
import video_to_audio
import os
from doctest import REPORT_CDIFF
import requests
import time
from dotenv import load_dotenv
from flask_cors import CORS, cross_origin


app = Flask(__name__, template_folder=template)
app.config['UPLOAD_FOLDER'] = "./assets"


@app.route('/try')
def trial():
    return {"trial": "4", "5": "8"}


@app.route('/upload', methods=["POST"])
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
            return {"filename": filename}


@app.route('/<name>', methods=["GET"])
def download_file(name):
    return send_from_directory(app.config["UPLOAD_FOLDER"], name)


@app.route('/generate-report/<name>')
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
    

    return {'text': response.json()['text']}


if __name__ == '__main__':
    app.secret_key = os.urandom(24)
    app.run(debug=True, host="0.0.0.0")

CORS(app, expose_headers='Authorization')
