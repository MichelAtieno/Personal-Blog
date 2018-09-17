from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import Required, DataRequired, Length

class SubscriberForm(FlaskForm):
    email = StringField('Email', validators=[Required()])
    subscribe = SubmitField('Subscribe')

class BlogPostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired(),Length(min=1, max=1000)])
    photo_url = StringField('Photo URL', validators=[Required()])
    blog_content= TextAreaField('Post your blog', validators=[DataRequired(), Length(min=1)])
    submit = SubmitField('Submit')

class CommentForm(FlaskForm):
    name = StringField('Name',validators=[Required()])
    comment = TextAreaField('Enter Comment', validators=[Required()])
    submit = SubmitField('submit Comment')
