# **************************************************************************** #
# ************** Day 2 ******************************************************* #
# **************************************************************************** #

# Exercise 1: Longest substring without repeating characters (https://leetcode.com/problems/longest-substring-without-repeating-characters/)
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

# Exercise 2: Occurrences of an anagram in a string (https://leetcode.com/problems/find-all-anagrams-in-a-string/)

# Brute force solution:
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        
        for i in range(len(s) - len(p) + 1):
            sub = s[i:len(p) + i]
            if sorted(sub) == sorted(p):
                res.append(i)
        
        return res

# Attempt - passes most tests but fails for duplicates (e.g. s = "abcabccbbaa" and p = "aabbcc")
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        start = 0
        match = {}
        
        for c in p:
            match[c] = match.get(c, 0) + 1
        
        tracker = {}
        ans = []
        
        for i, c in enumerate(s):
            if c in match:
                tracker[c] = tracker.get(c, 0) + 1
                if tracker == match:
                    ans.append(start)
                    tracker[s[start]] -= 1
                    start += 1
                elif tracker[c] > match[c]:
                    if c == s[start]:
                        start += 1
                        tracker[c] -= 1
                    else:
                        start = i
                        tracker = {}
                        tracker[c] = 1
            else:
                start = i + 1
                tracker = {}
        
        return ans

# Solution post-Byte review with sliding window and fixed-length arrays:
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res= []

        match = [0] * 26
        compare = [0] * 26

        for c in p:
            match[ord(c) - ord('a')] += 1

        for c in s[:len(p)]:
            compare[ord(c) - ord('a')] += 1

        if match == compare:
            res.append(0)

        for start in range(1, len(s) - len(p) + 1):
            compare[ord(s[start - 1]) - ord('a')] -= 1
            compare[ord(s[start + len(p) - 1]) - ord('a')] += 1

            if match == compare:
                res.append(start)

        return res
