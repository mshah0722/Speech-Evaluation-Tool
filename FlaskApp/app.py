from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return '<form method = "post" action = "/video" ><input type = "file" id = "myFile" name = "filename" ><input type = "submit" ></ >'
