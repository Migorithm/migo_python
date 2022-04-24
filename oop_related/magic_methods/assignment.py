from __future__ import annotations
from functools import total_ordering


#Using total_ordering decorator, remove redundency of codes
@total_ordering 
class IntervalList:
    """
    A pair of integers define a interval, for example:[1,5). 
    This range includes integers: 1,2,3 and 4. 
    A range list is an aggregate of these ranges: [1,5), [10,11), [100,201)
    """
    
    def __init__(self):
        self._interval_list:list=[]
    
    def add(self,new_interval:list):
        """
        A method to append interval list to _internval_list.
        In case there is an overlap between the existing interval and the newly given interval,
        The existing interval will be either extended or overriden.
        """
        
        # Overriding existing interval when there is a overlab.
        for order, existing_interval in enumerate(self._interval_list):
            low_end = existing_interval[0]
            high_end = existing_interval[1]
            if new_interval[1] < low_end or new_interval[0] > high_end: # no overlab 
                continue
            if new_interval[0] in range(low_end,high_end+1) and new_interval[1] not in range(low_end,high_end):
                high_end = new_interval[1]
                self._interval_list[order] = [low_end,high_end]
                break
            if new_interval[1] in range(low_end,high_end) and new_interval[0] not in range(low_end,high_end):
                low_end = new_interval[0]
                self._interval_list[order] = [low_end,high_end]
                break
            else: #if both ends are within the range
                break
        else:
            self._interval_list.append(new_interval)
    
    @property
    def interval(self):
        return self._interval_list
                      
    def remove(self,interval:list):
        """A method to remove a certain interval from the existing interval list"""
        if not self._interval_list: #empty? 
            return None
        
        #flatten the interval and make a list into a set of elements
        interval_set = {elem for row in [list(range(low_end,high_end)) for low_end,high_end in self._interval_list] for elem in row}
        
        #remove overlaps, if any
        interval_set.difference_update(range(interval[0],interval[1]))
        
        #sort the set in order, making it a list
        interval_elements = sorted(interval_set)
        
        #find continuing members and convert them back into a list
        length = len(interval_elements)
        idx = 0
        lst = []
        while idx < length:
            low = interval_elements[idx]
            while idx < length-1 and interval_elements[idx] +1 == interval_elements[idx+1]:
                idx +=1
            high = interval_elements[idx]
            
            if (high - low >=1):
                lst.append([low,high+1]) #high end is not included.
            idx +=1
        self._interval_list = lst
    
    def print(self):
        "A method to print out the elements in _interval_list in a form of '[x,y)'"
        self._interval_list= sorted(self._interval_list,key=lambda x:x[0])
        print(" ".join(map(lambda x:str(x).replace(']',')'),self._interval_list)))




    #comparison operators 
    # Assuming comparison is done when IntervalList has only one interval,
    def __eq__(self,other: IntervalList) -> bool:
        """
        If the size of self's interval is equal to that of comparison target, one that accounts for higher ordinal numbers is defined as bigger.
        """
        if len(self) == len(other):
            return self[-1] == other[-1]
        else:
            return len(self) == len(other)
        
    def __gt__(self,other: IntervalList)-> bool:
        if len(self) == len(other):
            return self[-1] > other[-1]
        return len(self) > len(other)

    # "in" operator must be "rebelliously misused for the sake of this assignment."
    def __contains__(self,other: IntervalList) -> bool:
        return self[0] <=  other[0] and self[-1] >= other[-1] #inversion!
        
   
    def __len__(self) -> int:
        """This magic method is redefined to streamline the calculation of length."""
        return len(tuple(range(self[0],self[1])))
    
    def __getitem__(self,index) -> int:
        """This magic method is redefined to make it easy to extract the certain element of a list assigned to an IntervalList instance."""
        return self._interval_list[0][index]
        
        
        
import unittest
class Test( unittest.TestCase ):
    def test_interval(self):
        rl = IntervalList()
        rl.add([1,5])
        self.assertEqual([[1,5]] , rl.interval)
        rl.print() # Should display: [1, 5)
        rl.add([10, 20])
        self.assertEqual([[1,5],[10,20]] , rl.interval)
        rl.print() #Should display: [1, 5) [10, 20)
        rl.add([20, 20])
        self.assertEqual([[1,5],[10,20]] , rl.interval)
        rl.print() #Should display: [1, 5) [10, 20)
        rl.add([20, 21])
        self.assertEqual([[1,5],[10,21]] , rl.interval)
        rl.print() #Should display: [1, 5) [10, 21)
        rl.add([2, 4])
        self.assertEqual([[1,5],[10,21]] , rl.interval)
        rl.print() #Should display: [1, 5) [10, 21)
        rl.add([3, 8])
        self.assertEqual([[1,8],[10,21]] , rl.interval)
        rl.print() # Should display: [1, 8) [10, 21)
        rl.remove([10, 10])
        self.assertEqual([[1,8],[10,21]] , rl.interval)
        rl.print() # Should display: [1, 8) [10, 21)
        rl.remove([10, 11])
        self.assertEqual([[1,8],[11,21]] , rl.interval)
        rl.print() #Should display: [1, 8) [11, 21)
        rl.remove([15, 17])
        self.assertEqual([[1,8],[11,15],[17,21]] , rl.interval)
        rl.print() #Should display: [1, 8) [11, 15) [17, 21)
        rl.remove([3, 19])
        self.assertEqual([[1,3],[19,21]] , rl.interval)
        rl.print() #Should display: [1, 3) [19, 21)

        
    def test_comparison(self):
        a = IntervalList()
        a.add([1, 5])
        b = IntervalList()
        b.add([1,6])
        self.assertGreater(b,a)
        self.assertGreaterEqual(b,a)
        self.assertTrue(a in b)
        self.assertFalse(a > b)
        self.assertFalse(a == b)
        
    
        
if __name__ == "__main__":
    unittest.main()
    


