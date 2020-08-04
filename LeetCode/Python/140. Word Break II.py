"""
See the problem description at: https://leetcode.com/problems/word-break-ii/
"""

class Solution:
    def wordBreak(self, s: str, word_dict: List[str]) -> List[str]:
        def _word_break_rec(s):
            """
            Computes the list of valid word lists that fully break string s based on the words in word_dict
            and stores s and its word lists (if any) in a memo. Then returns the list of word lists for s.
            """
            if not s: return [[]]           # List of empty list            
            if s in memo: return memo[s]    # Return the cached solution directly

            for r in range(len(s)):
                word = s[:r+1]
                if word in word_set:
                    # Break the postfix into words
                    for subsentence in _word_break_rec(s[r+1:]):
                        memo[s].append([word] + subsentence)
            return memo[s]

        word_set = set(word_dict)
        
        # A dictionary whose key are substrings and the values are valid combinations for each substring:
        memo = defaultdict(list)
        
        # Break the input string into lists of words list:
        _word_break_rec(s)
        print(memo)
        
        # Combine the lists of words into sentences:
        return [" ".join(words) for words in memo[s]]