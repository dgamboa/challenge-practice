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
  
  dict = {}

  
  for v in a:
    if a not in dict:
      dict[v] = 1
    else:
      dict[v] += 1
    
  print(dict)


