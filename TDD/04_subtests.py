"""
Subtests allow you to conveniently iterate through a collection of test inputs.
Imagine a function called numwords, which counts the number of unique words in a string(ignoring punctuation, spelling and spaces)
"""
import re
import string
def numwords(str:str)-> int:
    p = re.compile("["+string.punctuation+"]") #remove punctuation
    answer = len(set(p.sub("",str).split()))
    return answer


print(numwords("Good, Good morning. Beautiful morning!")) #3

"""
Suppose you want to test how numwords handles excess whitespace. You can easily imagine a dozen different reasonable inputs that will result in the same return value,
and want to verify it can handle them all. You might create something like this
"""

import unittest

class TestWords(unittest.TestCase):
    def test_whitespace(self):
        self.assertEqual(2, numwords("foo bar"))
        self.assertEqual(2, numwords("        foo bar"))
        self.assertEqual(2, numwords("\t foo bar"))
        self.assertEqual(2, numwords("foo         bar"))
        self.assertEqual(2, numwords("\t foo bar \t     \t "))
        
    def test_whitespace_forloop(self):
        """
        The above function seems a bit repetitive. So we might benefit from using a for loop:
        """
        texts = [
            "foo bar",
            "   foo bar",
            "foo\t bar",
            "foo    bar"
            "foo bar    \t  \t"
        ]
        for text in texts:
            self.assertEqual(2, numwords(text))
            
        """
        At first glance, this is certainly more maintainable.
        Howver, using a for loop like this creates more problems that it solves. If you run this, you will get error : 2 != 3
        
        Pop quiz here: out of all the inputs in the list, which caused the bad return value? - there is no way to know; the first problem
        The second is the test stops when the first failure happens. So, here comes 'subtest'
        """
    
    def test_whitespace_subtest(self):
        texts = [
            "foo bar",
            "   foo bar",
            "foo\t bar",
            "foo    bar"
            "foo bar    \t  \t"
        ]
        for text in texts:
            with self.subTest(text=text): #key-value arguments to self.subTest are used in reporting the output. They can be anything that helps you understand exactly what is wrong.
                self.assertEqual(2,numwords(text))
