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
                                       
        # A dictionary whose keys are node values and the  corresponding values are the 
        # nodes themselves. We can also check if a node has been visited by checking if
        # its value is present in the dictionary
        idx_nodes = {node.val: Node(node.val)}

        # Store the nodes to a stack so they can be process during the depth-first search:
        stack = [node]  
                                
        while stack:
            node = stack.pop()
            for nei in node.neighbors:
                if nei.val not in idx_nodes:
                    stack.append(nei)
                    idx_nodes[nei.val] = Node(nei.val)
                idx_nodes[node.val].neighbors.append(idx_nodes[nei.val])
                
        return idx_nodes[1]
