"""

Sometimes your code is supposed to raise an exception. 
IF that conditions occurs and your code does NOT raise the correct exception, that's a bug. How do you write test code for this situation?

-> assertRaises used with 'with' statement

For example, suppose your are writing a library that translates Roman numerals into integers. 
You decide that that passing nonsensical input to roman2int should raise a ValueError. Here's how you write a test to assert that behaviour.
"""

import unittest
from roman import roman2int

class TestRoman(unittest.TestCase):
    def test_roman2int_error(self):
        with self.assertRaises(ValueError):
            roman2int("This is not a valid roman numeral")
    


