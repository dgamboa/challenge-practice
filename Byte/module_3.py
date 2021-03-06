# Notes:
# 1. Understand the problem [3-5 minutes]
# 2. Find a brute force solution [5 minutes]
# 3. Optimize your solution [15 minutes]
# 4. Code your solution [15 minutes]
# 5. Test your solution [5 minutes]

# Day 1,2,3,4,5,6 ************************************************************ #
# Feedback: we don't discuss the patterns, Java in the solutions is a bit more confusing than Python so it's hard to follow, sometimes the workbooks have confusing instructions (how does Day 3 Module 3 fit into the BUD framework? Is the intent to do BUD on the BF solutions for these or code them?). The brute force solution descriptions provided in Day 5 are too simplistic and don't explain enough to be able to move on to the optimization phase 
# **************************************************************************** #

# Day 1 ********************************************************************** #
# Exercise 1: Climb Stairs
# Link: (https://leetcode.com/problems/climbing-stairs/)
  def climbStairs(n):
    if n <= 3:
      return n
      
    prev_prev = 2
    prev = 3
      
    for i in range(4, n + 1):
      temp = prev_prev
      prev_prev = prev
      prev = prev + temp
      
    return prev

# Exercise 2: Merge Intervals
# Link: (https://leetcode.com/problems/merge-intervals/)
# Pseudocode:
  # sort the array
  # start = 0
  # while loop that cycles while start <= len - 1
    # first = a[i]
    # second = a[i + 1]
    # if first[1] >= second[0]:
      # replace the two intervals with a merged interval (using min and max)
    # else:
      # increment start by 1
    # if len of a is 1, break the while loop
  # return a


# Day 2 ********************************************************************** #
# Refer back to previous brute force solutions
# Work through BUD optimization (bottlenecks, unnecessary work, duplicated work)
# Go through existing knowledge and list possible approaches or patterns

# Exercise 1: Max Sum Subarray
# Link: (https://leetcode.com/problems/maximum-subarray/)

import math

def maxSubArrayBF(nums):
  # set variable to track max sum and start with negative infinity
  max_tracker = -math.inf

  # Manage size of subarray with outer loop
  for size in range(1, len(nums) + 1): # -> includes size = 1, 2, 3
    # Manage the start of the subarray with inner loop
    for start in range(len(nums) - size + 1): # -> includes start at 0, 1, 2; 0, 1; 0
      # Create the subarray with start and start + size
      subarr = nums[start : start + size]
      # Sum the subarray
      sub_sum = sum(subarr)
      # Track the max sum so far
      max_tracker = max(max_tracker, sub_sum)
  
  return max_tracker

  # Bottlenecks: replicating the subarray using start and size indexes, summing the subarray after creating it
  # Un. work: rather than creating the array and summing up its items, we could loop through the items once
  # Dup. work: n/a

  # Possible approaches: by recognizing that a negative running sum won't yield larger subarray sum to the right, we can loop through the array once, and track the running sum. If it's negative, we reset the current running sum to zero. If it's positive, we add the current number to the running sum and check to see if it's the max

def maxSubArrayOp(nums):
  # Track the running sum and the previous running sums
  running_sum = 0
  sums_tracker = []

  # Loop through all numbers
  for n in nums:
    # If the running sum including cur n is > 0
    if running_sum + n > 0:
      # Update the running sum
      running_sum += n
      # Add it to the tracker
      sums_tracker.append(running_sum)
    else:
      # Otherwise reset running sum to 0
      running_sum = 0
      # And add the cur n to the tracker
      sums_tracker.append(n)
  
  # Return the max n in the tracker
  return max(sums_tracker)

# Exercise 2: Climbing Stairs
# Link: (https://leetcode.com/problems/climbing-stairs/)
# Comment: the brute force solution here is to calculate all possible combinations recursively. That means we should define the base case and build a recursive function that calculates all possible ways from each step and adds them to the next step through n

  # Bottlenecks: Finding all the combinations will consume lots of time and space
  # Un. work: n/a
  # Dup. work: The recursive nature of the BF solutions means we duplicate lots of the work 

  # Possible approaches: We might be able to derive a mathematical way to get this answer. For 2 options (1 stair or 2 stairs at a time), we know fibonacci applies


