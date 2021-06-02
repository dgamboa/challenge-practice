# ******************************************************************************************************************** #
# *************************************************** Exercise ******************************************************* #
# ******************************************************************************************************************** #
# There is a biker going on a road trip. The road trip consists of n + 1 points at different altitudes. The biker starts his trip on point 0 with altitude equal 0.

# You are given an integer array gain of length n where gain[i] is the net gain in altitude between points i​​​​​​ and i + 1 for all (0 <= i < n). Return the highest altitude of a point.

# Example 1:

# Input: gain = [-5,1,5,0,-7]
# Output: 1
# Explanation: The altitudes are [0,-5,-4,1,1,-6]. The highest is 1.
# Example 2:

# Input: gain = [-4,-3,-2,-1,4,3,2]
# Output: 0
# Explanation: The altitudes are [0,-4,-7,-9,-10,-6,-3,-1]. The highest is 0.

# Initial Solution
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        cur_max = 0
        prev = 0
        
        for v in gain:
            cur_alt = prev + v
            cur_max = max(cur_max, cur_alt)
            prev = cur_alt
        
        return cur_max

# One-Line Solution from Comments
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        return max(0, max(accumulate(gain)))
        # Slightly slower than the above, same memory usage

# ******************************************************************************************************************** #
# *************************************************** Exercise ******************************************************* #
# ******************************************************************************************************************** #
# Given the array of integers nums, you will choose two different indices i and j of that array. Return the maximum value of (nums[i]-1)*(nums[j]-1).
 

# Example 1:

# Input: nums = [3,4,5,2]
# Output: 12 
# Explanation: If you choose the indices i=1 and j=2 (indexed from 0), you will get the maximum value, that is, (nums[1]-1)*(nums[2]-1) = (4-1)*(5-1) = 3*4 = 12. 
# Example 2:

# Input: nums = [1,5,4,5]
# Output: 16
# Explanation: Choosing the indices i=1 and j=3 (indexed from 0), you will get the maximum value of (5-1)*(5-1) = 16.
# Example 3:

# Input: nums = [3,7]
# Output: 12

# Initial Solution
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ordered = sorted(nums, reverse=True)
        return (ordered[0] - 1) * (ordered[1] - 1)

# Other Solution
