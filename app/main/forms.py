from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Required

class SubscriberForm(FlaskForm):
    email = StringField('Email', validators=[Required()])
    subscribe = SubmitField('Subscribe')
