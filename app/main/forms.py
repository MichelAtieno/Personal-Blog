from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import Required, DataRequired, Length
from app.models import BlogPost, Subscribers

class SubscriberForm(FlaskForm):
    email = StringField('Email', validators=[Required()])
    subscribe = SubmitField('Subscribe')

class BlogPostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired(),Length(min=1, max=1000)])
    photo_url = StringField('Photo URL', validators=[Required()])
    blog_content= TextAreaField('Post your blog', validators=[DataRequired(), Length(min=1)])
    submit = SubmitField('Submit')