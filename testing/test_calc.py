import unittest
#https://docs.python.org/3/library/unittest.html#unittest.TestCase.debug

def add(x,y):
    """Add function"""
    return x+y

def subtract(x,y):
    """Subtract function"""
    return x-y

def multiply(x,y):
    """Multiply function"""
    return x*y

def divide(x,y):
    """Divide function"""
    if y == 0:
        raise ValueError("Cannot divide by Zero!")
    return x/y

class TestCalc(unittest.TestCase):
    #Naming convention is required any test case that you want to be tested must start with "test_"
    def test_add(self):
        self.assertEqual(add(10,5),15)
        self.assertEqual(add(-1,1),0)
        self.assertEqual(add(-1,-1),-2)
    #To run the test, you need to run :
        # python3 -m unittest test_calc.py
    #If it says "OK", it means everything is OK

    def test_subtract(self):
        self.assertEqual(subtract(10,5),5)
        self.assertEqual(subtract(-1,1),-2)
        self.assertEqual(subtract(-1,-1),0)    

    def test_multiply(self):
        self.assertEqual(multiply(10,5),50)
        self.assertEqual(multiply(-1,1),-1)
        self.assertEqual(multiply(-1,-1),1)

    def test_divide(self):
        self.assertEqual(divide(10,5),2)
        self.assertEqual(divide(-1,1),-1)
        self.assertEqual(divide(-1,-1),1)

        #To check if it raises error as expected  -- Way1
        self.assertRaises(ValueError,divide, 10,0)

        # Way 2 - The way suggested above necessitated passing argument separately; not good. 
        with self.assertRaises(ValueError):
            divide(10,0)
        




#Alternatively, you run tests by writing the following parts.
if __name__ =="__main__":
    unittest.main()


