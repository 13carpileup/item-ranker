#app.register_blueprint(account_api)
#app.register_blueprint(sus)

from flask import Flask, redirect, render_template, request
from flask import request
from flask_login import LoginManager
from flask import session
from flask import url_for
from photoManager import photo

login_manager = LoginManager()


from flask import session

# Set the secret key to some random bytes. Keep this really secret!

def create_app():
    app = Flask(__name__)
    app.secret_key = "secret key"
    login_manager.init_app(app)
    login_manager.login_view = 'login'
    return app

app=create_app()
app.register_blueprint(photo, url_prefix="/photo", methods=['GET', 'POST'])
@app.route('/')
def index():
    if 'username' in session:
        return f'Logged in as {session["username"]}'
    return 'You are not logged in'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        session['count'] = 0
        session['1']=0
        session['2']=0
        return redirect(url_for('index'))
    return '''
        <form method="post">
            <p><input type=text name=username>
            <p><input type=submit value=Login>
        </form>
    '''

@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('index'))