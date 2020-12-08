
from django.test import TestCase,SimpleTestCase,TransactionTestCase
 


# Create your tests here.




class PageLoadTests(TransactionTestCase):
    
    def test_home_status_code(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)

    def test_login_signup_status_code(self):
        response = self.client.get('/login_register/')
        print(response)
        self.assertEquals(response.status_code, 200)
 