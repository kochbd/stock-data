from app import db

class Company(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    exchange = db.Column(db.String(8), index=True, unique=False)
    symbol = db.Column(db.String(6), index=True, unique=True)
    name = db.Column(db.String(100), index=True, unique=False)

    def __repr__(self):
        return '<Company %r>' % (self.symbol)
