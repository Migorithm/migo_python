#How to sort a dict by value?
xs= {'a': 4, 'b': 2, 'c': 3, 'd': 1}

print(sorted(xs.items(),key=lambda x:x[1]))

# or use operator
import operator
print(sorted(xs.items(),key=operator.itemgetter(1)))