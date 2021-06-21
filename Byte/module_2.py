# Notes:
# 1. Understand the problem [3-5 minutes]
# 2. Find a brute force solution [5 minutes]
# 3. Optimize your solution [15 minutes]
# 4. Code your solution [15 minutes]
# 5. Test your solution [5 minutes]

# Day 1 ********************************************************************** #
# Focus: understand the problem ********************************************** #
# **************************************************************************** #

# Exercise 1: Maximum Sum Subarray
# Link: (https://leetcode.com/problems/maximum-subarray/)
# Assumptions: all items are integers, can be positive / negative, no empty subarray 
# Examples walk through ✅
# Custom examples (edges): [7,-8,9] => 9
# Function signature: def maxSubArray(nums: List[int]) -> int:
# IN: array of integers / OUT: integer with max sum
def maxSubArray(nums):
  print(nums)


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
