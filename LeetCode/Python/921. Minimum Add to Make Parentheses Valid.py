"""
See the problem description at: https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/
"""

class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        """
        Time complexity : O(n)
        Space complexity: O(1)
        """
        score1 = score2 = 0
        for char in S:
            if char == '(':
                score1 += 1
            else:
                if score1 == 0:
                    score2 += 1
                else: 
                    score1 -= 1
                
        return score1 + score2
