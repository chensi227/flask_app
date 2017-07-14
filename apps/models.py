from apps import db
from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash,check_password_hash
from apps import lm
# http://www.jb51.net/article/86606.htm


class User(db.Model, UserMixin):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True)
    password_hash = db.Column(db.String(64), index=True)
    nickname = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    phone = db.Column(db.String(32), index=True)
    add_time = db.Column(db.DateTime, default=datetime.now())
    update_time = db.Column(db.DateTime, default=datetime.now())

    @property
    def password(self):
        raise AttributeError('password is not readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    @lm.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    def __repr__(self):
        return '<User %r>' % (self.username)


class Member(db.Model):
    __tablename__ = 'member'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True)
    password = db.Column(db.String(64))
    phone = db.Column(db.String(32), index=True)
    email = db.Column(db.String(120), index=True)
    add_time = db.Column(db.DateTime, default=datetime.now())

    def __repr__(self):
        return '<User %r>' % (self.username)


class Article(db.Model):
    __tablename__ = 'article'
    id = db.Column(db.Integer, primary_key= True)
    title = db.Column(db.String(64))
    author = db.Column(db.String(64))
    categroy_id = db.Column(db.Integer,index=True)
    tag_ids = db.Column(db.String(120))
    content = db.Column(db.Text)
    synopsis = db.Column(db.String(120))
    add_time = db.Column(db.DateTime, default=datetime.now())
    update_time = db.Column(db.DateTime,default=datetime.now())

    def __repr__(self):
        return '<User %r>' % (self.title)