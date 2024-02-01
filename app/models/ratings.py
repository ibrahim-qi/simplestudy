from app import db

# Rating Model
class Rating(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    setid = db.Column(db.Integer, db.ForeignKey('set.id'))
    ratingNo = db.Column(db.Integer)
    hasRated = db.Column(db.Boolean)
