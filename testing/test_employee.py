import unittest

class Employee:
    raise_amt = 1.05

    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first,self.last)
    
    @property
    def fullname(self):
        return '{} {}'.format(self.first,self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)


class TestEmployee(unittest.TestCase):

    @classmethod    #it runs only once at the very beginning
    def setUpClass(cls):
        print("SETUPCLASS")

    @classmethod    #it runs only once at the very end
    def tearDownClass(cls):
        print("TEARDOWNCLASS")

    #DRY(don't repeat yourself)
    def setUp(self):
        print("SetUp")
        self.emp_1 = Employee("Corey","Schafer",50000)
        self.emp_2 = Employee("Sue","Smith",60000)

    def tearDown(self):
        print("TearDown\n")
        # tearDown exists just in case you created file to a directory or database
        # you could delete all of those so that you can go back to clean state
        pass


    def test_email(self):
        print("Test email")
        self.assertEqual(self.emp_1.email, "Corey.Schafer@email.com")
        self.assertEqual(self.emp_2.email, "Sue.Smith@email.com")

        self.emp_1.first = "John"
        self.emp_2.first = "Jane"
        self.assertEqual(self.emp_1.email, "John.Schafer@email.com")
        self.assertEqual(self.emp_2.email, "Jane.Smith@email.com")

    def test_apply_raise(self):
        print("Test raise")
        self.emp_1.apply_raise()
        self.emp_2.apply_raise()

        self.assertEqual(self.emp_1.pay,52500)
        self.assertEqual(self.emp_2.pay,63000)
        