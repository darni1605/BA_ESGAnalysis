from flask import Flask, jsonify
from RAnalysis import rAnalysis

app = Flask(__name__)


@app.route('/')
def hello_world():
    return jsonify("Hello World")


if __name__ == '__main__':
    app.run()
