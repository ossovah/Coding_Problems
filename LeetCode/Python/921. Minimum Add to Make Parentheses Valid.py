"""
See the problem description at: https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/
"""

class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        stack = []
        for s in S:
            if s == '(':
                stack.append(s)
            else:
                if stack and stack[-1] == '(':
                    stack.pop()
                else:
                    stack.append(')')
        return len(stack) 