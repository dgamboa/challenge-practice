# **************************************************************************** #
# ************** Day 1 ******************************************************* #
# **************************************************************************** #

# Exercise 1: Anagrams ( https://leetcode.com/problems/valid-anagram/ )
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False 
        
        s_d = {}
        t_d = {}
        
        for i in range(len(s)):
            cs = s[i]
            ct = t[i] 
            
            if cs in s_d:
                s_d[cs] += 1
            else:
                s_d[cs] = 1
            
            if ct in t_d:
                t_d[ct] += 1
            else:
                t_d[ct] = 1
        
        return s_d == t_d
# Runtime: 48 ms, faster than 68.28% of Python3 online submissions for Valid Anagram.
# Memory Usage: 14.4 MB, less than 76.38% of Python3 online submissions for Valid Anagram.

# Exercise 2: Sorting the characters in a string ( https://www.geeksforgeeks.org/sort-string-characters/ )
