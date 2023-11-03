from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, TextAreaField, SubmitField, PasswordField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo

class LoginForm(FlaskForm):
    username: str = StringField('Username', validators=[DataRequired()])
    password: str = PasswordField('Password', validators=[DataRequired()])
    remember_me: bool = BooleanField('Remember me')
    submit = SubmitField()

class RegisterForm(FlaskForm):
    username: str = StringField()
    email: str = StringField()
    password: str = PasswordField('Password', validators=[DataRequired()])
    password2: str = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField()
