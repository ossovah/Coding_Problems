"""
See the problem description at: https://leetcode.com/problems/word-break/
"""
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        We will use two pointers l (for left) and r (for right) to consider any substring of the input string s. Pointer r will vary from 1 to len(s) 
        and we also have 0 ≤ l < r. Let us consider a substring of the input string s up to index r, i.e., s[:r]. For this substring to be valid based 
        on the requirements of the problem, there must be a left index l such that the substring up to index l is valid and s[l:r] is also present in 
        the dictionary. For example, suppose s = "isleetcode" and the dictionary contains "is", "leet", and "code". When r = 10, we notice that for 
        l = 6, the substring up to index l = 6, i.e., "isleet" is valid and furthermore, substring s[6:10] is also present in the dictionary. Thus, 
        the input string is a valid string.
        The above example shows that the approach is better to start from r = 1 and increase r accordingly. If so, then we have verified that "isleet" 
        is valid before we want to evaluate the entire input string. Moreover, we can store the validity results of a substring till index l in a 1D 
        array of length 1 + len(s) where the first element corresponds to and empty string and is set to True all the time. We call this array is_valid. 
        For instance, is_valid(1) indicates where the first element in the string can be decomposed using the dictionary word and the last element in 
        is_valid indicates whether the entire input string can be decomposed as such.
 
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
