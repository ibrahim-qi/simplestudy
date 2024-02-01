from app import db

# Self Quiz Model
class SelfTest(db.Model):
    __tablename__ = 'selftest'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    setid = db.Column(db.Integer, db.ForeignKey('set.id'))
    rightCount = db.Column(db.Integer)
    wrongCount = db.Column(db.Integer)
    totalFlashcards = db.Column(db.Integer)
    flashcardsCompleted = db.Column(db.Integer)
    percentageScore = db.Column(db.Integer)
    frontNumber = db.Column(db.Integer)
    backNumber = db.Column(db.Integer)