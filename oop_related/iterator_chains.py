"""
By chaining together multiple iterators,  you can write highly efficient data processing pipelines.

Generators can be connected to each other in order to build efficient data processing algorithms that work like a pipeline.
"""

def integers():
    for i in range(1,9):
        yield i
        
def squared(seq):
    for i in seq:
        yield i*i
        
chain = squared(integers())
print(list(chain)) #[1, 4, 9, 16, 25, 36, 49, 64]

"""
We can keep on adding new building blocks to this pipeline. Data flows in one direction only.
This is similar to how pipelines work in Unix.

Data processing happens one element at a time - There is no buffering between the processing steps in the chain:
"""


def negate(lst):
    for i in lst:
        yield -i
        
chain = negate(squared(integers()))
print(list(chain))