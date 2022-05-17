# How to merge two dictionaries?
# In python 3.5+
x = {'a': 1, 'b': 2}
y = {'b': 3, 'c': 4}

z= {**x,**y}

print(z)
#Note that the value of 'b' will be replaced by latter one.