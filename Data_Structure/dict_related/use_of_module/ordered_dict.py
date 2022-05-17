"""
Python includes a specialied dict subclass that remembers the insertion order of keys
added to it. 

If key order is important for your algorithm to work, it's best to communicate this by using
OrderedDict class.

"""

import collections

d = collections.OrderedDict(one=1, two=2 , three=3 )
print(d)

d["four"] = 4
print(d)
print(d.keys())