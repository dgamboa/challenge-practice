# ************************************************************************************************
# Write a function that reverses characters in (possibly nested) parentheses in the input string.
# Input strings will always be well-formed with matching ()s.
# For inputString = "foo(bar(baz))blim", the output should be
# reverseInParentheses(inputString) = "foobazrabblim"

# My solution:
def reverseInParentheses(inputString):
    store = []
    counter = 0
    output = ""
    
    for c in inputString:
        if c == "(":
            store.append("")
            counter += 1
            continue
        if c == ")":
            counter -= 1
            if counter > 0:
                store[counter - 1] += store.pop()[::-1]
            else:
                output += store.pop()[::-1]
            continue
        if counter == 0:
            output += c
            continue
        store[counter - 1] += c
    
    return output

# One of the top solutions -- uses recursion to preserve context for nested parentheses
def reverseInParentheses(s):
    for i in range(len(s)):
        if s[i] == "(":
            start = i
        if s[i] == ")":
            end = i
            return reverseInParentheses(s[:start] + s[start+1:end][::-1] + s[end+1:])
    return s

# The shortest solution:
def reverseInParentheses(s):
    return eval('"' + s.replace('(', '"+("').replace(')', '")[::-1]+"') + '"')

# ************************************************************************************************
# Given a string s consisting of small English letters, find and return the first instance of a non-repeating character in it. If there is no such character, return '_'.

# Example

# For s = "abacabad", the output should be
# firstNotRepeatingCharacter(s) = 'c'.

# There are 2 non-repeating characters in the string: 'c' and 'd'. Return c since it appears in the string first.

# For s = "abacabaabacaba", the output should be
# firstNotRepeatingCharacter(s) = '_'.

# There are no characters in this string that do not repeat.

# My Solution:
def firstNotRepeatingCharacter(s):
    tracker = []
    
    for c in string.ascii_lowercase:
        if c in s:
            tracker.append([s.count(c), s.index(c)])
    
    indeces = []
    for pair in tracker:
        if pair[0] == 1:
            indeces.append(pair[1])
    
    return s[min(indeces)] if len(indeces) > 0 else "_"

# Top Solution:
def firstNotRepeatingCharacter(s):
    for c in s:
        if s.index(c) == s.rindex(c):
            return c
    return '_'


# ************************************************************************************************
# From Trey:
# Output [**,**] for n=2, [***,* *,***] for n=3, [*****,*   *,*   *,*   *,*****] for n=5
def someListFunction(n):
  return ["*"*n] + ["*" + " "*(n-2) + "*"]*(n-2) + ["*"*n]


# ************************************************************************************************
# From Lindsay:
# Find all the pairs of two integers in an unsorted array that sum up to a given S. For example, if the array is [3, 5, 2, -4, 8, 11] and the sum is 7, your program should return [[11, -4], [2, 5]] because 11 + -4 = 7 and 2 + 5 = 7.
def findPairs(arr, S):
  result = []

  for n1 in arr:
    for n2 in arr:
      if n1 + n2 == S:
        result.append([n1, n2])
  
  return result
# >>> [[5, 2], [2, 5], [-4, 11], [11, -4]]
# Need to make sure there are no duplicates
