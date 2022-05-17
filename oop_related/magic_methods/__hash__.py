"""
There are some restrictions on which objects can be used as valid keys.
Python dictionaries are indexed by keys that can be of any hashable type: 
A hashable object has a hash value which never changes during its lifetime(__hash__) 
AND it can be compared to other objects(__eq__)

Immutable types like strings and numbers are therefore hashable and work well as keys.
"""