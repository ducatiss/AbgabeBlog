from app import db

class Blogeintrag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    datum = db.Column(db.Date, nullable=False)
    titel = db.Column(db.String, nullable=False)
    kategorie = db.Column(db.ForeignKey('kategorie.id'), nullable=False)
    text = db.Column(db.Text, nullable=False)

class Kategorie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String, nullable=False)
    blogeintrag = db.relationship('Blogeintrag', backref='Kategorie')