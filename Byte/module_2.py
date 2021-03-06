# Notes:
# 1. Understand the problem [3-5 minutes]
# 2. Find a brute force solution [5 minutes]
# 3. Optimize your solution [15 minutes]
# 4. Code your solution [15 minutes]
# 5. Test your solution [5 minutes]

# Day 1,2,3,4,5,6 ************************************************************ #
# Focus Day 1: understand the problem **************************************** #
# Focus Day 2,3,4,5: brute force solutions & optimization ******************** #

# Exercise 1: Maximum Sum Subarray
# Link: (https://leetcode.com/problems/maximum-subarray/)
# Assumptions: all items are integers, can be positive / negative, no empty subarray 
# Examples walk through ✅
# Custom examples (edges): [7,-8,9] => 9
# Function signature: def maxSubArray(nums: List[int]) -> int:
# IN: array of integers / OUT: integer with max sum
def maxSubArray(nums):
  print(nums)

# Import math module to use negative infinity as initial max
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

# Optimization:
# Time Complexity of BF Solution: O(n^2) -> because n * (n + 1) / 2 simplifies to n^2; although the above may be O(n^3) taking into account that building subarrays using start and start + size is O(n--)
# Space Complexity of BF Solution: O(n) -> subarr is an array that will grow to the size of the input
# Best conceivable runtime: it seems like O(n^2) may be the optimal runtime because we have to compute all possible subarrays to determine the largest one

# Description:
# Set a tracker variable for the max sum at negative infinity
# Iterate through every subarray and compare its sum to the previous max
  # Iterate by establishing a size outer loop that cycles through the smallest subarray to the full array,
  # and a start inner loop that determines the subarray start index; start increments until the subarray end is the last index of the main array based on size
# If the sum is higher, update the max
# Return the max sum


# Exercise 2: Number of Islands
# Link: (https://leetcode.com/problems/number-of-islands/)
# Assumptions: grid edges are surrounded by water, 1s are land, 0s are water, 2D binary grid, not connected unless adjacent hz or vt, numbers are strings
# Examples walk through ✅
# Custom examples (edges):
  # Input: grid = [
  #   ["1","0","0","0","0"],
  #   ["0","1","0","0","0"],
  #   ["0","0","1","0","0"],
  #   ["0","0","0","1","0"]
  # ]
  # Output: 4
  # Input: grid = [
  #   ["1","1","1","0","1"],
  #   ["1","1","1","0","0"],
  #   ["1","0","1","0","1"],
  #   ["1","1","1","0","0"]
  # ]
  # Output: 3
# Function signature: def numIslands(grid: List[List[str]]) -> int:
# IN: matrix (i.e. list with lists are items with strings as items) / OUT: integer with islands count
def numIslands(grid):
  print(grid)

# Helper method to add neighbors to tracker
def trackSelfAndNeighbors(t,g,r,c):
  k = str(r) + str(c)
  t[k] = t.get(k, g[r][c])

  if r != 0:
    k1 = str(r - 1) + str(c)
    t[k1] = t.get(k1, g[r - 1][c])

  if c != 0:
    k2 = str(r) + str(c - 1)
    t[k2] = t.get(k2, g[r][c - 1])

  if r != len(g) - 1:
    k3 = str(r + 1) + str(c)
    t[k3] = t.get(k3, g[r + 1][c])

  if c != len(g[0]) - 1:
    k4 = str(r) + str(c + 1)
    t[k4] = t.get(k4, g[r][c + 1])
  
def checkLandConnection(t,g,r,c):
  flag = not not int(t.get(g[r][c], '0'))

  if r != 0:
    k1 = str(r - 1) + str(c)
    flag = not not int(t.get(k1, '0')) or flag

  if c != 0:
    k2 = str(r) + str(c - 1)
    flag = not not int(t.get(k2, '0')) or flag

  if r != len(g) - 1:
    k3 = str(r + 1) + str(c)
    flag = not not int(t.get(k3, '0')) or flag

  if c != len(g[0]) - 1:
    k4 = str(r) + str(c + 1)
    flag = not not int(t.get(k4, '0')) or flag
  
  return not flag

