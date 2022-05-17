"""
This stack implementation in the Python standard library is synchronized and provides
locking semantics to support multiple concurrent producers and consumers
"""

from queue import LifoQueue
s = LifoQueue()
s.put("eat")
s.put("sleep")
s.put("code")

print(s)

print(s.get())
print(s.get())
print(s.get())

s.get() #block / waits forever...