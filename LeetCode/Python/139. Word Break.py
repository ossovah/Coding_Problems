"""
See the problem description at: https://leetcode.com/problems/word-break/
"""
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        The essence of the solution is based on the 
        """
        
        l_s = len(s)
        is_valid = [False] * (l_s + 1)
        is_valid[0] = True              # '0' refers to an empty string which is assumed to be valid
        
        for r in range(1, l_s + 1):     # r for right pointer
            for l in range(r):          # l for left pointer
                if is_valid[l] and s[l:r] in wordDict:
                    is_valid[r] = True
                    break
        
        return is_valid[-1]