def numIslandsBF(grid):
  # Set up islands counter
  islands = 0

  # Set up tracker of land with key as position (e.g. 00, 01, 02, 10, 11, 12, 20, 21, 22) and value as "1" or "0"
  land_tracker = {}

  # Loop through grid with nested loops for row and column
  for r in range(len(grid)):
    for c in range(len(grid[0])):
      # If string in that position is water (i.e. "0"), move on
      if grid[r][c] == "0":
        continue
      # If string is land (i.e. "1")
      else:
        # Check if it has been included in an island already
        if checkLandConnection(land_tracker,grid,r,c):
          # Add to counter, found new island!
          islands += 1
        
        # Add neighbors to the tracker
        trackSelfAndNeighbors(land_tracker,grid,r,c)
  
  return islands

  # when I track self and neighbors, I should recursively move through the neighbors to track them and include a base case <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

# Optimization:
# The above solution is very complex and doesn't run on all edge cases. My sense is that it uses O(n^2) time because it hits all values in the matrix several times
# I think the best way to optimize this would be by using depth-first or breadth-first search across the matrix
# Best conceivable runtime: it seems like there may be a way to do this in O(n) time by reviewing each number only once

# Description:
# TBD


# Exercise 3: Climbing Stairs
# Link: (https://leetcode.com/problems/climbing-stairs/)
# Assumptions: it takes n individual steps to the top, you can only climb by 1 or 2 steps, max 45 steps
# Examples walk through ✅
# Custom examples (edges):
  # n = 4 => 5 (1 + 1 + 1 + 1, 2 + 1 + 1, 1 + 2 + 1, 1 + 1 + 2, 2 + 2)
  # n = 5 => 8 (1 + 1 + 1 + 1 + 1, 2 + 1 + 1 + 1, 1 + 2 + 1 + 1, 1 + 1 + 2 + 1, 1 + 1 + 1 + 2, 2 + 2 + 1, 1 + 2 + 2, 2 + 1 + 2)
  # Exhibits fibonacci sequence
# Function signature: def climbStairs(n: int) -> int:
# IN: number of steps integer / OUT: number of combinations integer
def climbStairs(n):
  print(n)
  # Set a base case: there's 1 way to climb 1 stair and 0 ways to climb 0 stairs
  # Then there's 2 ways to climb 2 stairs
  # And there's 3 ways to climb 3 stairs
  # And there's 5 ways to climb 4 stairs

  # Set a numberOfWaysPrev counter at 0:
  # Set a numberOfWaysCurr counter at 1:

  # Set a stairsNumber variable at 1:

  # While stairsNumber is less than n:
    # temp = numberOfWaysCurr
    # numberOfWaysCurr = numberOfWaysCurr + numberOfWaysPrev
    # numberOfWaysPrev = temp
    # stairsNumber += 1
  
  # return numberOfWaysCurr

  # Problem exhibits fibonacci sequence at n + 1:
  #                 n = 0, f = 0
  # 1 -> 1 (0 + 1)  n = 1, f = 1
  # 2 -> 2 (1 + 1)  n = 2, f = 1
  # 3 -> 3 (2 + 1)  n = 3, f = 2
  # 4 -> 5 (3 + 2)  n = 4, f = 3
  # 5 -> 8 (5 + 3)  n = 5, f = 5
  # 6 -> 13 (8 + 5) n = 6, f = 8

  # Optimization:
  # Time Complexity: This solution cycles through n time so it's O(n)
  # Space Complexity: This is O(1) since we always store the same amount of information regardless of how large n grows
  # Best Conceivable Runtime: O(n) because we will need to iterate over all the steps at least once
  # Description:
  # Use a previous and current point set at 0 and 1 to start with
  # Then iterate with a while loop that climbs the stairs one by one
  # As the loop climbs, it increments the number of ways to climb by the current number of ways plus the previous number of ways


# Exercise 4: Merge Intervals
# Link: (https://leetcode.com/problems/merge-intervals/)
# Assumptions: intervals are inclusive, contain two integers, 0 and positive integers only, start can equal end
# Examples walk through ✅
# Custom examples (edges): 
  # intervals = [[0,1],[2,3],[4,5],[5,10]] => [[0,1],[2,3],[4,10]]
  # intervals = [[0,0],[0,0],[1,1],[1,5]] => [[0,0],[1,5]]
