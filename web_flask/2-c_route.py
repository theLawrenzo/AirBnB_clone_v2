#!/usr/bin/python3
'''Flask web application that is list can be accessed from
any location
'''

from flask import Flask

app = Flask(__name__)

@app.route('/c/<text>', strict_slashes=False)
def c(text):
	'''Returns a dynamic string object'''
	return 'C {}'.format(text)

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000, debug=True)
