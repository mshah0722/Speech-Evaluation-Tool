from doctest import REPORT_CDIFF
import requests
import time
from get_assembly_key import get_assembly_key

# authorization
headers = {
    "authorization": get_assembly_key(),
    "content-type": "application/json"
}

# upload local file to assembly
filename = "audio/test.mp3"


def read_file(filename, chunk_size=5242880):
    with open(filename, 'rb') as _file:
        while True:
            data = _file.read(chunk_size)
            if not data:
                break
            yield data


response = requests.post('https://api.assemblyai.com/v2/upload',
                         headers=headers,
                         data=read_file(filename))

audio_url = response.json()['upload_url']

# post transcription request
postEndpoint = "https://api.assemblyai.com/v2/transcript"
json = {
    "audio_url": audio_url
}
response = requests.post(postEndpoint, json=json, headers=headers)

# store transcription id
id = response.json()['id']

# get transcription using id
getEndpoint = "https://api.assemblyai.com/v2/transcript/"+id

response = requests.get(getEndpoint, headers=headers)
while not response.json()['status'] == "completed":
    response = requests.get(getEndpoint, headers=headers)
    print(response.json()['status'])
    time.sleep(1)

print(response.json()['text'])
