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
        

# **************************************************************************** #
# May 4 GCA Practice
# **************************************************************************** #
# #1
# Given an integer n and an array a of length n, your task is to apply the following mutation to a:

# Array a mutates into a new array b of length n.
# For each i from 0 to n - 1, b[i] = a[i - 1] + a[i] + a[i + 1].
# If some element in the sum a[i - 1] + a[i] + a[i + 1] does not exist, it should be set to 0. For example, b[0] should be equal to 0 + a[0] + a[1].
def mutateTheArray(n, a):
    if n == 1:
        return a
    
    b = []
    
    for i in range(n):
        if i == 0:
            x, y, z = 0, a[i], a[i + 1]
        elif i == n - 1:
            x, y, z = a[i - 1], a[i], 0
        else:
            x, y, z = a[i - 1], a[i], a[i + 1]
            
        b.append(x + y + z)
    
    return b
            


# #2
# Given two strings s and t, both consisting of lowercase English letters and digits, your task is to calculate how many ways exactly one digit could be removed from one of the strings so that s is lexicographically smaller than t after the removal. Note that we are removing only a single instance of a single digit, rather than all instances (eg: removing 1 from the string a11b1c could result in a1b1c or a11bc, but not abc).

# Also note that digits are considered lexicographically smaller than letters.

# Example

# For s = "ab12c" and t = "1zz456", the output should be removeOneDigit(s, t) = 1.
def removeOneDigit(s, t):
    counter = 0
    
    for i, c in enumerate(s):
        if ord(c) < 97:
            c = list(s)
            c.pop(i)
            if "".join(c) < t:
                counter += 1
    
    for i, c in enumerate(t):
        if ord(c) < 97:
            c = list(t)
            c.pop(i)
            if "".join(c) > s:
                counter += 1
    
    return counter

# #3
# You are implementing your own programming language and you've decided to add support for merging strings. A typical merge function would take two strings s1 and s2, and return the lexicographically smallest result that can be obtained by placing the symbols of s2 between the symbols of s1 in such a way that maintains the relative order of the characters in each string.

# For example, if s1 = "super" and s2 = "tower", the result should be merge(s1, s2) = "stouperwer".

# You'd like to make your language more unique, so for your merge function, instead of comparing the characters in the usual lexicographical order, you'll compare them based on how many times they occur in their respective initial strings (fewer occurrences means the character is considered smaller). If the number of occurrences are equal, then the characters should be compared in the usual lexicographical way. If both number of occurences and characters are equal, you should take the characters from the first string to the result. Note that occurrences in the initial strings are compared - they do not change over the merge process.

# Given two strings s1 and s2, return the result of the special merge function you are implementing.

# Example 

# For s1 = "dce" and s2 = "cccbd", the output should be
# mergeStrings(s1, s2) = "dcecccbd".
# All symbols from s1 goes first, because all of them have only 1 occurrence in s1 and c has 3 occurrences in s2.
    def mergeStrings(s1, s2):
    s1_ref = {}
    s2_ref = {}
    
    for c in s1:
        if c in s1_ref:
            s1_ref[c] += 1
        else: 
            s1_ref[c] = 1
            
    for c in s2:
        if c in s2_ref:
            s2_ref[c] += 1
        else: 
            s2_ref[c] = 1
    
    output = ""
    n_s1 = 0
    n_s2 = 0
    
    for i in range(len(s1) + len(s2)):
        s1_c = s1_ref[s1[n_s1]]
        s2_c = s2_ref[s2[n_s2]]
        print(output)
        print(n_s1)
        
        if n_s1 > len(s1) - 1:
            output += s2[n_s2:]
            break
        
        if n_s2 > len(s2) - 1:
            output += s1[n_s1:]
            break
        
        if s1_c < s2_c:
            output += s1[n_s1]
            n_s1 += 1
        elif s2_c < s1_c:
            output += s2[n_s2]
            n_s2 += 1
        elif s1[n_s1] < s2[n_s2]:
            output += s1[n_s1]
            n_s1 += 1
        elif s2[n_s2] < s1[n_s1]:
            output += s2[n_s2]
            n_s2 += 1
        else:
            output += s1[n_s1]
            n_s1 += 1
    
    return output

