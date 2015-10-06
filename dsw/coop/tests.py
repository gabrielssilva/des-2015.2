from django.test import TestCase

from .models import User

class UserTest(TestCase):

    def setUp(self):
    	self.user = User(name="name", email="email", password="password")

    	self.name = "name"
    	self.email = "email"
    	self.password = "password"

    def testUnicode(self):
   		self.assertEquals(self.name, unicode(self.user))
   		self.assertEquals("email", self.email)
   		self.assertEquals("password", self.password)
