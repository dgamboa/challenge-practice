# Notes:
# 1. Understand the problem [3-5 minutes]
# 2. Find a brute force solution [5 minutes]
# 3. Optimize your solution [15 minutes]
# 4. Code your solution [15 minutes]
# 5. Test your solution [5 minutes]

# Day 1,2,3,4,5,6 ************************************************************ #
# Feedback: we don't discuss the patterns, Java in the solutions is a bit more confusing than Python so it's hard to follow, sometimes the workbooks have confusing instructions (how does Day 3 Module 3 fit into the BUD framework? Is the intent to do BUD on the BF solutions for these or code them?)****************************************************************************** #

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
# Knowledge: what if we use a hash table to track numbers seen with the number as the key, and make the value pair the counter. We can then track a max_counter as we loop through the array

def longestConsecutiveOp(nums):
  tracker = {}
  max_counter = 0

  for n in nums:
    if n in tracker:
    else:
      tracker[n]
