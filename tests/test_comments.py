import unittest
from app.models import Comment, BlogPost
from app import db

class CommentTest(unittest.TestCase):

    def setUp(self):
        self.new_blog = BlogPost(title='New Blog',blog_post='This is the content')
        self.new_comment = Comment(name='Test Comment', comment_content='This is my comment', blog=new_blog)

    def tearDown(self):
        db.session.delete(self.new_blog)
        db.session.commit()
        db.session.delete(self.new_comment)
        db.session.commit()

    def test_instance(self):
        self.assertTrue(isinstance(self.new_comment,Comment))

    def test_check_instance_variables(self):
        self.assertEquals(self.new_comment.name,'Test Comment')
        self.assertEquals(self.new_comment.email,'another@example.com')
        self.assertEquals(self.new_comment.comment_content,'This is my comment')
        self.assertEquals(self.new_comment.blog, new_blog)


    def test_save_comment(self):
        self.new_comment.save_comment()
        self.assertTrue(len(Comment.query.all())>0)
