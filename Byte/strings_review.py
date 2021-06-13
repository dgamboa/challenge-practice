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

# **************************************************************************** #
# ************** Day 2 ******************************************************* #
# **************************************************************************** #

# Exercise 1: Remove Duplicates ( https://leetcode.com/problems/remove-duplicates-from-sorted-array/ )
def removeDuplicates1(nums):
    if len(nums) == 0:
        return 0
    
    curr = nums[0]
    i = 1
    
    for n in nums:
        if curr != n:
            nums[i] = n
            curr = n
            i += 1
    
    return i

# Refactor:
def removeDuplicates2(nums):
    pointer = 0
    
    for i in range(1, len(nums)):
        if nums[pointer] != nums[i]:
            pointer += 1
            nums[pointer] = nums[i]
            
    return pointer + 1

# Exercise 2: Is String Palindrome ( https://leetcode.com/problems/valid-palindrome/ )
# Partial Solution:
class Solution:
    def isPalindrome(self, s: str) -> bool:
        lower_s = s.casefold()
        rev_lower_s = lower_s[::-1]
        
        print(lower_s)
        print(rev_lower_s)
        
        i = 0
        j = 0
        
        for x in range(len(s)):
            for y in range(i, len(s)):
                if ord('a') <= ord(lower_s[y]) <= ord('z'):
                    break    
                else:
                    i += 1
            
            for y in range(j, len(s)):
                if ord('a') <= ord(rev_lower_s[y]) <= ord('z'):
                    break    
                else:
                    j += 1
            
            if lower_s[i] != rev_lower_s[j]:
                print(i)
                print(j)
                return False
            else:
                i += 1
                j += 1
            
            if i == len(s) or j == len(s):
                break
        
        return True
            
            

# Working Solution (two-pointers beginning and end):
def isPalindrome(self, s):
    l, r = 0, len(s)-1
    while l < r:
        while l < r and not s[l].isalnum():
            l += 1
        while l <r and not s[r].isalnum():
            r -= 1
        if s[l].lower() != s[r].lower():
            return False
        l +=1; r -= 1
    return True
