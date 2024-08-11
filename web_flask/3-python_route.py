#!/usr/bin/python3
'''
Starts a Flask web application listening on all host on
a network interface
'''

from flask import Flask

app = Flask(__name__)


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text='is cool'):
    '''Returns a string to the client'''
    return 'Pyhton {}'.format(text.replace('_', ' '))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
