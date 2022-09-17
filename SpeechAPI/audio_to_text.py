from doctest import REPORT_CDIFF
import requests
import time

# post transcription request
postEndpoint = "https://api.assemblyai.com/v2/transcript"
json = {
    "audio_url": "https://bit.ly/3yxKEIY"
}
headers = {
    "authorization": "4c1fcafbf469465299912b663672b5c2",
    "content-type": "application/json"
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