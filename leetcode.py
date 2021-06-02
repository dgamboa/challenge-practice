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

# Other Solution from Discussion
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        m = n = -math.inf
        for num in nums:
            if num >= m:
                n = m
                m = num
            elif num > n:
                n = num
        return (m - 1) * (n - 1)

# ******************************************************************************************************************** #
# *************************************************** Exercise ******************************************************* #
# ******************************************************************************************************************** #
# A school is trying to take an annual photo of all the students. The students are asked to stand in a single file line in non-decreasing order by height. Let this ordering be represented by the integer array expected where expected[i] is the expected height of the ith student in line.

# You are given an integer array heights representing the current order that the students are standing in. Each heights[i] is the height of the ith student in line (0-indexed).

# Return the number of indices where heights[i] != expected[i].

 

# Example 1:

# Input: heights = [1,1,4,2,1,3]
# Output: 3
# Explanation: 
# heights:  [1,1,4,2,1,3]
# expected: [1,1,1,2,3,4]
# Indices 2, 4, and 5 do not match.

# Initial Solution
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        counter = 0
        ordered = sorted(heights)
        
        for i,v in enumerate(heights):
            if v != ordered[i]:
                counter += 1
        
        return counter

# Other Solution from Discussion
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        cnt = collections.Counter(heights)
        i, ans = 1, 0
        for h in heights:
            while cnt[i] == 0: # non-exist height.
                i += 1         # skip it.
            if i != h:         # mismatch found.
                ans += 1       # increase by 1.
            cnt[i] -= 1        # remove the one that has been used.
        return ans

# ******************************************************************************************************************** #
# *************************************************** Exercise ******************************************************* #
# ******************************************************************************************************************** #
# Given two string arrays word1 and word2, return true if the two arrays represent the same string, and false otherwise.

# A string is represented by an array if the array elements concatenated in order forms the string.

 

# Example 1:

# Input: word1 = ["ab", "c"], word2 = ["a", "bc"]
# Output: true
# Explanation:
# word1 represents string "ab" + "c" -> "abc"
# word2 represents string "a" + "bc" -> "abc"
# The strings are the same, so return true.

# Initial Solution
class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        return ''.join(word1) == ''.join(word2)

# ******************************************************************************************************************** #
# *************************************************** Exercise ******************************************************* #
# ******************************************************************************************************************** #
# A sentence is a list of words that are separated by a single space with no leading or trailing spaces. Each word consists of lowercase and uppercase English letters.

# A sentence can be shuffled by appending the 1-indexed word position to each word then rearranging the words in the sentence.

# For example, the sentence "This is a sentence" can be shuffled as "sentence4 a3 is2 This1" or "is2 sentence4 This1 a3".
# Given a shuffled sentence s containing no more than 9 words, reconstruct and return the original sentence.

 

# Example 1:

# Input: s = "is2 sentence4 This1 a3"
# Output: "This is a sentence"
# Explanation: Sort the words in s to their original positions "This1 is2 a3 sentence4", then remove the numbers.

# Initial Solution
class Solution:
    def sortSentence(self, s: str) -> str:
        s_lst = s.split(" ")
        ordered = sorted(s_lst, key=lambda x: int(x[-1]))
        
        ans = []
        for v in ordered:
            ans.append(v[:-1])
        return " ".join(ans)

# Second Solution
class Solution:
    def sortSentence(self, s: str) -> str:
        s_lst = s.split(" ")
        ordered = sorted(s_lst, key=lambda x: int(x[-1]))
        
        ans = ""
        for v in ordered:
            ans += (v[:-1] + " ")
        return ans[:-1]

# Third Solution
class Solution:
    def sortSentence(self, s: str) -> str:
        return " ".join([i[:-1] for i in sorted(s.split(" "), key = lambda x: x[-1])])



# ******************************************************************************************************************** #
# *************************************************** Exercise ******************************************************* #
# ******************************************************************************************************************** #
# Balanced strings are those that have an equal quantity of 'L' and 'R' characters.

# Given a balanced string s, split it in the maximum amount of balanced strings.

# Return the maximum amount of split balanced strings.

 

# Example 1:

# Input: s = "RLRRLLRLRL"
# Output: 4
# Explanation: s can be split into "RL", "RRLL", "RL", "RL", each substring contains same number of 'L' and 'R'.

# Initial Submission
class Solution:
    def balancedStringSplit(self, s: str) -> int:
        counter = R_count = L_count = 0
        
        for c in s:
            if c == "R": R_count += 1 
            if c == "L": L_count += 1
            if R_count == L_count: counter += 1

        return counter

# Discussion Submission
class Solution:
    def balancedStringSplit(self, s: str) -> int:
        ans = prefix = 0
        for c in s: 
            prefix += 1 if c == "R" else -1
            if not prefix: ans += 1
        return ans 
