from app import db

# Multiple Choice Question Model
class Question(db.Model):
    __tablename__ = 'question'
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    testID = db.Column(db.Integer, db.ForeignKey('multiplechoicetest.id'))
    flashcardid = db.Column(db.Integer, db.ForeignKey('flashcard.id'), nullable=False)
    question = db.Column(db.Text)
    answer = db.Column(db.Text)
    options = db.relationship('Option', backref='question') # one to many relationship - question to options
    user_choice = db.Column(db.Text)
    choices = db.relationship('Choice', backref='question') # one to many relationship - question to choices

# Option Model - Stores options that will be displayed in each question (randomised choices)
class Option(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question_id = db.Column(db.Integer, db.ForeignKey('question.id'))
    name = db.Column(db.Text)

# Choice Model - Choices that will be displayed in each question including the answer
class Choice(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question_id = db.Column(db.Integer, db.ForeignKey('question.id'))
    name = db.Column(db.Text)


