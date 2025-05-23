from flask import Blueprint, render_template

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return render_template('index.html')  # This is the main page of the web application

@bp.route('/secret')
def secret():
    return '<h1 style="color:blue;">You found the secret page!</h1>'  # This is a secret page of the web application