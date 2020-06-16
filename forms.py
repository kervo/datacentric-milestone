from flask_wtf import FlaskForm
from wtforms import BooleanField, PasswordField, StringField, SubmitField, validators
from wtforms.validators import DataRequired, EqualTo, Length

class signUpForm(FlaskForm):
    name_first = StringField('User Name', [validators.DataRequired()])
    email = StringField('Email Address', [validators.DataRequired(), validators.Email(), validators.Length(min=6, max=35)])
    password = PasswordField('New Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')
    submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')