# Function signature: def merge(intervals: List[List[int]]) -> List[List[int]]:
# IN: intervals list (i.e. list of lists with two ints each) / OUT: consolidated list of lists
def merge(intervals):
  print(intervals)
# First pseudocode brainstorm:
  # Cycle through each pair
  # Loop through a pair of intervals for length - 1 times:
    # First Loop:
      # first interval:   start_1 and end_1
      # second interval:  start_2 and end_2
      # If end_1 >= start_2:
        # Create a new array replacing first interval and second interval with updated interval: start_1, end_2
    # Second Loop:
      # first interval (updated interval):  start_1 and end_1
      # second interval:                    start_2 and end_2
      # If end_1 >= start_2:
        # Create a new array replacing first interval and second interval with updated interval: start_1, end_2
      # Else:
        # first interval: second interval
        # second interval: third interval
  
  # Second pseudocode brainstorm:
  # Sort intervals
  intervals.sort()
  # first = 0
  first = 0

  # While loop: while first < len(intervals) - 1:  --> while first interval index is less than the length of the intervals list minus one
  while first < len(intervals) - 1:
    # first_interval = intervals[first]
    first_interval = intervals[first]
    # second_interval = intervals[first + 1]
    second_interval = intervals[first + 1]
    # if first_interval[1] >= second_interval[0]:
    if first_interval[1] >= second_interval[0]:
      # intervals[first:first + 2] = [[first_interval[0], second_interval[1]]] -> note that this doesn't take into account instances where the intervals are in different order, which is why the code below is required
      intervals[first:first + 2] = [[min(first_interval[0], second_interval[0]), max(first_interval[1], second_interval[1])]]
    # else:
    else:
      # first += 1
      first += 1
    # break if len(intervals) == 1
    break if len(intervals) == 1
  
  # return intervals
  return intervals

  # Optimization:
  # Time Complexity: The while loop alone would make this an O(n) process. Sorting adds a multiple to that. Merging any interval inside the while loop causes the intervals array to be rebuilt which could be O(n) -> O(n^2)
  # Space Complexity: O(n) because we have keep track of intervals while we change it, otherwise it's O(1)
  # Best Conceivable Runtime: I think there's a way to do this in O(n) with dynamic arrays
  # Description:
  # Sort the intervals array
  # Set a first variable at 0
  # Do a while loop that cycles through each interval and compares it to the next interval
  # If the numbers overlap, merge the intervals, otherwise go to the next comparison
  # If the length of intervals reaches 1, break out of the loop, otherwise keep going until reaching the second to last item
  # return intervals
  


# Exercise 5: Max Binary Tree Depth
# Link: (https://leetcode.com/problems/maximum-depth-of-binary-tree/)
# Assumptions: root of binary tree has value, left, and right pointers; value can be 0 and positive integers, root counts as 1 depth
# Examples walk through ✅
# Custom examples (edges): 
  # root = [3,9,20,null,null,15,7] => 3
  # root = [1,3,5,null,2,15,7,6,null] => 4
# Function signature: def maxDepth(root: TreeNode) -> int:
# IN: binary tree root / OUT: max depth of the binary tree
def maxDepth(root):
  print(root)

  # Establish base case:
  # if root is null: return 0

  # Establish a counter variable that accounts for root depth of 1 -> counter = 1
  # Set a left_depth variable equal to this function to recursively explore the left node
  # Set a right_depth variable equal to this function to recursively explore the right node

  # Return counter + the max of left_depth and right_depth
  if root is None:
    return 0

  counter = 1
  left_depth = maxDepth(root.left)
  right_depth = maxDepth(root.right)

  return counter + max(left_depth, right_depth)

  # Optimization:
  # Time Complexity: This solution goes through each node once so it's O(n)
  # Space Complexity: Because we use recursion, this solution requires O(n) memory (i.e. technically depth/2 since the stack only grows fully to one side before returning)
  # Best Conceivable Runtime: O(n) because we will need to go to each node at least once to determine depth
  # Description:
  # If the node is empty, return a 0 for no depth
  # Otherwise, count the node depth as 1, then count all the nodes to its left and right in the same way
  # Finally, return the counter (i.e. the root node's depth of 1) plus the deepest branch, either left or right


