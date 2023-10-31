'''
Blueprints for the website routes 
'''
from flask import Blueprint

views = Blueprint('views', __name__)

@views.route('/')
def index():
    '''
    A route for the page index
    '''
    return 'Welcome to my e-commerce'