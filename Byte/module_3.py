# Notes:
# 1. Understand the problem [3-5 minutes]
# 2. Find a brute force solution [5 minutes]
# 3. Optimize your solution [15 minutes]
# 4. Code your solution [15 minutes]
# 5. Test your solution [5 minutes]

# Day 1,2,3,4,5,6 ************************************************************ #

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
