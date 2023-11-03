from flask import Blueprint, render_template, url_for

views = Blueprint('views', __name__)

@views.route('/')
def index():
    return 'Welcome to my e-commerce'

@views.route('/home')
def home():
    return render_template('home.html')