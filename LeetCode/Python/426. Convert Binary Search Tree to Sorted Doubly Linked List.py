"""
See the problem description at: 
https://leetcode.com/problems/convert-binary-search-tree-to-sorted-doubly-linked-list/

Solution:
Here are the steps for my solution:
1) A helper function is called recursively to process all the nodes in an inorder traversal of the 
depth-first search algorithm. The helper function takes a node, then recursively calls itself to 
process its left and right subtrees. From processing each subtree, it receives the head and tail of 
doubly linked lists (but not circular). Then it connects them to itself and returns the head and 
tail of the updated (longer) linked list to its parent node.

2) The parent node does a similar operation and this continues until we reach the root.

3) At the root node, the head and tail are connected such that we would have a circular doubly 
linked list.

Definition for a Node:

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        def _build_list(node):
            if not node.left and not node.right: return node, node
            if node.left:
                left_low, left_high = _build_list(node.left)
                node.left = left_high
                left_high.right = node
            if node.right:
                right_low, right_high = _build_list(node.right)
                right_low.left = node
                node.right = right_low
            
            if node.left and node.right:
                return left_low, right_high
            if node.left:
                return left_low, node
            return node, right_high                
        
        if not root: return root
        
        root, tail = _build_list(root)
        root.left = tail
        tail.right = root  
        
        return root