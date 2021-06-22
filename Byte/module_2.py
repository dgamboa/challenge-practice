# Notes:
# 1. Understand the problem [3-5 minutes]
# 2. Find a brute force solution [5 minutes]
# 3. Optimize your solution [15 minutes]
# 4. Code your solution [15 minutes]
# 5. Test your solution [5 minutes]

# Day 1,2,3 ****************************************************************** #
# Focus Day 1: understand the problem **************************************** #
# Focus Day 2, 3: brute force solutions ************************************** #

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
    for start in range(len(nums) - size + 1): # -> includes start at 0, 1, 3; 0, 1; 0
      # Create the subarray with start and start + size
      subarr = nums[start : start + size]
      # Sum the subarray
      sub_sum = sum(subarr)
      # Track the max sum so far
      max_tracker = max(max_tracker, sub_sum)
  
  return max_tracker

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
  print(n)

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


# Exercise 5: Max Binary Tree Depth
# Link: (https://leetcode.com/problems/maximum-depth-of-binary-tree/)
# Assumptions: root of binary tree has value, left, and right pointers; value is 0 and positive integers, root counts as 1 depth
# Examples walk through ✅
# Custom examples (edges): 
  # root = [3,9,20,null,null,15,7] => 3
  # root = [1,3,5,null,2,15,7,6,null] => 4
# Function signature: def maxDepth(root: TreeNode) -> int:
# IN: binary tree root / OUT: max depth of the binary tree
def maxDepth(root):
  print(root)


# Exercise 6: Linked List Cycles
# Link: (https://leetcode.com/problems/linked-list-cycle/)
# Assumptions: values are only used once in the list and are effectively IDs, list is made up of nodes with val and next properties
# Examples walk through ✅
# Custom examples (edges): 
  # head = [1,2,3] => -1
  # head = [1,2,3,1] => 0
  # head = [1,2,3,3] => 2
# Function signature: def hasCycle(head: ListNode) -> bool:
# IN: head of linked list / OUT: true if linked list has a cycle else false
def hasCycle(head):
  print(head)

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
