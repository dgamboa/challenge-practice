# Notes:
# 1. Understand the problem [3-5 minutes]
# 2. Find a brute force solution [5 minutes]
# 3. Optimize your solution [15 minutes]
# 4. Code your solution [15 minutes]
# 5. Test your solution [5 minutes]

# Day 1,2,3,4,5,6 ************************************************************ #
# Feedback: we don't discuss the patterns, Java in the solutions is a bit more confusing than Python so it's hard to follow, sometimes the workbooks have confusing instructions ****************************************************************************** #

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
