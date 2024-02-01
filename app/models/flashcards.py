# import sqlalchemy database
from app import db

# Flashcard SQL Database Model
class Flashcard(db.Model):
    __tablename__ = 'flashcard'
    id = db.Column(db.Integer, primary_key=True) # flashcard id (primary key)
    setid = db.Column(db.Integer, db.ForeignKey('set.id')) # foreign key to the set
    front = db.Column(db.Text) # front text of the flashcard
    back = db.Column(db.Text) # back text of the flashcard


    def __repr__(self):
        return '<Flashcard: %r>' % self.id
