import unittest
from app.models import Subscribers
from app import db

class SubscriberTest(unittest.TestCase):
    '''
    Test class to test the behavior of the Email class
    '''
    def setUp(self):
        '''
        Set up method that will run before every test
        '''
        self.new_subscriber = Subscribers(email='abc@example.com')
    
    def tearDown(self):
        '''
        Method that will clear up after test has run
        '''
        db.session.delete(self.new_subscriber)
        db.session.commit()
    
    def test_instance(self):
        self.assertTrue(isinstance(self.new_subscriber,Subscribers))

    def test_check_instance_variables(self):
        self.assertEquals(self.new_subscriber.email,'abc@example.com')


    def test_save_review(self):
        self.new_subscriber.save_subscriber()
        self.assertTrue(len(Subscribers.query.all())>0)

        