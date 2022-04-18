import unittest
from angle import Angle
class TestAngle(unittest.TestCase): #User define Test class inheriting unittest.TestCase
    def test_degrees(self): #1
        small_angle = Angle(60)
        self.assertEqual(60,small_angle.degrees)
        self.assertTrue(small_angle.is_acute())
        big_angle =Angle(320)
        self.assertFalse(big_angle.is_acute())
        funny_angle = Angle(1081)
        self.assertEqual(1,funny_angle.degrees)
     
    def test_arithmetic(self): #1
        small_angle = Angle(60)
        big_angle = Angle(320)
        total_angle = small_angle.add(big_angle)
        self.assertEqual(20,total_angle.degrees,"Adding angles with wrap-around") #2 



"""
#1
both test_degrees and test_arithmetic have assertions, using some methods of TestCase: assertEqual, assertTrue, assertFalse
Every methods in which you want to test things out MUST start with 'test'


#2 Last assertion includes a custom message, as its third argument

To see how it works, let's define Angle in angle.py

class Angle:
    def __init__(self,degrees):
        self.degrees=0
    
    def is_acute(self):
        return False
    
    def add(self,other_angle):
        return Angle(0)


and run it. 

python3 -m unittest 01_test.py

And you will see the following output:
- FF



Notice that test_degrees makes several assertions, but only the first one has been run. 

At this point, we have a correctly failing test. The next step is to actually make that test pass.




'''
from __future__ import annotations
class Angle:
    def __init__(self,degrees):
        self.degrees= degrees % 360
    
    def is_acute(self):
        return self.degrees < 90
    
    def add(self,other_angle:Angle):
        return Angle(self.degrees + other_angle.degrees)
'''

python3 -m unittest 01_test.py

Ran 2 tests in 0.000s

OK


---------

assertEqual, assertTrue, assertFalse will be the most common assertion methods you'll use, along with assertNotEqual 

If you try checking that two dictionaries are equal, and they are not, the output is tailored to the data type: highlighting which key is missing.

What's actually happening is that unittest provides certain type-specialized asssertions, like: 
- assertDictEqual
- assertListEqual
and more. 

In fact, you almost never need to invoke them directly: if you invoke assertEqual with two directories, it automatically dispatches to 
assertDictEqual and similar for the other types(list, set, tuple...)


"""

