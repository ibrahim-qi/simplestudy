from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_pagedown import PageDown

app = Flask(__name__) # Initiates Flask App
app.config['SECRET_KEY'] = 'flashcardapp'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///NEA.sqlite3'

db = SQLAlchemy(app) # Initiates SQLAlchemy Database
Bootstrap(app) # Initiates Flask Bootstrap into app
pagedown = PageDown(app)

login_manager = LoginManager(app) # Initiates Flask Login
login_manager.init_app(app)
login_manager.login_view = 'auth.login' # Links it to the auth blueprint

# Assigns user id to current user that is logged in
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

from app.auth.routes import auth
app.register_blueprint(auth) # Registers the auth blueprint

from app.main.routes import main
app.register_blueprint(main) # Registers the main blueprint

# Import all database models
from app.models.users import User
from app.models.sets import Set
from app.models.flashcards import Flashcard
from app.models.selftests import SelfTest
from app.models.ratings import Rating
from app.models.multiplechoicetests import MultipleChoiceTest
from app.models.multiplechoicequestions import Question, Option, Choice
from app.models.ratings import Rating
db.create_all() # Creates all database tables of models

# Runs the flask app
if __name__ == '__main__':
    app.run(debug=True)