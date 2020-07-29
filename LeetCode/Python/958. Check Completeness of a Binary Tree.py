"""
See the problem description at: https://leetcode.com/problems/check-completeness-of-a-binary-tree/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        if not root: return True        
        queue = collections.deque([root])
        while queue:
            node = queue.popleft()
            # We are allowed to add None to the queue. But when we reach a
            # None, there must be no entry in the queue other than None:
            if node is None: return False if any(queue) else True # 
            
            # If a node has a right child but no left child, this violates
            # the completeness condition. This the node level check:
            if node.right and not node.left: return False 
            
            # We have no issue with adding None if it is what node.left and/or
            # node.right is:
            queue.append(node.left)
            queue.append(node.right)                