from flask import Flask, jsonify
import RAnalysis.rAnalysis
from importFilesPackages import importData
from importFilesPackages import importRPackages

app = Flask(__name__)


@app.route('/')
def hello_world():
    return jsonify("Hello World")


if __name__ == '__main__':
    app.run()
