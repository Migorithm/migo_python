"""
Sometimes our code relies on certain things that we have no control over;
for example, let's say we have a function that goes to our website and pulls down some info.

Now, if that website is down, certainly that's not our fault. But then again, your test will also fail.
That is not what you want because there is nothing wrong with YOUR code. 

We can get around this with something called 'mocking'
"""

import requests
import unittest
from unittest.mock import patch

class Employee:
    raise_amt =1.05
    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.pay=pay
    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first,self.last)
    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)
        
    def monthly_schedule(self,month):
        """
        This is sample method that we are going to pretend that goes to a company's website.
        So the information from the website is what we want to mock. 
        """
        response = requests.get(f'http://company.com/{self.last}/{month}')
        if response.ok:
            return response.text
        else:
            return "Bad Response!"
        
        
class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.emp_1 = Employee("Corey","Migo",50000)
        self.emp_2 = Employee("Suse","Redhat",60000)
    def tearDown(self):
        pass
    
    def test_monthly_schedule(self):
        with patch("05_mocking.requests.get") as mocked_get:  #Specify what you want to mock Here, we want to mock 'request.get' of current module.
            mocked_get.return_value.ok = True #because we want the 'ok' attribute of return value to be True
            mocked_get.return_value.text ="Success" #The same logic as above.
            
            schedule = self.emp_1.monthly_schedule('May') #within the context
            mocked_get.assert_called_with("http://company.com/Migo/May")#We want to make sure that get method in the last call was called with the correct url. 
            self.assertEqual(schedule,"Success")
            
            mocked_get.return_value.ok = False
            schedule = self.emp_2.monthly_schedule("June")
            mocked_get.assert_called_with("http://company.com/Redhat/June")
            self.assertEqual(schedule,"Bad Response!")
            
if __name__ =="__main__":
    unittest.main()