from flask import Blueprint, render_template, url_for
from .forms import LoginForm, RegisterForm

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    form: LoginForm = LoginForm()
    return render_template('login.html', form=form)

@auth.route('/register', methods=['GET', 'POST'])
def register():
    form: RegisterForm = RegisterForm()
    return render_template('register.html', form=form)

@auth.route('logout')
def logout():
    return 'You have been logged out'