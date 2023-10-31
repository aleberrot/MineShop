'''
This module is for creating the authentication routes for the website
'''

from flask import Blueprint

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return 'Login'

@auth.route('/register')
def register():
    return 'Register'

@auth.route('logout')
def logout():
    return 'You have been logged out'