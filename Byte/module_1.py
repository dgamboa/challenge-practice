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

# **************************************************************************** #
# ************** Day 3 ******************************************************* #
# **************************************************************************** #

# Exercise 1: reverse a linked list (https://leetcode.com/problems/reverse-linked-list/)

# First solution:
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        
        pre = None
        nex = head.next
        cur = head

        while cur != None:
            cur.next = pre
            pre = cur
            cur = nex
            if cur:
                nex = cur.next

        return pre

# Refactored:
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        
        cur = head
        nex = cur.next
        cur.next = None

        while nex != None:
            pre = cur
            cur = nex
            nex = cur.next
            cur.next = pre

        return cur

# Exercise 2: implement stack with queue (https://leetcode.com/problems/implement-stack-using-queues/)

# Solution:
from collections import deque

class MyStack:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.main = deque()
        self.store = deque()

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        main = self.main
        store = self.store
        
        while len(main) > 0:
            store.append(main.popleft())
        
        main.append(x)
        
        while len(store) > 0:
            main.append(store.popleft())
        
        return

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        return self.main.popleft()

    def top(self) -> int:
        """
        Get the top element.
        """
        return self.main[0]

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return len(self.main) == 0
