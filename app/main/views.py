from flask import render_template, redirect, url_for,flash
from . import main
from .forms import SubscriberForm, BlogPostForm
from ..models import User, Subscribers, BlogPost
from ..email import mail_message
from .. import db
from flask_login import login_required, current_user

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

@main.route('/create_blogpost', methods = ['GET', 'POST'])
@login_required
def create_blogpost():
    blog_form = BlogPostForm()

    if blog_form.validate_on_submit():
        title= blog_form.title.data
        blog = blog_form.blog_content.data

        new_blog = BlogPost(title=title, blog_post=blog)
        new_blog.save_blog()

        return redirect(url_for('main.blog',id=new_blog.id))
    
    return render_template('create_blog.html', blog_form=blog_form)