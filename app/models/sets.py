from app import db

# Set Model
class Set(db.Model):
    __tablename__ = 'set'
    id = db.Column(db.Integer, primary_key=True)
    setname = db.Column(db.String(40), index=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    username = db.Column(db.String())
    topic = db.Column(db.String(40))
    subject = db.Column(db.String(40))
    flashcards = db.relationship('Flashcard', backref='set', lazy='dynamic') # one to many relationship set to flashcards
    ratingNo = db.Column(db.Float)

    def __repr__(self):
        return '<Set: %r>' % self.setname