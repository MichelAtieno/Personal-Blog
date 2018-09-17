from . import db, login_manager
from flask_login import UserMixin
from werkzeug.security import generate_password_hash,check_password_hash

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin,db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255))
    pass_secure  = db.Column(db.String(255))

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)

    def __repr__(self):
        return f'User {self.username}'
    
class Subscribers(db.Model):
    __tablename__='subscribers'
    id = db.Column(db.Integer,primary_key = True)
    email = db.Column(db.String(255))

    def save_subscriber(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_subscribers(cls):
        subscribers=Subscribers.query.all()
        return subscribers

    def __repr__(self):
        return f'Subscribers {self.email}'

class BlogPost(db.Model):
    __tablename__='blogs'
    id = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.String())
    blog_post = db.Column(db.String)
    blog_pic = db.Column(db.String)
    photo_url = db.Column(db.String)

    comment = db.relationship('Comment',backref='blog',lazy='dynamic')
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def save_blog(self):
       db.session.add(self)
       db.session.commit()

    
    @classmethod
    def get_blog(cls,id):
        blog = BlogPost.query.filter_by(id = id).all()
        return blog
    
    @classmethod
    def get_all_blogs(cls):
        blogs = BlogPost.query.order_by('-id').all()
        return blogs

class Comment(db.Model):
    __tablename__='comments'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    comment_content = db.Column(db.String())

    blog_id = db.Column(db.Integer, db.ForeignKey('blogs.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    
    def save_comment(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_single_comment(cls,id_blog,id):
        comment = Comment.query.filter_by(blog_id=id_blog,id=id).first()
        return comment
    
    @classmethod
    def get_all_comments(cls,id):
        comments = Comment.query.filter_by(blog_id=id).order_by('-id').all()
        return comments
    
    


