"""
deque class implements a double-ended queue that supports adding and removing elements 
from either end in O(1) time(non-amortized).

It's great tool for inserting and deleting elements but has poor O(n) performance for randomly accessing
elements in the middle of a stack.

"""

from collections import deque

#Stack
s = deque()
s.append("eat")
s.append("sleep")
s.append("code")

print(s)
print(s.pop())
print(s.pop())
print(s.pop())




#Queue
s.append("eat")
s.append("sleep")
s.append("code")
print(s.popleft())
print(s.popleft())
print(s.popleft())