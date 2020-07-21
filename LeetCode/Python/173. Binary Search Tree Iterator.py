"""
For the problem description, see: https://leetcode.com/problems/binary-search-tree-iterator/
In this approach, we store the entire values in the tree in a list. Then we use heapq.heapify 
to convert the list into a min heap. The min heap is then used in the next and hasNext methods. 
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator:

    def __init__(self, root: TreeNode):
        self.val_ascending = []
        nodes = collections.deque([root])
        while nodes:
            node = nodes.pop()
            if node:
                self.val_ascending.append(node.val)
                nodes.append(node.left)
                nodes.append(node.right)
        heapq.heapify(self.val_ascending)
        

    def next(self) -> int:
        """
        @return the next smallest number
        """
        return heapq.heappop(self.val_ascending)
        

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return True if self.val_ascending else False
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()