from app import db

class Company(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    exchange = db.Column(db.String(8), index=True, unique=False)
    symbol = db.Column(db.String(6), index=True, unique=True)
    name = db.Column(db.String(100), index=True, unique=False)
    historical_data = db.relationship('Day', backref='company', lazy='dynamic')

    def __repr__(self):
        return '<Company %r>' % (self.symbol)

class Day(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date)
    open = db.Column(db.Float(asdecimal=True))
    close = db.Column(db.Float(asdecimal=True))
    high = db.Column(db.Float(asdecimal=True))
    low = db.Column(db.Float(asdecimal=True))
    volume = db.Column(db.Float(asdecimal=True))
    company_id = db.Column(db.Integer, db.ForeignKey('company.id'))

    def __repr__(self):
        return '<%r, %r, %r, %r>' % (self.id, self.date, self.open, self.close)

class CurrentDay(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_time = db.Column(db.DateTime)
    open = db.Column(db.Float(asdecimal=True))
    last = db.Column(db.Float(asdecimal=True))
    high = db.Column(db.Float(asdecimal=True))
    low = db.Column(db.Float(asdecimal=True))
    volume = db.Column(db.Float(asdecimal=True))
    company_id = db.Column(db.Integer, db.ForeignKey('company.id'))

    def __repr__(self):
        return '<Close %r>' % (self.date_time)