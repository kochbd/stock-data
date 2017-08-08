from app import db
import datetime

def _get_date():
    return datetime.datetime.now()

class Company(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    exchange = db.Column(db.String(8), index=True, unique=False)
    symbol = db.Column(db.String(6), index=True, unique=True)
    name = db.Column(db.String(100), index=True, unique=False)
    historical_data = db.relationship('Day', backref='company', lazy='dynamic')
    today = db.relationship('CurrentDay', backref='company', lazy='dynamic')
    #earnings = db.relationship('Earnings', backref='company', lazy='dynamic')

    def __repr__(self):
        return '<Company %r>' % (self.symbol)

class Day(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date)
    open = db.Column(db.Float(asdecimal=True))
    close = db.Column(db.Float(asdecimal=True))
    high = db.Column(db.Float(asdecimal=True))
    low = db.Column(db.Float(asdecimal=True))
    volume = db.Column(db.Integer)
    company_id = db.Column(db.Integer, db.ForeignKey('company.id'))

    def __repr__(self):
        return '<%r, %r, %r, %r>' % (self.id, self.date, self.open, self.close)

class CurrentDay(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, default=_get_date)
    time = db.Column(db.Time)
    price = db.Column(db.Float(asdecimal=True))
    volume = db.Column(db.Integer)
    company_id = db.Column(db.Integer, db.ForeignKey('company.id'))

    def __repr__(self):
        return '<Close %r>' % (self.date_time)



class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(15), index=True, unique=True)
    portfolio_value = db.Column(db.Float, index=True, unique=True)
    available_funds = db.Column(db.Float, index=True, unique=False)
    orders = db.relationship('Order', backref='buyer', lazy='dynamic')
    watching = db.relationship('WatchList', backref='watcher', lazy='dynamic')

    def __repr__(self):
        return '<User %r>' % (self.nickname)

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    company_id = db.Column(db.Integer, db.ForeignKey('company.id'))
    initial_price = db.Column(db.Float(asdecimal=True))
    current_price = db.Column(db.Float(asdecimal=True))
    amount = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<User %r>' % (self.balance)

class WatchList(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    company_symbol = db.Column(db.String(6))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))