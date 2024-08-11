#!/usr/bin/python3
'''Flask web application that is list can be accessed from
any location
'''

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    '''Returns a string HBNB to the client'''
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    '''Returns a string HBNB to the client'''
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    '''Returns a dynamic string object to the client'''
    return 'C {}'.format(text.replace('_', ' '))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
