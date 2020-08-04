"""
See the problem description at: https://leetcode.com/problems/insert-delete-getrandom-o1/
"""
class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data_structure = dict()
        self.vals = collections.deque([])
        self.num = 0
        

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val not in self.data_structure:
            self.num += 1
            self.data_structure[val] = self.num - 1
            self.vals.append(val)
            return True
        return False        
        

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.data_structure: return False
        
        # Retrieve the index of val from the dictionary:
        idx = self.data_structure[val]
        
        # Swap val in the list with the last element in the list, so removal of val from the list
        # would take constant time:
        self.vals[idx], self.vals[-1] = self.vals[-1], self.vals[idx]
        
        # Update the index of the element -that was used to be the last element in the list- in the dict:
        self.data_structure[self.vals[idx]] = idx
        
        # Now remove val from the dict and list:
        tt = self.vals.pop()
        self.data_structure.pop(val)
        
        self.num -= 1
        return True        
        

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return random.choice(self.vals)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()