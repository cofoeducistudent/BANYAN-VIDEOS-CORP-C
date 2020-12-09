
from django.test import TestCase,SimpleTestCase,TransactionTestCase
 


# Create your tests here.




class PageLoadTests(TransactionTestCase):
    
    def test_home_status_code(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)

    def test_login_signup_status_code(self):
        response = self.client.get('/login_register/login_register')
        self.assertEquals(response.status_code, 200)

    def test_account(self):
        response = self.client.get('/my_account/my_account')
        self.assertEquals(response.status_code, 302)
        
        
    def test_search(self):
        response = self.client.get('/search_results/search_results')
        self.assertEquals(response.status_code, 200)
            
        
    def test_shopping_cart(self):
        response = self.client.get('/shopping_cart/shopping_cart')
        self.assertEquals(response.status_code, 200)
        
    def test_about(self):
        response = self.client.get('/about/about')
        self.assertEquals(response.status_code, 200)
        
    def test_members(self):
        response = self.client.get('/members/members')
        self.assertEquals(response.status_code, 302)
        
    def test_contact(self):
        response = self.client.get('/contact/contact')
        self.assertEquals(response.status_code, 200)
        
    
    def test_logout(self):
        response = self.client.get('/logout/logout')
        self.assertEquals(response.status_code, 200)  
    
    
 