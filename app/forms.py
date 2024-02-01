from flask import redirect, url_for, flash
from flask_wtf import FlaskForm
from flask_sqlalchemy import SQLAlchemy
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from flask_pagedown.fields import PageDownField
from wtforms.validators import InputRequired, Length, DataRequired, ValidationError
from app.models.users import User

# Login Form
class LoginForm(FlaskForm):
  username = StringField('Username', validators=[InputRequired(), Length(min=4, max=20)])
  password = PasswordField('Password', validators=[InputRequired(), Length(min=8, max=80)])
  submit = SubmitField('Submit')

# Register Form
class RegisterForm(FlaskForm):
  username = StringField('Username', validators=[InputRequired(), Length(min=4, max=15)])
  password = PasswordField('Password', validators=[InputRequired(), Length(min=8, max=80)])
  submit = SubmitField('Submit')

  # Username Validator - Checks whether username already exists in the database
  def validate_username(self, username):
    user = User.query.filter_by(username=username.data).first()
    if user:
      raise ValidationError("Username already exists")

# Create Set Form
class SetForm(FlaskForm):
  setname = StringField('Set Name', validators=[DataRequired(), Length(max=40)])
  topic = StringField('Topic', validators=[DataRequired()])
  subject = StringField('Subject', validators=[DataRequired()])

# Create Flashcard Form
class FlashcardForm(FlaskForm):
# Contains Page Down Fields
  front = PageDownField('Front', validators=[DataRequired()])
  back = PageDownField('Back', validators=[DataRequired()])
  next = BooleanField('Add another flashcard?')
  submit = SubmitField('Add')

# Edit Flashcard Form
class EditFlashcardForm(FlaskForm):
  front = PageDownField('Front', validators=[DataRequired()])
  back = PageDownField('Back', validators=[DataRequired()])
  submit = SubmitField('Update')



