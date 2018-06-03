from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    msg = "<h1>Hello World</h1>"
    return msg