# #4
# Problem Name: countOnSubarrays
# It asked to count the number of times a number appeared in a subarray based
# on a queries array
# a = [1,2,1,3,1,2,1]
# queries = [
#   [1,3,1], --> find number of 1's between index 1 and 3 inclusive => 1
#   [0,4,2], => 1
#   [5,6,1]  => 1
# ]
# Returns 3

# My solution was something like:
# count = 0
# Loop through the queries array
#   l, r, x = cur
#   count += a[l:r+1].count(x)
# return count

# This didn't work fast enough for larger inputs

# I then refactored it using a dictionary, which worked for one additional test
# But it still didn't pass all the hidden tests (3 or 4 more)

# Best score: 233/300




# 2
# You are given three integers in the form of strings: firstnum, secondnum, and thirdnum. Your task is to check whether it is possible to erase at most one digit from firstnum, so that the resulting string contains at least one digit, has no leading zeros and the value of thirdnum is equal to the sum of the values of firstnum and secondnum.

# Return true if it's possible, otherwise return false.

# Note: All three strings are provided without leading zeros.

# Example

# For firstnum = "10534", secondnum = "67", and thirdnum = "1120", the output should be eraseOneDigit(firstnum, secondnum, thirdnum) = true.

# By erasing the 5th digit of firstnum, the result is 1053, and 1053 + 67 = 1120. So the answer is true.

# For firstnum = "10000", secondnum = "67", and thirdnum = "1120", the output should be eraseOneDigit(firstnum, secondnum, thirdnum) = false.

# The only possible modified values of firstnum would be 10000 (nothing was deleted), 0000 (first digit was deleted), and 1000 (any zero was deleted); none of which would produce the required sum, so the answer is false.

# For firstnum = "1067", secondnum = "33", and thirdnum = "100", the output should be eraseOneDigit(firstnum, secondnum, thirdnum) = false.

# We could delete the first digit of firstnum, resulting in 067 (and 67 + 33 = 100), but since in this case new firstnum value has a leading zero, it's considered invalid. So the answer is false.

# For firstnum = "153", secondnum = "153", and thirdnum = "306", the output should be eraseOneDigit(firstnum, secondnum, thirdnum) = true.

# Because 153 + 153 = 306, there's no need to delete a digit from firstnum, and the result is true.

def eraseOneDigit(firstnum, secondnum, thirdnum):
    for i in range(len(firstnum)):
        new = firstnum[:i] + firstnum[i+1:]
        if (
            int(new) + int(secondnum) == int(thirdnum) and
            len(new) == len(str(int(new)))
            ):
            return True
    
    if int(firstnum) + int(secondnum) == int(thirdnum):
        return True
    
    return False


# 3
# You are given a matrix of integers matrix of size n × m and a list of queries queries. The given matrix is colored in black and white in a checkerboard style - the top left corner is colored white and any two side-neighboring cells have opposite colors.

# Each query is represented as a pair of indices (i, j). For each query, perform the following operations:

# Select the ith-smallest value among the black cells. In case of a tie, select the one with the lower row number. If there is still a tie, select the one with the lower column number;
# Select the jth-smallest white cell using the same process;
# Find the average value of these two cells;
# If the average value is a whole integer, replace both of the selected cells with the found average value;
# Otherwise, replace the cell of the greater value with the average rounded up to the nearest integer, and replace the cell of the smaller value with the average rounded down to the nearest integer.
# Your task is to return the resulting matrix after processing all the queries.



# 4
# You are given an array of integers arr. Your task is to count the number of contiguous subarrays, such that each element of the subarray appears at least twice.

# Example

# For arr = [0, 0, 0], the output should be duplicatesOnSegment(arr) = 3.

# There are 3 subarrays that satisfy the criteria of containing only duplicate elements:

# arr[0..1] = [0, 0]
# arr[1..2] = [0, 0]
# arr[0..2] = [0, 0, 0]
# For arr = [1, 2, 1, 2, 3], the output should be duplicatesOnSegment(arr) = 1.

# There is only 1 applicable subarray: arr[0..3] = [1, 2, 1, 2].
def duplicatesOnSegment(a):
  if not a or len(a) == 0:
    return 0

  counter = 0
  for s in range(len(a) - 1): # O(n)
    for e in range(s + 1, len(a)): # O(n)
      sub = a[s:e + 1] # O(n)
      unique = 0
      dict = {}
      for v in sub: # O(n)
        if v in dict:
          dict[v] += 1
          unique -= 1
        else:
          dict[v] = 1
          unique += 1
      if unique <= 0:
        counter += 1
  
  return counter
    
  
