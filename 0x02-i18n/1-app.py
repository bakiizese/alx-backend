#!/usr/bin/env python3
'''  simple flask app '''
from flask import Flask, render_template
from flask_babel import Babel
from typing import Classvar


class Config:
    LANGUAGES: ClassVar[list[str]] = ["en", "fr"]
    BABEL_DEFAULT_LOCALE: ClassVar[str] = 'en'
    BABEL_DEFAULT_TIMEZONE: ClassVar[str] = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@app.route('/', strict_slashes=False)
def index() -> str:
    ''' route to / '''
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run(debug=1)