# Exercise 6: Linked List Cycles
# Link: (https://leetcode.com/problems/linked-list-cycle/)
# Assumptions 1: values are only used once in the list and are effectively IDs -- wrong assumption, list is made up of nodes with val and next properties
# Assumptions 2: values can be used more than once in the list
# Examples walk through ✅
# Custom examples (edges): 
  # head = [1,2,3] => -1
  # head = [1,2,3,1] => 0
  # head = [1,2,3,3] => 2
# Function signature: def hasCycle(head: ListNode) -> bool:
# IN: head of linked list / OUT: true if linked list has a cycle else false
def hasCycle(head):
  # Create a hash table
  tracker = {}
  # Add head.val to the hash table
  tracker[head.val] = head
  # Make variable cur = head
  cur = head
  # Create while loop on cur.next is not None
  while cur.next is not None:
    # If cur.next.val is in the hash table and it's pointing to the node seen, return True
    if cur.next.val in tracker and tracker[cur.next.val] = cur.next:
      return True
    # Otherwise add cur.next to the hash table and cur = cur.next
    else:
      tracker[cur.next.val] = cur.next
      cur = cur.next

  # After the loop, return False
  return False

  # Optimization:
  # Time Complexity: O(n) because we view each linked item once
  # Space Complexity: O(n) because we use a hash table to track the items already seen
  # Best Conceivable Runtime: In order to determine a cycle, we'll have to view each item once in the worst case so O(n)
  # Description:
  # Add the head node to the tracker
  # Loop through all nodes
  # If we come across a node we've seen (i.e. the value is in the keys of tracker, and the value of that key is the node object), return True
  # If we finish looping (i.e. get to a None), then return False


# Exercise 7: Buy and Sell Stock
# Link: (https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)
# Assumptions: prices are 0 or positive integers, every integer represents a snapshot price for the day and the only opportunity to buy or sell, max profit is the biggest difference between and sell, you only buy and sell once
# Examples walk through ✅
# Custom examples (edges): 
  # [5,4,3,1] => 0
  # [2,4,3,1] => 2
  # [5,1,1,6] => 5
# Function signature: def maxProfit(prices: List[int]) -> int:
# IN: array of integers representing prices / OUT: max profit from buying one day and selling any other day
def maxProfit(prices):
  print(prices)

# Example:
# Input: prices = [7,1,5,3,6,4]
# Output: 5

# Input: prices = [7,4,5,3,6,1]
# Output: 3

# Input: prices = [7,5,5,3,3,2]
# Output: 0

  # Brute Force:
  # Set a variable profit = 0
  profit = 0

  # Loop through all prices in price array (price_a):
  for i in range(0, len(prices) - 1): # 0 -> 5 exclusive (i.e. 4)
    # Loop through all prices to the right of the selected price (price_b):
    for j in range(i + 1, len(prices)): # i + 1 (i.e. 1 to the right) -> 6 exclusive (i.e. 5)
      # profit = max(profit, price_b - price_a)
      profit = max(profit, prices[j] - prices[i])
  
  # Return profit
  return profit

  # Another approach:
  # Set variable lowest = prices[0]
  lowest = prices[0]
  # Set variable profit = 0
  profit = 0

  # Loop starting with index 1 (i.e. second price)
  for i in range(1, len(prices)):
    # Is price lower than lowest?
      # Yes: set lowest to price
      # No: check max(profit, price - lowest)
    if prices[i] < lowest:
      lowest = prices[i]
    else:
      profit = max(profit, prices[i] - lowest)
  
  # Return profit
  return profit

  # Optimization:
  # Time Complexity: O(n) because we'll need to look at all prices before we can be sure we have the max profit
  # Space Complexity: O(1) because we only track the variables profit and lowest in memory
  # Best Conceivable Runtime: O(n)
  # Description:
  # Set the lowest price variable to the first price
  # Set a profit variable to 0
  # Loop through the prices list starting with the second price
  # If we run into a price lower than lowest, update the lowest variable --> now look for a higher profit to the right of that lowest price
  # If the price is not lower than lowest, calculate the profit from buying at lowest to current price
  # If that profit is greater than the previously highest profit, update profit
  # Return the profit
