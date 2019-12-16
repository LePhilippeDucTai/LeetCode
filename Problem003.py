# Given a string, find the length of the longest substring without repeating characters.

# Example 1:

# Input: "abcabcbb"
# Output: 3 
# Explanation: The answer is "abc", with the length of 3. 

# Example 2:

# Input: "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:

# Input: "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3. 
#              Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

# Gives the list of all of the substrings that form the string s of given size
import functools

def _substrings(s: str, of_size : int) -> list :
    def loop(acc : list, s: str) -> list :
        if len(s) < of_size or len(s) == 0 :
            return(acc)
        else :
            acc.update(s[:of_size])
            return(loop(acc, s[1:]))
    return(loop(set(), s))    

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        of_size = len(s)
        length_set = lambda l, n : len(set(l)) == n
        for i in reversed(range(1, of_size + 1)) :
            x = _substrings(s, i)
            mapping_set = set(map(functools.partial(length_set, n = i), x))
            if True in mapping_set :
                return(i)
        return(0)
        
if __name__ == "__main__":
    s = "PhilippeAzertyuiopqsdfgh"
    obj = Solution()
    ss = _substrings(s, 5)
    print(ss)