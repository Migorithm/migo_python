"""
collections.ChainMap data structure groups multiple dictionaries into a single mapping.
Lookups search the underlying mappings one by one until a key is found.

Insertions, updates, and deletions only affect the first mapping
"""

from collections import ChainMap

dict1 = dict(one=1, two=2)
dict2 = dict(three=3,four=4)
dict3 = dict(five=5,six=6)
chain = ChainMap(dict1,dict2,dict3)

print(chain)

print(chain.get("one"))
chain.pop("one")
print(chain)