# Time Complexity: # O(n^3)





# 1
# You are given an array of integers a and two integers l and r. You task is to calculate a boolean array b, where b[i] = true if there exists an integer x, such that a[i] = (i + 1) * x and l ≤ x ≤ r. Otherwise, b[i] should be set to false.

# Example

# For a = [8, 5, 6, 16, 5], l = 1, and r = 3, the output should be boundedRatio(a, l, r) = [false, false, true, false, true].

# For a[0] = 8, we need to find a value of x such that 1 * x = 8, but the only value that would work is x = 8 which doesn't satisfy the boundaries 1 ≤ x ≤ 3, so b[0] = false.
# For a[1] = 5, we need to find a value of x such that 2 * x = 5, but there is no integer value that would satisfy this equation, so b[1] = false.
# For a[2] = 6, we can choose x = 2 because 3 * 2 = 6 and 1 ≤ 2 ≤ 3, so b[2] = true.
# For a[3] = 16, there is no an integer 1 ≤ x ≤ 3, such that 4 * x = 16, so b[3] = false.
# For a[4] = 5, we can choose x = 1 because 5 * 1 = 5 and 1 ≤ 1 ≤ 3, so b[4] = true.
def boundedRatio(a, l, r):
    b = []
    for i in range(len(a)):
        if a[i] % (i + 1) != 0:
            b.append(False)
            continue
            
        x = a[i] / (i + 1)
        print(x)
        if x >= l and x <= r:
            b.append(True)
        else:
            b.append(False)
    return b




# 2
# You are given a string s. Your task is to count the number of ways of splitting s into three non-empty parts a, b and c (s = a + b + c) in such a way that a + b, b + c and c + a are all different strings.

# NOTE: + refers to string concatenation.

# Example

# For s = "xzxzx", the output should be countWaysToSplit(s) = 5.

# Consider all the ways to split s into three non-empty parts:

# If a = "x", b = "z" and c = "xzx", then all a + b = "xz", b + c = "zxzx" and c + a = xzxx are different.
# If a = "x", b = "zx" and c = "zx", then all a + b = "xzx", b + c = "zxzx" and c + a = zxx are different.
# If a = "x", b = "zxz" and c = "x", then all a + b = "xzxz", b + c = "zxzx" and c + a = xx are different.
# If a = "xz", b = "x" and c = "zx", then a + b = b + c = "xzx". Hence, this split is not counted.
# If a = "xz", b = "xz" and c = "x", then all a + b = "xzxz", b + c = "xzx" and c + a = xxz are different.
# If a = "xzx", b = "z" and c = "x", then all a + b = "xzxz", b + c = "zx" and c + a = xxzx are different.
# Since there are five valid ways to split s, the answer is 5.
def countWaysToSplit(s):
    count = 0
    
    for i in range(1, len(s) - 1):
        for j in range(2, len(s)):
            a = s[:i]
            b = s[i:j]
            c = s[j:]
            
            if (
                len(a) != 0 and
                len(b) != 0 and
                len(c) != 0 and
                a + b != c + a and
                a + b != b + c and
                b + c != c + a
            ):
                count += 1
    
    return count


# 4
# Given an array of integers a, consider all its contiguous subarrays of length m. Calculate the number of such subarrays, which contain a pair of integers in it with sum greater than or equal to k.

# More formally, given the array a, your task is to count the number of such indices 0 ≤ i ≤ a.length - m such that a subarray [a[i], a[i + 1], ..., a[i + m - 1]] contains such pair (a[s], a[t]), such that:

# s ≠ t
# a[s] + a[t] ≥ k
# Example

# For a = [2, 4, 2, 7, 1, 6, 1, 1, 1], m = 4, and k = 8, the output should be segmentsWithSum(a, m, k) = 4.
# Let's consider all subarrays of length m = 4 and see which of them fit the description conditions:

