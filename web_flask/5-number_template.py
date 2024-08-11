#!/usr/bin/python3
'''
This module contains functios that starts a flask web
Application and maps url to approciate page
'''

from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    '''Returns an html page to the client'''
    return render_template('5-number_template.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
