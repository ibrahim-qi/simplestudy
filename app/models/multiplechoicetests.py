from app import db

# Multiple Choice Quiz Model
class MultipleChoiceTest(db.Model):
    __tablename__ = 'multiplechoicetest'
    id = db.Column(db.Integer, primary_key=True)
    setid = db.Column(db.Integer, db.ForeignKey('set.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    score = db.Column(db.Integer)
    questions = db.relationship('Question', backref='multiplechoicetest', lazy='dynamic') # one to many relationship = quiz to questions
    questionNumber = db.Column(db.Integer)
