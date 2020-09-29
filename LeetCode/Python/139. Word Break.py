"""
See the problem description at: https://leetcode.com/problems/word-break/
"""
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        We will use two pointers start and end to consider any substring of the input string s. Pointer end will vary 
        from 1 to len(s) and we also have 0 ≤ start < end. Let us consider a substring of the input string s up to index r, i.e., s[:r]. 
        For this substring to be valid based on the requirements of the problem, there must be a left index l such that the 
        substring up to index l is valid and s[l:r] is also present in the dictionary. For example, suppose s = "isleetcode" and the 
        dictionary contains "is", "leet", and "code". When r = 10, we notice that for l = 6, the substring up to index l = 6, i.e., 
        "isleet" is valid and furthermore, substring s[6:10] is also present in the dictionary. Thus, the input string is a valid 
        string.
        The above example shows that the approach is better to start from r = 1 and increase r accordingly. If so, then we have 
        verified that "isleet" is valid before we want to evaluate the entire input string. Moreover, we can store the validity 
        results of a substring till index l in a 1D array of length 1 + len(s) where the first element corresponds to and empty 
        string and is set to True all the time. We call this array is_valid. 
        For instance, is_valid(1) indicates where the first element in the string can be decomposed using the dictionary word and 
        the last element in is_valid indicates whether the entire input string can be decomposed as such.
        
        Another Example:
        Input: s = "applepen", wordDict = ["app", "apple", "pen"]
        inner loop conditions: is_valid[l] and s[l:r] in wordDict
        r   = 1
        l   = 0    is_valid[0] and s[0:1] in wordDict -> looks at: "",    "a":    no

        r   = 2
        l   = 0    is_valid[0] and s[0:2] in wordDict -> looks at: "",    "ap":   no
            = 1    is_valid[1] and s[1:2] in wordDict -> looks at: "a",   "ap":   no

        r   = 3
        l   = 0    is_valid[0] and s[0:3] in wordDict -> looks at: "" and "app":  yes
                        -> is_valid[3] = True (i.e., "app" can be segmented using the words in wordDict) 
                        -> break
        ...
        when r = 8, we are considering the whole input string and if is_valid[8] = True,
        it means that the input string can be segmented using the words in wordDict.        
 
        """
        
        s_len = len(s)
        is_valid = [False] * (1 + s_len)    # index i >= 1 represents if s[:i] can be segmented using wordDict
        is_valid[0] = True                  # index i = 0 corresponds to an empty string and so is set to True
        word_set = set(wordDict)

        for end in range(1, len(is_valid)): # end of the string to be examined
            for start in range(end):        # start of the string to be examined
                if is_valid[start] and s[start : end] in word_set:
                    is_valid[end] = True
                    break
                    
        return is_valid[s_len]              # represents if the entire s can be segmented using wordDict
