import flask
import requests
import utils.Score as scores
import os

app = flask.Flask(__name__)

@app.route('/',methods = ['GET'])
def home():
    return {
        'what': "Hello"
    }

@app.route('/api', methods=['POST'])
def score():
    data = flask.request.get_json()
    message = data['message']
    if message is not None or message != '':
        score = scores.get_scores(message)
    else:
        score = 0
    return {
        'score': score
    }


if __name__ == '__main__':
    app.run(host="localhost", port=5000, debug=True)