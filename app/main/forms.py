from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Required

class EmailForm(FlaskForm):
    name = StringField('User Name', validators=[Required()])
    email = StringField('Email', validators=[Required()])
    subscribe = SubmitField('Subscribe')
