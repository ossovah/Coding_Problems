"""
See the problem description at: https://leetcode.com/problems/simplify-path/
"""

class Solution:
    def simplifyPath(self, path: str) -> str:
        """
        Before describing the solution, it is important to note while command '/..' indicates 
        going one level higher and command '/.'' indicates staying in the same level, the above 
        two commands must be followed by either '/' or nothing (if they occur at the end of path) 
        for the above two commands to be applied. For example, "/a/b/.." results in "/a", while 
        "/a/b/..." results in "/a/b/...".
        To solve this problem, we follow the following steps:
        1) we use the .split('/') to remove all such symbols and obtain the parts (tokens)
        between them. 
        2) Then we use a stack to store the tokens while noting that when we see '..' in the 
        tokens, we pop out the highest element in the stack. We also ensure that '.' and '..' and 
        empty tokens are not added to the stack. 
        3) We combine the elements in the stack to get the path. Before an element is added to the 
        path, we add '/' as this character doesn't exist in the stack. Also, if the stack is empty, 
        which means that we are in the root, we should just return '/'.
        """
        # Step 1:
        tokens = path.split('/')
        
        # Step 2:
        stack = []
        for i in range(1, len(tokens)):        
            if tokens[i] == '.':
                continue
            if tokens[i] == '..':
                if stack:
                    stack.pop()
            elif tokens[i]:
                stack.append(tokens[i])
        
        # Step 3:
        new_path = ''
        for token in stack:
            new_path += '/' + token

        return new_path if stack else "/"