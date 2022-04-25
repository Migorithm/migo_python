"""
Finding duplicate number in linear time and constant space
requires Floyd's Tortoise and Hare.

This is simpole detection algorithm where one pointer traverses twice as fast as another.
And once they meet, you can trace back to the point where the cycle began. 


"""


def find_duplicate(nums):
    tortoise =nums[0]
    hare = nums[0]
    while True:
        tortoise = nums[tortoise]
        hare = nums[nums[hare]]
        if tortoise == hare:
            break
    ptr1=nums[0]
    ptr2=tortoise
    while ptr1 != ptr2:
        ptr1 = nums[ptr1]
        ptr2 = nums[ptr2]
    return ptr1

print(find_duplicate([3,2,1,6,4,6,5]))
        
    
