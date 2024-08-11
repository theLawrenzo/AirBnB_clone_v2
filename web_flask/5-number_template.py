#!/usr/bin/python3
'''
This module contains functios that starts a flask web
Application and maps url to approciate page
'''

from flask import Flask

app = Flask(__name__)


@app.route('/number_template/<n>')
def number_template(n):
    '''Returns an html page to the client'''
    return ''
