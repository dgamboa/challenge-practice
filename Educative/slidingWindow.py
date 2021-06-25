# **************************************************************************** #
# ************** Day 1 ******************************************************* #
# **************************************************************************** #

# Given an array of positive numbers and a positive number ‘k,’ find the maximum sum of any contiguous subarray of size ‘k’.

# Time complexity O(n * k):
def max_sub_array_of_size_k(k, arr):
  _max = 0

  for i in range(len(arr) - k + 1):
      _max = max(_max, sum(arr[i:k + i]))
  
  return _max

# Time complexity O(n):
def max_sub_array_of_size_k(k, arr):
  _max = 0
  _sum = 0
  start = 0

  for i in range(len(arr)):
    _sum += arr[i]

    if i >= k - 1:
      _max = max(_max, _sum)
      _sum -= arr[start]
      start += 1
  
  return _max

# Given an array of positive numbers and a positive number ‘S,’ find the length of the smallest contiguous subarray whose sum is greater than or equal to ‘S’. Return 0 if no such subarray exists.

# Brute Force, time complexity O(n^2):
def smallest_subarray_with_given_sum(s, arr):
  for i in range(1, len(arr)):
    for j in range(len(arr) - i + 1):
      if sum(arr[j:j + i]) >= s:
        return i # Because we're exploring subarrays from length 1 upward, we'll run into the shortest subarray that sums to s along the way

  return 0

# Time complexity O(n) with sliding window:
import math

def smallest_subarray_with_given_sum(s, arr):
  _sum, start = 0, 0
  _len = math.inf

  for end in range(len(arr)):
    _sum += arr[end]

    while _sum >= s:
      _len = min(_len, end - start + 1)
      _sum -= arr[start]
      start += 1
  
  return _len if _len != math.inf else 0