# Subarray a[0..3] = [2, 4, 2, 7] contain a pair (a[0], a[3]) that have sum greater than or equal k: a[0] + a[3] = 2 + 7 + 9 ≥ 8. Note, that there are two more such pairs in the subarray: (a[1], a[3]) and (a[2], a[3]). Also note that there is a pair (a[3], a[3]) having sum 7 + 7 = 14 ≥ 8, but it shoudn't be taken into account, because it violates condition s ≠ t.
# Subarray a[1..4] = [4, 2, 7, 1] contains a pair (a[1], a[3]), having a[1] + a[3] = 4 + 7 = 11 ≥ 8. Note, that there is one more such pair in the subarray: (a[3], a[4]).
# Subarray a[2..5] = [2, 7, 1, 6] contains a pair (a[2], a[3]), having a[2] + a[3] = 2 + 7 = 9 ≥ 8. Note, that there are three more such pairs: (a[2], a[5]), (a[3], a[4]), and (a[3], a[5]).
# Subarray a[3..6] = [7, 1, 6, 1] contains a pair (a[3], a[4]) having the sum equal a[3] + a[4] = 7 + 1 = 8 ≥ 8. Note, that there is one more such pair in the subarray: (a[3], a[5]).
# Subarray a[4..7] = [1, 6, 1, 1] doesn't contain any pair having the sum greater than or equal to k = 8.
# Subarray a[5..8] = [6, 1, 1, 1] doesn't contain any pair having the sum greater than or equal to k = 8.
# Summary, there are 4 subarrays having a pair with sum greater than or equal to k = 8.

# For a = [2, 3, 3, 3, 4, 3, 2, 1, 2, 4], m = 2, and k = 7, the output should be segmentsWithSum(a, m, k) = 2.
# There are 2 subarrays satisfying the description conditions: a[3..4] = [3, 4] and a[4..5] = [4, 3].

def segmentsWithSum(a, m, k):
    counter = 0
    
    i = 0
    j = m
    for i in range(len(a) - m + 1):
        max_val = a[i]
        for v in a[i + 1:j]:
            # print(f"{max_val} + {v} >= {k} {max_val + v >= k}")
            if max_val + v >= k:
                counter += 1
                break
            elif v > max_val:
                max_val = v
        j += 1
    
    return counter

# This solution scored 243/300 (and I had it with 15min to spare)
# It wasn't performant on the hidden tests so there must be a more efficient way

# 1
# Let's say a triple (a, b, c) is a zigzag if either a < b > c or a > b < c.

# Given an array of integers numbers, your task is to check all the triples of its consecutive elements for being a zigzag. More formally, your task is to construct an array of length numbers.length - 2, where the ith element of the output array equals 1 if the triple (numbers[i], numbers[i + 1], numbers[i + 2]) is a zigzag, and 0 otherwise.

# Example

# For numbers = [1, 2, 1, 3, 4], the output should be isZigzag(numbers) = [1, 1, 0].

# (numbers[0], numbers[1], numbers[2]) = (1, 2, 1) is a zigzag, because 1 < 2 > 1;
# (numbers[1], numbers[2] , numbers[3]) = (2, 1, 3) is a zigzag, because 2 > 1 < 3;
# (numbers[2], numbers[3] , numbers[4]) = (1, 3, 4) is not a zigzag, because 1 < 3 < 4;
# For numbers = [1, 2, 3, 4], the output should be isZigzag(numbers) = [0, 0];

# Since all the elements of numbers are increasing, there are no zigzags.

# For numbers = [1000000000, 1000000000, 1000000000], the output should be isZigzag(numbers) = [0].

# Since all the elements of numbers are the same, there are no zigzags.
def isZigzag(numbers):
    arr = []
    
    for i in range(len(numbers) - 2):
        a, b, c = numbers[i], numbers[i + 1], numbers[i + 2]
        
        if a < b > c or a > b < c:
            arr.append(1)
        else:
            arr.append(0)
    
    return arr



# 2
# You are given an array of non-negative integers numbers. You are allowed to choose any number from this array and swap any two digits in it. If after the swap operation the number contains leading zeros, they can be omitted and not considered (eg: 010 will be considered just 10).

# Your task is to check whether it is possible to apply the swap operation at most once, so that the elements of the resulting array are strictly increasing.

# Example

# For numbers = [1, 5, 10, 20], the output should be makeIncreasing(numbers) = true.

# The initial array is already strictly increasing, so no actions are required.

# For numbers = [1, 3, 900, 10], the output should be makeIncreasing(numbers) = true.

# By choosing numbers[2] = 900 and swapping its first and third digits, the resulting number 009 is considered to be just 9. So the updated array will look like [1, 3, 9, 10], which is strictly increasing.

# For numbers = [13, 31, 30], the output should be makeIncreasing(numbers) = false.

