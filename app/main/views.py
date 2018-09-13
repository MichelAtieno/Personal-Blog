from flask import render_template, redirect, url_for,flash
from . import main
from .forms import SubscriberForm
from ..models import User, Subscribers
from ..email import mail_message
from .. import db

@main.route('/',methods=['GET', 'POST'])
def index():

    '''
    View root page function that returns the index page and its data
    '''
    title= "Personal Blog"

    subscribers = SubscriberForm()
    if subscribers.validate_on_submit():
        subscriber = Subscribers(email = subscribers.email.data)
        db.session.add(subscriber)
        db.session.commit()
        flash('You are now subscribed')
        mail_message("Welcome to my blog","email/welcome",subscriber.email,subscriber=subscriber)
        return redirect(url_for('main.index'))

    return render_template('index.html', title=title, subscribers=subscribers)