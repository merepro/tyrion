from flask import Flask, render_template, g, session, url_for, redirect, request
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.admin import Admin

from time import strftime

app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html', error=error), 404


#Loading user modules
#from app.users.views import mod as usersModules
#app.register_blueprint(usersModules)

@app.before_request
def before_request():
    """
    pull user's profile from the database before every request are treated
    """
    g.user = None
    if 'user_id' in session:
        g.user = User.query.get(session['user_id'])

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/resume')
def resume():
    return render_template('resume.html')