# The initial array elements are not increasing.
# By swapping the digits of numbers[0] = 13, the array becomes [31, 31, 30] which is not strictly increasing;
# By swapping the digits of numbers[1] = 31, the array becomes [13, 13, 30] which is not strictly increasing;
# By swapping the digits of numbers[2] = 30, the array becomes [13, 31, 3] which is not strictly increasing;
# So, it's not possible to obtain a strictly increasing array, and the answer is false.
def compare(arr1, arr2):
    store = []
    
    for i in range(len(arr1)):
        if arr1[i] != arr2[i]:
            store.append(i)
    
    return store

def getOptions(str):
    store = []
    
    for i in range(len(str) - 1):
        store.append(int(str[i + 1:] + str[:i + 1]))
    
    return store

def check(i, arr):
    curr = str(arr[i])
    
    options = getOptions(curr)
    
    if i == 0:
        for v in options:
            if v < arr[i + 1]:
                return True
    elif i == len(arr) - 1:
        for v in options:
            if v > arr[i - 1]:
                return True
    else:
        for v in options:
            if v > arr[i - 1] and v < arr[i + 1]:
                return True
    
    return False

def makeIncreasing(numbers):
    b = sorted(numbers)
    
    store = compare(numbers, b)
    
    print(store)
    
    if len(store) > 2 and store[-1] - store[0] != len(store) - 1:
        return False
    if len(store) == 0:
        return True
        
    if check(store[0], numbers) or check(store[1], numbers):
        return True
    else:
        return False



# 4
# Given an array of positive integers a, your task is to calculate the sum of every possible a[i] ∘ a[j], where a[i] ∘ a[j] is the concatenation of the string representations of a[i] and a[j] respectively.

# Example

# For a = [10, 2], the output should be concatenationsSum(a) = 1344.

# a[0] ∘ a[0] = 10 ∘ 10 = 1010,
# a[0] ∘ a[1] = 10 ∘ 2 = 102,
# a[1] ∘ a[0] = 2 ∘ 10 = 210,
# a[1] ∘ a[1] = 2 ∘ 2 = 22.
# So the sum is equal to 1010 + 102 + 210 + 22 = 1344.

# For a = [8], the output should be concatenationsSum(a) = 88.

# There is only one number in a, and a[0] ∘ a[0] = 8 ∘ 8 = 88, so the answer is 88.

# For a = [1, 2, 3], the output should be concatenationsSum(a) = 198.

# a[0] ∘ a[0] = 1 ∘ 1 = 11,
# a[0] ∘ a[1] = 1 ∘ 2 = 12,
# a[0] ∘ a[2] = 1 ∘ 3 = 13,
# a[1] ∘ a[0] = 2 ∘ 1 = 21,
# a[1] ∘ a[1] = 2 ∘ 2 = 22,
# a[1] ∘ a[2] = 2 ∘ 3 = 23,
# a[2] ∘ a[0] = 3 ∘ 1 = 31,
# a[2] ∘ a[1] = 3 ∘ 2 = 32,
# a[2] ∘ a[2] = 3 ∘ 3 = 33.
# The total result is 11 + 12 + 13 + 21 + 22 + 23 + 31 + 32 + 33 = 198.


# ***************************************************************************** #
# Practice June 3
# ***************************************************************************** #

# 1
# You are given an array of integers a and two integers l and r. You task is to calculate a boolean array b, where b[i] = true if there exists an integer x, such that a[i] = (i + 1) * x and l ≤ x ≤ r. Otherwise, b[i] should be set to false.

# Example

# For a = [8, 5, 6, 16, 5], l = 1, and r = 3, the output should be boundedRatio(a, l, r) = [false, false, true, false, true].

# For a[0] = 8, we need to find a value of x such that 1 * x = 8, but the only value that would work is x = 8 which doesn't satisfy the boundaries 1 ≤ x ≤ 3, so b[0] = false.
# For a[1] = 5, we need to find a value of x such that 2 * x = 5, but there is no integer value that would satisfy this equation, so b[1] = false.
# For a[2] = 6, we can choose x = 2 because 3 * 2 = 6 and 1 ≤ 2 ≤ 3, so b[2] = true.
# For a[3] = 16, there is no an integer 1 ≤ x ≤ 3, such that 4 * x = 16, so b[3] = false.
# For a[4] = 5, we can choose x = 1 because 5 * 1 = 5 and 1 ≤ 1 ≤ 3, so b[4] = true.

