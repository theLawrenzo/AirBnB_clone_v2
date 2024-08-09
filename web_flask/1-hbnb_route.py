#!/usr/bin/python3
'''Web application that run on all computer in the same network'''

from flask import Flask

app = Flask(__name__)

@app.route('/hbnb', strict_slashes=False)
def hbnb():
	'''Returns a string object'''
	return "HBNB"

if __name__ == "__main__":
	app.run(host="0.0.0.0", port=5000)
