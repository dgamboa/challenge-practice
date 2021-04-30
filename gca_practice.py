# ********PROBLEM************************************************************* #
# GCA Practice Problem

# You are given two integer arrays a, b and one array of distinct integers c. Your task is to check whether b is the longest contiguous subarray of a consisting only of elements from c, i.e.

# Each of the elements of b belong to c,
# a contains b as a contiguous subarray,
# b is the longest of the contiguous subarrays of a which satisfy the first two conditions.
# Return true if all the above conditions are met, and false otherwise.

# NOTE: If there is a tie for the longest contiguous subarrays of a consisting of elements from c, the answer is still considered true if b is one of these longest contiguous subarrays.

# Example

# For a = [1, 1, 5, 1, 2], b = [1, 2], and c = [2, 1], the output should be longestSubarrayCheck(a, b, c) = true.

# All three conditions are met:

# All of the elements of b belong to c,
# a contains b as a contiguous subarray (a[3..4] = b),
# b is the longest of these contiguous subarrays. To prove this, let's look at all the contiguous subarrays of length greater than 2:
# a[0..2] = [1, 1, 5] contains 5, which doesn't belong to c.
# a[0..3] = [1, 1, 5, 1] contains 5, which doesn't belong to c.
# a[0..4] = [1, 1, 5, 1, 2] contains 5, which doesn't belong to c.
# a[1..3] = [1, 5, 1] contains 5, which doesn't belong to c.
# a[1..4] = [1, 5, 1, 2] contains 5, which doesn't belong to c.
# a[2..4] = [5, 1, 2] contains 5, which doesn't belong to c.
# Therefore b is the longest contiguous subarray of a consisting only of elements from c, so the answer is true.

# For a = [1, 2, 3, 6, 1, 1, 1], b = [1, 2, 3], and c = [2, 1], the output should be longestSubarrayCheck(a, b, c) = false.

# Although b is a contiguous subarray of a, it contains the element b[2] = 3 which does not appear in c, therefore it does not meet the conditions. So the answer is false.

# For a = [1, 2, 2, 3, 2, 1, 3], b = [3, 2, 1, 3], and c = [2, 1, 3], the output should be longestSubarrayCheck(a, b, c) = false.

# All of the elements of a belong to c, and b.length < a.length, so b couldn't possibly be the longest contiguous subarray consisting of elements from c. So, the answer is false.

def longestSubarrayCheck(a, b, c):
    for v in b:
        if v not in c:
            return False
    
    tracker = 0
    for i in range(len(a) - len(b) + 2):
        if b == a[i:len(b) + i]:
            tracker += 1
            break
    
    if tracker == 0:
        return False
    
    return False
    
    # j = len(b) + 1
    # y = len(b) + 1
    # while j > 0:
    #     for i in range(len(b) + 1, len(a) + 1):
    #         for v in a[i:i + y]:
    #             if v not in c:
    #                 continue
    #     j -= 1
    #     y += i
        
