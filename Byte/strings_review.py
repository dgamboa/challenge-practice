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

# Solution using get dict method (would work with any encoding system):
def isAnagramGet(self, s, t):
    dic1, dic2 = {}, {}
    for item in s:
        dic1[item] = dic1.get(item, 0) + 1
    for item in t:
        dic2[item] = dic2.get(item, 0) + 1
    return dic1 == dic2

# Solution using fixed-length array sort (would not work with extended characters):
def isAnagramFixedArraySort(self, s, t):
    s_d, t_d = [0]*26, [0]*26
    for item in s:
        s_d[ord(item)-ord('a')] += 1
    for item in t:
        t_d[ord(item)-ord('a')] += 1
    return s_d == t_d

# Trivial sort solution (time complexity is higher at O(n*logn)):
def isAnagramTrivialSort(self, s, t):
    return sorted(s) == sorted(t)

# Exercise 2: Sorting the characters in a string ( https://www.geeksforgeeks.org/sort-string-characters/ )
def sortString(s):
      store = [0]*26

      for c in s:
        store[ord(c) - ord('a')] += 1
      
      ans = ''
      for i, count in enumerate(store):
        ans += chr(i + ord('a')) * count
      
      return ans

# Trivial sort solution (time complexity is higher at O(n*logn)):
def sortStringTrivial(s):
  return ''.join(sorted(s))

# Exercise 3: Longest substring without repeating characters (https://leetcode.com/problems/longest-substring-without-repeating-characters/)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        max_length = 0
        
        seen = {}
        
        for i, c in enumerate(s):
            if c in seen and seen[c] >= start:
                start = seen[c] + 1
            else:
                max_length = max(max_length, i - start + 1)
                
            seen[c] = i
        
        return max_length
# Runtime: 48 ms, faster than 96.41% of Python3 online submissions for Longest Substring Without Repeating Characters.
# Memory Usage: 14.3 MB, less than 53.12% of Python3 online submissions for Longest Substring Without Repeating Characters.
