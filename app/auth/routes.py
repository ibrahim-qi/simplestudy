
# imports flask modules
from flask import Blueprint, render_template, redirect, url_for, flash

# import class forms created by WTForms
from app.forms import LoginForm, RegisterForm

# import user database model to use for querying and adding records
from app.models.users import User

# module used to encrypt and decrypt user passwords
from werkzeug.security import generate_password_hash, check_password_hash

# manages the auth system
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

# instantiation for the authentication system with Flask Blueprint
auth = Blueprint('auth', __name__)

# creates a /login route inside of the auth blueprint with GET and POST as HTTP methods to manage data
@auth.route('/login', methods=['GET', 'POST'])
def login():
  # instantiates the imported LoginForm object from forms.py within the route in order to create the form with FlaskForm
  form = LoginForm()
  # selection statement for when the user clicks submit button
  if form.validate_on_submit():
    # queries the username of the user that logged in and assigns it to the user variable
    user = User.query.filter_by(username=form.username.data).first()
    # checks if the username matches with the hashed password on the database
    if user:
      # checks the password hash using the check_password_hash object in the werkzug.security library
      if check_password_hash(user.password, form.password.data):
        # creates a session for the user using flask_login
        login_user(user)
        return redirect(url_for('main.index')) # redirects the user to the dashboard once they have logged in

    # if the inputted username and password do not match the queried results then it will display this message on the login page
    flash("Invalid Username or Password")
  return render_template('auth/login.html', form=form) # render_template is used to render the html template in the auth folder

# creates the logout route in the auth blueprint
@auth.route('/logout')
@login_required # allows it so the user will not be able to access this route unless they are logged in
def logout():
  logout_user() # quits the current session for the user
  return redirect(url_for('auth.login')) # redirects them back to the login page

@auth.route('/register', methods=['GET', 'POST'])
def register():
  # imports the SQL database from __init__..py
  from app import db
  form = RegisterForm()
  if form.validate_on_submit():
    # uses the generate_password_hash object from werkzeug.security to hash the inputted password and assigns it as a variable
    hashed_pass = generate_password_hash(form.password.data, method='sha256')

    # assigns the inputted username and the hashed password variable to the column variables in the User object
    new_user = User(username=form.username.data,
                    password=hashed_pass)
    db.session.add(new_user) # Creates a record with the data assigned to the new_user variable to the User table in the database
    db.session.commit()

    flash("Successfully registered")
    return redirect(url_for('auth.login')) # Redirects user to login page and displays success message

  return render_template('auth/register.html', form=form)