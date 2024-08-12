#!/usr/bin/python3
'''
Starts a Flask web application listening to connection
from all hosts on a network interface
'''

from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    '''Returns an html document page if n is integer'''
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
