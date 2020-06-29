from flask_wtf import FlaskForm
from wtforms import BooleanField, PasswordField, TextAreaField, StringField, SubmitField, validators, IntegerField
from wtforms.validators import DataRequired, EqualTo, Length

class RegistrationForm(FlaskForm):
    username = StringField('Username', [validators.Length(min=4, max=25)])
    email = StringField('Email Address', [validators.Length(min=6, max=35)])
    password = PasswordField('New Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')
    accept_tos = BooleanField('I accept the TOS', [validators.DataRequired()])

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class Add_RecipeForm(FlaskForm):
    recipe_name = StringField('Recipe Name', validators=[DataRequired()])
    ingredients = StringField('List of ingredients', validators=[DataRequired()])
    preparation = TextAreaField('Ingredients', validators=[DataRequired()])
    country = StringField('Country')
    allergens = IntegerField('Allergens')
    submit = SubmitField('New Recipe')

class DeleteRecipe(FlaskForm):
    key = StringField('Name')
    title = StringField('Recipe Title')
    delete = SubmitField('Delete')

'''   '''


class CreateTask(FlaskForm):
    title = TextAreaField('Task Title')
    shortdesc = TextAreaField('Short Description')
    priority = IntegerField('Priority')
    create = SubmitField('Create')

class DeleteTask(FlaskForm):
    key = TextAreaField('Task ID')
    title = TextAreaField('Task Title')
    delete = SubmitField('Delete')

class UpdateTask(FlaskForm):
    key = TextAreaField('Task Key')
    shortdesc = TextAreaField('Short Description')
    update = SubmitField('Update')

class ResetTask(FlaskForm):
    reset = SubmitField('Reset')