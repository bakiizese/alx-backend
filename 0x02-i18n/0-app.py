#!/usr/bin/env python3
'''  simple flask app '''
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def index():
    ''' route to / '''
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='localhost', port=5001)
