"""
For the problem description, see: https://leetcode.com/problems/basic-calculator-ii/ 
"""
class Solution:
    def calculate(self, st: str) -> int:
        """
        Step 1: Create a list of tokens where each token is either one of the symbols
        in "=-*/" or an integer. The tokens are collected by left-to-right scanning of
        the input string. Note that each integer token represents a complete number 
        between two operational tokens "+-*/" in the string.
        """
        tokens = []        
        num = ''
        for s in st:
            if s == ' ':
                continue
            if s in '+-*/':
                tokens.append(int(num))
                tokens.append(s)
                num = ''
            else:
                num += s
        tokens.append(int(num))
        
        """
        step 2: Add the integers to a stack. Each entry in the stack corresponds to one
        the result of the calculation that is between a pair of operations from "+-".
        The goal is to obtain the final summation by adding the entries in the stack. 
        Thus, the numbers should be signed where the sign is determined by the preceeding
        "+-". 
        """        
        stack = []
        operation = '+' # This is for the first integer token, since it doesn't have a 
                        # preceeding operational token
        for token in tokens:
            if isinstance(token, int):
                if operation == '+':
                    stack.append(token)
                if operation == '-':
                    stack.append(-token)
                if operation == '*':
                    stack.append(stack.pop() * token)
                if operation == '/':
                    stack.append(int(stack.pop() / token)) # division towards 0
            else:
                operation = token
                
        return sum(stack)