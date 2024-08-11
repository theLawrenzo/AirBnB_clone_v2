#!/usr/bin/python3
'''
Flask web appplication listening to connection from
all host on a network interface
'''

from flask import Flask

app = Flask(__name__)


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    '''Return a string and an integer'''
    return '{} is a number'.format(n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
