from . import db

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255))

    def __repr__(self):
        return f'User {self.username}'
    
class Subscribers(db.Model):
    __tablename__='subscribers'
    id = db.Column(db.Integer,primary_key = True)
    email = db.Column(db.String(255))

    def __repr__(self):
        return f'Subscribers {self.email}'

