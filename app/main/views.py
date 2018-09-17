from flask import render_template, redirect, url_for,flash, abort
from . import main
from .forms import SubscriberForm, BlogPostForm, CommentForm
from ..models import User, Subscribers, BlogPost, Comment
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

    all_blogs = BlogPost.get_all_blogs()
    if all_blogs:
        blogs= all_blogs
        return render_template('index.html',title=title, all_blogs= blogs, subscribers=subscribers)
    elif not all_blogs:
        blog_status= 'There are no blogs'
        return render_template('index.html', title=title, blog_status=blog_status,subscribers=subscribers)

@main.route('/create_blogpost', methods = ['GET', 'POST'])
@login_required
def create_blogpost():
    title="Create BlogPost"

    blog_form = BlogPostForm()

    if blog_form.validate_on_submit():
        blog = BlogPost(title= blog_form.title.data, blog_post= blog_form.blog_content.data)
        db.session.add(blog)
        db.session.commit()
        return redirect(url_for('main.create_blogpost'))

    comment_form = CommentForm()
    if comment_form.validate_on_submit():
        new_comment = Comment(name= comment_form.name.data, comment_content= comment_form.comment_content.data)
        db.session.add(new_comment)
        db.session.commit()
        return redirect(url_for('main.create_blogpost'))


    return render_template('blog.html', BlogPost = blog_form, title=title, comment_form=comment_form)

@main.route('/blogpost/<id>', methods=['POST','GET'])
def blogpost(id):
    
    title= f'Posts' 
    blog = BlogPost.query.filter_by(id=id).first()
    comment_form = CommentForm()
    if comment_form.validate_on_submit():
        new_comment = Comment(name= comment_form.name.data,comment_content = comment_form.comment_content.data, blog_id=id)
        db.session.add(new_comment)
        db.session.commit()
        return redirect(url_for('main.blogpost',id=blog.id))

    all_comments = Comment.query.all()
    blog_comments = Comment.query.filter_by(blog_id=id).all()

    return render_template('blogpost.html', title = title, blog=blog, comment_form=comment_form,all_comments=all_comments,blog_comments=blog_comments)

@main.route('/blog/<int:id>/<int:id_comment>/delete_comment')
@login_required
def delete_comment(id,id_comment):
    comment = Comment.get_single_comment(id,id_comment)

    db.session.delete(comment)
    db.session.commit()

    flash('Comment has been deleted')

    return redirect(url_for('main.blogpost',id=id))


