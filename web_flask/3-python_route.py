#!/usr/bin/python3

'''
Starts a Flask web application listening on all host on
a network interface
'''

from flask import Flask

app = Flask(__name__)

@app.route('/python/<text>')
