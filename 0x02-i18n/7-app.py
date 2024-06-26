#!/usr/bin/env python3
'''  simple flask app '''
from flask import Flask, g, session, render_template, request
from flask_babel import Babel
from typing import Dict
from pytz import timezone
import pytz.exceptions


class Config:
    ''' class '''
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user(find_id) -> Dict:
    ''' get user from users '''
    if find_id:
        try:
            find_id = int(find_id)
        except Exception:
            return None
        if find_id in users:
            return users[find_id]
    return None


@app.before_request
def before_request():
    ''' run before all funcs '''
    login_id = request.args.get('login_as')
    if login_id:
        us = get_user(login_id)
        if us:
            g.user = us


@babel.localeselector
def get_locale():
    ''' get locale '''
    locale = request.args.get('locale')
    hlocale = request.headers.get('Accept-Language')
    if locale and locale in Config.LANGUAGES:
        return locale
    elif hasattr(g, 'user'):
        if g.user['locale'] and g.user['locale'] in Config.LANGUAGES:
            return g.user['locale']
    elif hlocale:
        return hlocale
    return request.accept_languages.best_match(app.config['LANGUAGES'])



@babel.timezone_selector
def get_timezone():
    ''' timezone selector '''
    tzone = request.args.get('timezone', None)
    if tzone:
        try:
            tzone = timezone(tzone)
        except pytz.exceptions.UnknownTimeZoneError:
            pass
    elif g.user:
        try:
            tzone = g.user.get('timezone')
            tzone = timezone(tzone)
        except pytz.exceptions.UnknownTimeZoneError:
            pass
    return tzone


@app.route('/', strict_slashes=False)
def index() -> str:
    ''' route to / '''
    user_name = None
    if hasattr(g, 'user'):
        user_name = g.user['name']
    return render_template('6-index.html', user_name=user_name)


if __name__ == '__main__':
    app.run(debug=1)

