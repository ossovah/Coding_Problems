"""
See the problem description at: https://leetcode.com/problems/clone-graph/
"""

# Definition for a Node.
class Node
    def __init__(self, val = 0, neighbors = None)
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node: return node

        # Store the nodes to a stack so they can be process during the depth-first search:
        stack = [node]
        
        # A set that stores the node values (indexes) that have been added to the stack:
        visited = {node.val}    
                                
        # A dictionary whose keys are node values (or 1 + list indexes) and the
        # corresponding values are the nodes themselves:
        idx_nodes = {node.val: Node(node.val)}      
                                
        while stack:
            node = stack.pop()
            val = node.val
            neighbors = node.neighbors
            for nei in neighbors:
                if nei.val not in visited:
                    stack.append(nei)
                    visited.add(nei.val)
                if nei.val not in idx_nodes:
                    idx_nodes[nei.val] = Node(nei.val)
                idx_nodes[val].neighbors.append(idx_nodes[nei.val])
                
        return idx_nodes[1]