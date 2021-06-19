# **************************************************************************** #
# ************** Day 1 ******************************************************* #
# **************************************************************************** #

# Given an array of positive numbers and a positive number ‘k,’ find the maximum sum of any contiguous subarray of size ‘k’.

def max_sub_array_of_size_k(k, arr):
  _max = 0
  _sum = 0
  start = 0

  for i in range(len(arr)):
    _sum += arr[i]

    print(_sum)

    if i >= k - 1:
      _max = max(_max, _sum)
      _sum -= arr[start]
      start += 1
  
  return _max
