#!/usr/bin/python3
'''A flask web application that runs on all available network
interface on machine it is run on
'''

from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def index():
    '''Function that displays the home page'''
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