def boundedRatio(a, l, r):
    b = []
    
    for i, v in enumerate(a):
        x = v / (i + 1)
        if int(x) == x and l <= x and x <= r:
            b.append(True)
        else:
            b.append(False)
    
    return b

# 2
# Given an array of integers a, your task is to calculate the digits that occur the most number of times in the array. Return the array of these digits in ascending order.

# Example

# For a = [25, 2, 3, 57, 38, 41], the output should be mostFrequentDigits(a) = [2, 3, 5].

# Here are the number of times each digit appears in the array:

# 0 -> 0
# 1 -> 1
# 2 -> 2
# 3 -> 2
# 4 -> 1
# 5 -> 2
# 6 -> 0
# 7 -> 1
# 8 -> 1
# The most number of times any number occurs in the array is 2, and the digits which appear 2 times are 2, 3 and 5. So the answer is [2, 3, 5].

def mostFrequentDigits(a):
    str1 = "".join(str(n) for n in a)
    
    store = {}
    max_count = 0
    ans = []
    
    for c in str1:
        if c in store:
            store[c] += 1
        else:
            store[c] = 1
        
        if store[c] > max_count:
            max_count = store[c]
            ans = [int(c)]
        elif store[c] == max_count:
            ans.append(int(c))
        
    return sorted(ans)

# 3
# Given a square matrix of positive integers a, your task is to sort the numbers in each of its diagonals parallel to the secondary diagonal. Each diagonal should contain the same set of numbers as before, but sorted in ascending order from the bottom-left to top-right.
# For

# a = [[1, 3, 9, 4],
#      [9, 5, 7, 7],
#      [3, 6, 9, 7],
#      [1, 2, 2, 2]]
# the output should be

# diagonalsSort(a) = [[1, 9, 9, 7],
#                     [3, 5, 6, 9],
#                     [3, 4, 7, 7],
#                     [1, 2, 2, 2]]


# 4
# Given an array of integers a, your task is to find how many of its contiguous subarrays of length m contain a pair of integers with a sum equal to k.

# More formally, given the array a, your task is to count the number of indices 0 ≤ i ≤ a.length - m such that a subarray [a[i], a[i + 1], ..., a[i + m - 1]] contains at least one pair (a[s], a[t]), where:

# s ≠ t
# a[s] + a[t] = k
# Example

# For a = [2, 4, 7, 5, 3, 5, 8, 5, 1, 7], m = 4, and k = 10, the output should be findPairsSummingToK(a, m, k) = 5.

# Let's consider all subarrays of length m = 4 and see which fit the description conditions:

# Subarray a[0..3] = [2, 4, 7, 5] doesn't contain any pair of integers with a sum of k = 10. Note that although the pair (a[3], a[3]) has the sum 5 + 5 = 10, it doesn't fit the requirement s ≠ t.
# Subarray a[1..4] = [4, 7, 5, 3] contains the pair (a[2], a[4]), where a[2] + a[4] = 7 + 3 = 10.
# Subarray a[2..5] = [7, 5, 3, 5] contains two pairs (a[2], a[4]) and (a[3], a[5]), both with a sum of k = 10.
# Subarray a[3..6] = [5, 3, 5, 8] contains the pair (a[3], a[5]), where a[3] + a[5] = 5 + 5 = 10.
# Subarray a[4..7] = [3, 5, 8, 5] contains the pair (a[5], a[7]), where a[5] + a[7] = 5 + 5 = 10.
# Subarray a[5..8] = [5, 8, 5, 1] contains the pair (a[5], a[7]), where a[5] + a[7] = 5 + 5 = 10.
# Subarray a[6..9] = [8, 5, 1, 7] doesn't contain any pair with a sum of k = 10.
# So the answer is 5, because there are 5 contiguous subarrays that contain a pair with a sum of k = 10.

def findPairsSummingToK(a, m, k):
  counter = 0
  have = {}

  for i, n in enumerate(a):
    if i > m - 1:
      if have.get(a[i - m], 0) <= 1:
        have.pop(a[i - m], None)
      else:
        have[a[i - m]] -= 1
    
    if k - n in have:
      counter += 1 # may want to track the index
    
    have[n] = have.get(n, 0) + 1
  
  return counter

example = [2, 4, 7, 5, 3, 5, 8, 5, 1, 7]
findPairsSummingToK(example, 4, 10)
