from os import urandom, getenv

from flask import Flask, render_template, request, session, url_for, g

from model import init_db, SessionWrapper
from user_ops import UserOps
from errors import InvalidCredentialsError, UserExistsError

BASEURL = getenv('BASEURL', '')
init_db()
app = Flask(__name__)
app.secret_key = urandom(32)
app.jinja_env.globals.update(  # pylint: disable=no-member
    get_url=lambda endpoint: f'{BASEURL}{url_for(endpoint)}'
)


@app.before_request
def setup_db():
    # pylint: disable=protected-access
    g._db_session_wrapper = SessionWrapper()
    g.db_session = g._db_session_wrapper.session


@app.teardown_appcontext
def close_db_session(_):
    # pylint: disable=protected-access
    g._db_session_wrapper.teardown()


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            with g.db_session() as db_session:
                UserOps(
                    request.form.get('username'),
                    request.form.get('password'),
                    db_session
                ).authenticate()
        except InvalidCredentialsError:
            return render_template('login.html', alert='Invalid credentials!')

        session['logged_in'] = True
        session['username'] = request.form['username']
        return render_template('internal.html')

    if session.get('logged_in'):
        return render_template('internal.html')
    return render_template('login.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        form_filled_out = all([
            request.form.get('username'),
            request.form.get('password'),
            request.form.get('passwordconfirm')
        ])

        if not form_filled_out:
            return render_template('register.html', alert='You need to fill everything.')
        if request.form['password'] != request.form['passwordconfirm']:
            return render_template('register.html', alert='Passwords do not match! Please try again.')

        try:
            with g.db_session() as db_session:
                UserOps(
                    request.form.get('username'),
                    request.form.get('password'),
                    db_session
                ).register()
        except UserExistsError:
            return render_template('register.html', alert='Username already in use.')

        return render_template(
            'login.html',
            success=(
                'Account "{}" successfully registered. '
                'You can log in now!'.format(request.form['username'])
            )
        )

    return render_template('register.html')


@app.route('/logout')
def logout():
    try:
        session.pop('logged_in')
        session.pop('username')
    except KeyError:
        pass
    return render_template('login.html')


@app.errorhandler(401)
@app.errorhandler(404)
@app.route('/error')
def error(err): # pylint: disable=unused-argument
    return render_template('error.html', error=err), err.code


# 500 needs a separate handler, as Flask would print
# the actual piece of code that caused the exception
# for some bizarre reason
@app.errorhandler(500)
@app.route('/error')
def servererror(err): # pylint: disable=unused-argument
    return render_template('error.html', error='500: Internal server error'), 500


if __name__ == '__main__':
    app.run(host='127.0.0.1', debug=False, port=11111)