# Exercise 3: Merge Intervals
# Link: (https://leetcode.com/problems/merge-intervals/)

  # Bottlenecks: sorting at the beginning, rebuilding the array
  # Un. work: rebuilding the array may be unnecessary
  # Dup. work: could pop an interval that falls inside another interval

  # Possible approaches: I wonder if we could build a queue while we sort. Then we might dequeue the first two intervals and decide whether to append an integrated interval or just the first interval. After that, we would dequeue the next interval and so on. This would avoid replacing intervals (i.e. rebuilding the intervals array)


# Exercise 4: Buy and Sell Stock
# Link: (https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)

  # Bottlenecks: BF approach has nested loops
  # Un. work: we only need to see each price once to know they're in the list, we should be able to do it in O(n) time
  # Dup. work: we recalculate several profits by re-looping over some of the prices

  # Possible approaches: we could track the lowest price and calculate a profit as we go along. If the profit increases, we could change the lowest price and otherwise select the highest profit between the max so far and the profit from the latest price minus the lowest price


# Day 3 ********************************************************************** #
# Code up the solution by hand and test it by hand
# Then copy it to a Leetcode and run it
# Make a list of all the errors

# Exercise 1: Max Binary Tree Depth
# Link: (https://leetcode.com/problems/maximum-depth-of-binary-tree/)

# We can do this with depth-first search and recursion
# The base case is: if node is None -> return 0
# We can then run this function for the left and right nodes adding 1 for the current node
# Finally, we can return the max of the left or right depth
# This ultimately trickles back up to the root node and calculates the max depth

def maxBinaryTreeDepth(root):
  if root is None:
    return 0

  left_depth = maxBinaryTreeDepth(root.left) + 1
  right_depth = maxBinaryTreeDepth(root.right) + 1

  return max(left_depth, right_depth)

# Exercise 2: Linked List Cycles
# Link: (https://leetcode.com/problems/linked-list-cycle/)

# The key to this one is keeping track of the nodes we've seen while traversing the linked list
# We can use a hash table to track nodes by their value
# We can traverse the linked list while current.next is not None

def hasCycle(head):
  if head is None:
    return False
  
  tracker = {}
  current = head

  while current.next is not None:
    if current.next.value in tracker and tracker[current.next.value] == current.next:
      return True
    else:
      tracker[current.next.value] = current.next
      current = current.next
  
  return False

# Exercise 3: Buy and Sell Stock
# Link: (https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)

# Brute Force:
# Nested loops that compare each price to all subsequent prices to calculate profit,
# and tracks max profit across all comparisons
# For example: [7, 1, 5, 3, 6, 4]
# Start with 7, calculate all profits, keep max profit
# Move onto 1, calculate all profits, keep max profit

def buyAndSellBF(prices):
  max_profit = 0

  for i in range(len(prices) - 1):
    for j in range(i + 1, len(prices)):
      profit = prices[j] - prices[i]
      max_profit = max(max_profit, profit)
  
  return max_profit

  # Bottlenecks: n/a
  # Un. work: do we need to do nested loops?
  # Dup. work: we're looking at each price multiple times
  
  # Possible approaches: what if we tracked lowest price so far and max profit;
  # then we might be able to loop only once

def buyAndSellOp(prices):
  lowest = prices[0]
  max_profit = 0

  for i in range(1, len(prices)):
    if prices[i] < lowest:
      lowest = prices[i]
    else:
      max_profit = max(max_profit, prices[i] - lowest)
  
  return max_profit


# Day 4 ********************************************************************** #
# Objective: optimize code using BUD framework
# Use the given brute force solution to (1) compute best conceivable runtime, and (2) draw on knowledge to try to find the most optimal solution you can

# Exercise 1: Longest Consecutive Sequence
# Link: (https://leetcode.com/problems/longest-consecutive-sequence/)

# Example
# Input: nums = [100,4,200,1,3,2]
# Output: 4

# Brute Force Solution:
def longestConsecutiveBF(nums):
  numsSorted = sorted(nums)

  counter = 1
  max_counter = 0

  for i in range(len(numsSorted) - 1):
    if numsSorted[i] + 1 == numsSorted[i + 1]:
      counter += 1
      max_counter = max(max_counter, counter)
    else:
      counter = 1
  
  return max_counter

