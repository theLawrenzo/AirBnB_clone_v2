#!/usr/bin/python3
# This script contians a flask web application

'''Web application that run on all computer in the same network'''

from flask import Flask

app = Flask(__name__)

@app.route('/hbnb', strict_slashes=False)
def hbnb():
	return "HBNB"

if __name__ == "__main__":
	app.run(host="0.0.0.0", port=5000)