# BCR: O(n) because we'll need to iterate over the array
# Bottlenecks: we sort the array first, which is time O(n log n)
# Un. Work: the initial sorting may be unnecessary since we're going to loop through all n's
# Dup. Work: n/a
# Knowledge: what if we use a set to track numbers seen. We can loop through the set checking for the start of a sequence with n - 1 in set. Once we find the start of a sequence, we can add 1 while tracking the length of the sequence until the sequence ends

def longestConsecutiveOp(nums):
  # Set a max_length tracker
  max_length = 0
  # Create a set of the nums array -> O(n)
  nums_set = set(nums)

  # Loop through the set -> O(n)
  for n in nums_set:
    # If n - 1 is not in the set, that means it's the start of a sequence
    if n - 1 not in nums_set:
      # Initial conditions:
      # Set the current n to n
      cur_n = n
      # Set the seq length to 1
      seq_length = 1

      # Capture the sequence with this start n by incrementing by 1 and checking if it's in the set
      while cur_n + 1 in nums_set:
        # If it's in the set, keep going and increment the seq length
        cur_n += 1
        seq_length += 1

      # Once we've cycled through this sequence, check to see if it's the global max length so far
      max_length = max(max_length, seq_length)
  
  return max_length


# Exercise 2: Longest Palindromic Substring
# Link: (https://leetcode.com/problems/longest-palindromic-substring/)

# Example
# Input: s = "babad"
# Output: "bab"
# Constraints: characters are digits (0-9) or English letters (a-zA-Z)

# Brute Force Solution:
def longestPalindromeBF(s):
  longest = ""

  for length in range(1, len(s) + 1):
    for start in range(len(s) - length + 1):
      substring = s[start:start + length]
      if substring == substring[::-1]:
        longest = substring
  
  return longest

# BCR: We will need to look at each character at least once so O(n)
# Bottlenecks: Nested loops
# Un. Work: We may not need to reverse the substring which is another nested loop
# Dup. Work: We look at the same character multiple times to form substrings
# Knowledge: palindromes spell the same word forward and backward.

def longestPalindromeOp(s):
  pass
  # if s is None or len(s) < 1:
  #   return ""
  
  # start,end = 0,0

  # for i in range(len(s)):


# Exercise 3: Merge K Sorted Lists
# Link: (https://leetcode.com/problems/merge-k-sorted-lists/)

# Example
# Input: lists = [[1,4,5],[1,3,4],[2,6]]
# Output: [1,1,2,3,4,4,5,6]
# Constraints: lists are sorted in ascending order

# Brute Force Solution:
def mergeKLists(lists):
  store = []
        
  head = point = ListNode(0)

  for list in lists:
    node = list
    while node:
      store.append(node.val)
      node = node.next
  
  for x in sorted(store):
    point.next = ListNode(x)
    point = point.next

  return head.next

# BCR: We'll have to look at each node at least once, so BCR is O(n)
# Bottlenecks: The array store and then sorting the store are the bottlenecks
# Un. Work: Can we get rid of the store, and just cycle through the linked lists?
# Dup. Work: We have an extra head node to help with the return
# Knowledge: We might be able to use a new node to order the nodes. We could set three variables to each node, then pick the lowest of the three as the first node in the returned list. We would replace that variable with that node's next node. Then we could pick the lowest one again, and so on.


# Day 5 ********************************************************************** #
# Objective: optimize code using BUD framework
# Use the given brute force solution to (1) compute best conceivable runtime, and (2) draw on knowledge to try to find the most optimal solution you can

# Exercise 1: LRU Cache
# Link: (https://leetcode.com/problems/lru-cache/) 

# Solution:
from collections import OrderedDict

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.cache:
          return -1
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            del self.cache[key]
        self.cache[key] = value
        
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)

# Commentary: I'm uncertain on how to solve this problem with a brute force solution at this point. I think using a linked list to track the cache, and moving nodes as needed would do it. That would be brute force because iterating over the linked list every time would be O(n) time with n being the cache capacity.
# Optimizing: Learning about OrderedDicts with this implementation was great. The problem becomes very straightforward when using a dictionary that can be ordered.

# Exercise 2: Generate Parentheses
# Link: (https://leetcode.com/problems/generate-parentheses/)

# Example
# Input: int n -> n = 3
# Output: list of valid parentheses combinations -> ["((()))","(()())","(())()","()(())","()()()"]

