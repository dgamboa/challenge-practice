# ********Sprint 1.1***************************************************************************** #
# ********PROBLEM 1***************************************************************************** #
def do_lots_of_things(items):
  last = len(items) - 1
  print(items[last])
  
  middle = len(items) / 2
  i = 0
  while i < middle:
    print(items[i])
    i += 1

  for num in range(100):
    print(num)


# ********PROBLEM 2***************************************************************************** #
def do_a_couple_things(n):
  my_list = []
  my_second_list = [0] * 26

  for _ in range(n):
    my_list.append("lambda")
    print(my_second_list[n % 25])

  return my_list


# ********PROBLEM 3***************************************************************************** #
def csLongestPossible(str_1, str_2):
  combined_strings = list(str_1 + str_2)
  combined_strings.sort()
  combined_remove_dups = list(dict.fromkeys(combined_strings))
  return "".join(combined_remove_dups)


# ********Sprint 1.3***************************************************************************** #
# ********PROBLEM 1***************************************************************************** #
# You are given the prices of a stock, in the form of an array of integers, prices. Let's say that prices[i] is the price of the stock on the ith day (0-based index). Assuming that you are allowed to buy and sell the stock only once, your task is to find the maximum possible profit (the difference between the buy and sell prices).

# Note: You can assume there are no fees associated with buying or selling the stock.

# Example

# For prices = [6, 3, 1, 2, 5, 4], the output should be buyAndSellStock(prices) = 4.

# It would be most profitable to buy the stock on day 2 and sell it on day 4. Thus, the maximum profit is prices[4] - prices[2] = 5 - 1 = 4.

# For prices = [8, 5, 3, 1], the output should be buyAndSellStock(prices) = 0.

# Since the value of the stock drops each day, there's no way to make a profit from selling it. Hence, the maximum profit is 0.

# For prices = [3, 100, 1, 97], the output should be buyAndSellStock(prices) = 97.

# It would be most profitable to buy the stock on day 0 and sell it on day 1. Thus, the maximum profit is prices[1] - prices[0] = 100 - 3 = 97.


# First Attempt:
def buyAndSellStock(prices):
    accum = 0
    start_index = len(prices) - 1
    
    for i in range(start_index, 0, -1):
        for x in range(i - 1, -1, -1):
            if prices[i] - prices[x] > accum:
                accum = prices[i] - prices[x]
    
    return accum
# Score: 100/300


# Second Attempt:
def buyAndSellStock(prices):
    local_min = [0, prices[0]]
    local_max = [0, prices[0]]
    
    for i, p in enumerate(prices):
        if p > local_max[1] and i > local_min[0]:
            local_max = [i, p]
        if p < local_min[1] and i < local_max[0]:
            local_min = [i, p]
        
            
    return local_max[1] - local_min[1]
# Score: n/a


# Third Attempt:
def buyAndSellStock(prices):
    accum = 0
    
    for i in range(0, len(prices) - 1, 1):
        if max(prices[i + 1:]) - prices[i] > accum:
            accum = max(prices[i + 1:]) - prices[i]
    
    return accum
# Score: 180/300


# Fourth Attempt:
def buyAndSellStock(prices):
    max_profit = 0
    low_price = prices[0]
    
    for i in range(1, len(prices)):
        low_price = min(low_price, prices[i])
        max_profit = max(max_profit, prices[i] - low_price)
    
    return max_profit
# Score: 300/300


# ********PROBLEM 2***************************************************************************** #
# Given a string, your task is to replace each of its characters by the next one in the English alphabet; i.e. replace a with b, replace b with c, etc (z would be replaced by a).

# Example

# For inputString = "crazy", the output should be alphabeticShift(inputString) = "dsbaz".

# First Attempt:
def alphabeticShift(inputString):
    alpha = list(string.ascii_lowercase)
    input_list = list(inputString)
    output_list = []
    
    for c in input_list:
        if c == 'z':
            output_list.append('a')
        else:
            i = alpha.index(c)
            output_list.append(alpha[i + 1])
    
    return "".join(output_list)

# Score: 300/300


# Re-factored Attempt:
def alphabeticShift(inputString):
    output = ""
    
    for c in inputString:
        output += 'a' if c == 'z' else chr(ord(c) + 1)
        
    return output
# Score: 300/300



# ********PROBLEM 3***************************************************************************** #
# You are given a parentheses sequence, check if it's regular.

# Example

# For s = "()()(())", the output should be
# validParenthesesSequence(s) = true;
# For s = "()()())", the output should be
# validParenthesesSequence(s) = false.

# First Attempt:
def validParenthesesSequence(s):
    accum = 0
    
    for c in s:
        if c == '(':
            accum += 1
        else:
            accum -= 1
        
        if accum < 0:
            return False
    
    if accum == 0:
        return True
        
    return False
# Score: 300/300


# Re-factored Attempt:
def validParenthesesSequence(s):
    accum = 0
    
    for c in s:
        accum += 1 if c == '(' else -1
        if accum < 0:
            return False
    
    return True if accum == 0 else False
# Score: 300/300



# ********Sprint 1.4***************************************************************************** #
# ********PROBLEM 1***************************************************************************** #
# You are given the prices of a stock, in the form of an array of integers, prices. Let's say that prices[i] is the price of the stock on the ith day (0-based index). Assuming that you are allowed to buy and sell the stock only once, your task is to find the maximum possible profit (the difference between the buy and sell prices).

# Note: You can assume there are no fees associated with buying or selling the stock.

# Example

# For prices = [6, 3, 1, 2, 5, 4], the output should be buyAndSellStock(prices) = 4.

# It would be most profitable to buy the stock on day 2 and sell it on day 4. Thus, the maximum profit is prices[4] - prices[2] = 5 - 1 = 4.

# For prices = [8, 5, 3, 1], the output should be buyAndSellStock(prices) = 0.

# Since the value of the stock drops each day, there's no way to make a profit from selling it. Hence, the maximum profit is 0.

# For prices = [3, 100, 1, 97], the output should be buyAndSellStock(prices) = 97.

# It would be most profitable to buy the stock on day 0 and sell it on day 1. Thus, the maximum profit is prices[1] - prices[0] = 100 - 3 = 97.


# First Attempt:
def buyAndSellStock(prices):
    accum = 0
    start_index = len(prices) - 1
    
    for i in range(start_index, 0, -1):
        for x in range(i - 1, -1, -1):
            if prices[i] - prices[x] > accum:
                accum = prices[i] - prices[x]
    
    return accum
# Score: 100/300


# Second Attempt:
def buyAndSellStock(prices):
    local_min = [0, prices[0]]
    local_max = [0, prices[0]]
    
    for i, p in enumerate(prices):
        if p > local_max[1] and i > local_min[0]:
            local_max = [i, p]
        if p < local_min[1] and i < local_max[0]:
            local_min = [i, p]
        
            
    return local_max[1] - local_min[1]
# Score: n/a


# Third Attempt:
def buyAndSellStock(prices):
    accum = 0
    
    for i in range(0, len(prices) - 1, 1):
        if max(prices[i + 1:]) - prices[i] > accum:
            accum = max(prices[i + 1:]) - prices[i]
    
    return accum
# Score: 180/300


# Fourth Attempt:
def buyAndSellStock(prices):
    max_profit = 0
    low_price = prices[0]
    
    for i in range(1, len(prices)):
        low_price = min(low_price, prices[i])
        max_profit = max(max_profit, prices[i] - low_price)
    
    return max_profit
# Score: 300/300


# ********PROBLEM 2***************************************************************************** #
# Given a string, your task is to replace each of its characters by the next one in the English alphabet; i.e. replace a with b, replace b with c, etc (z would be replaced by a).

# Example

# For inputString = "crazy", the output should be alphabeticShift(inputString) = "dsbaz".

# First Attempt:
def alphabeticShift(inputString):
    alpha = list(string.ascii_lowercase)
    input_list = list(inputString)
    output_list = []
    
    for c in input_list:
        if c == 'z':
            output_list.append('a')
        else:
            i = alpha.index(c)
            output_list.append(alpha[i + 1])
    
    return "".join(output_list)

# Score: 300/300


# Re-factored Attempt:
def alphabeticShift(inputString):
    output = ""
    
    for c in inputString:
        output += 'a' if c == 'z' else chr(ord(c) + 1)
        
    return output
# Score: 300/300



# ********PROBLEM 3***************************************************************************** #
# You are given a parentheses sequence, check if it's regular.

# Example

# For s = "()()(())", the output should be
# validParenthesesSequence(s) = true;
# For s = "()()())", the output should be
# validParenthesesSequence(s) = false.

# First Attempt:
def validParenthesesSequence(s):
    accum = 0
    
    for c in s:
        if c == '(':
            accum += 1
        else:
            accum -= 1
        
        if accum < 0:
            return False
    
    if accum == 0:
        return True
        
    return False
# Score: 300/300


# Re-factored Attempt:
def validParenthesesSequence(s):
    accum = 0
    
    for c in s:
        accum += 1 if c == '(' else -1
        if accum < 0:
            return False
    
    return True if accum == 0 else False
# Score: 300/300


# ********Sprint 1.5 Challenge***************************************************************************** #
# ********PROBLEM 1***************************************************************************** #
# Given a string (the input will be in the form of an array of characters), write a function that returns the reverse of the given string.

# Examples:

# csReverseString(["l", "a", "m", "b", "d", "a"]) -> ["a", "d", "b", "m", "a", "l"]
# csReverseString(["I", "'", "m", " ", "a", "w", "e", "s", "o", "m", "e"]) -> ["e", "m", "o", "s", "e", "w", "a", " ", "m", "'", "I"]
# Notes:

# Your solution should be "in-place" with O(1) space complexity. Although many in-place functions do not return the modified input, in this case you should.
# You should try using a "two-pointers approach".
# Avoid using any built-in reverse methods in the language you are using (the goal of this challenge is for you to implement your own method).

# First Attempt:
# Score: 300 / 300
def csReverseString(chars):
    i, j = 0, len(chars) - 1
    
    for n in range(j//2 + 1):
        store = chars[i]
        chars[i] = chars[j]
        chars[j] = store
        i += 1
        j -= 1
    
    return chars


# ********PROBLEM 2***************************************************************************** #
# A palindrome is a word, phrase, number, or another sequence of characters that reads the same backward or forward. This includes capital letters, punctuation, and other special characters.

# Given a string, write a function that checks if the input is a valid palindrome.

# Examples:

# csCheckPalindrome("racecar") -> true
# csCheckPalindrome("anna") -> true
# csCheckPalindrome("12345") -> false
# csCheckPalindrome("12321") -> true
# Notes:

# Try to solve this challenge without using the reverse of the input string; use a for loop to iterate through the string and make the necessary comparisons.
# Something like the code below might be your first intuition, but can you figure out a way to use a for loop instead?

# Example to Avoid:
def csCheckPalindrome(input_str):
    return input_str == "".join(reversed(input_str))

# First Attempt:
# Score: 300 / 300
def csCheckPalindrome(input_str):
    reverse = ""
    
    for i in range(len(input_str) - 1, -1, -1):
        reverse += input_str[i]
    
    return reverse == input_str

# Re-factored Attempt:
# Score: 300 / 300
def csCheckPalindrome(input_str):
    return input_str == "".join([input_str[i] for i in range(len(input_str) - 1, -1, -1)])

# Using 2-Pointer Approach:
# Score: 300 / 300
    def csCheckPalindrome(input_str):
        reverse = list(input_str)
        i, j = 0, len(input_str) - 1
        
        for n in range(len(input_str)//2 + 1):
            store = reverse[i]
            reverse[i] = reverse[j]
            reverse[j] = store
            i += 1
            j -= 1
        
        return "".join(reverse) == input_str


# ********PROBLEM 3***************************************************************************** #
# Given a string, write a function that removes all duplicate words from the input. The string that you return should only contain the first occurrence of each word in the string.

# Examples:

# `csRemoveDuplicateWords("alpha bravo bravo golf golf golf delta alpha bravo bravo golf golf golf delta") -> "alpha bravo golf delta"
# `csRemoveDuplicateWords("my dog is my dog is super smart") -> "my dog is super smart"

# First Attempt:
# Score: 300 / 300
def csRemoveDuplicateWords(input_str):
    novel = []
    raw = input_str.split(" ")
    
    for w in raw:
        if w not in novel: novel.append(w)
        
    return " ".join(novel)

# One-Line Approach:
def csRemoveDuplicateWords(input_str):
    return " ".join(list(dict.fromkeys(input_str.split(" "))))



# ********Sprint 2.1 Challenge***************************************************************************** #
# ********PROBLEM 1***************************************************************************** #
# Given an integer, write a function that reverses the bits (in binary) and returns the integer result.

# Examples:

# csReverseIntegerBits(417) -> 267
# 417 in binary is 110100001. Reversing the binary is 100001011, which is 267 in decimal.
# csReverseIntegerBits(267) -> 417
# csReverseIntegerBits(0) -> 0
# Notes:

# The input integer will not be negative.

# Initial Submission
def csReverseIntegerBits(n):
    if n == 0: return 0
    
    places = math.floor(math.log2(n))
    store = [0] * (places + 1)
    sum = 0
    
    for i in range(places, -1, -1):
        if 2**i + sum <= n:
            sum += 2**i
            store[i] = 1
    
    store.reverse()
    
    sum = 0
    for i, v in enumerate(store):
        sum += 2**i * v
    
    return sum

# Re-Factored
def csReverseIntegerBits(n):
    return int(f"{n:b}"[::-1], 2)


# ********PROBLEM 2***************************************************************************** #
# Given a binary string (ASCII encoded), write a function that returns the equivalent decoded text.

# Every eight bits in the binary string represents one character on the ASCII table.

# Examples:

# csBinaryToASCII("011011000110000101101101011000100110010001100001") -> "lambda"
# 01101100 -> 108 -> "l"
# 01100001 -> 97 -> "a"
# 01101101 -> 109 -> "m"
# 01100010 -> 98 -> "b"
# 01100100 -> 100 -> "d"
# 01100001 -> 97 -> "a"
# csBinaryToASCII("") -> ""
# Notes:

# The input string will always be a valid binary string.
# Characters can be in the range from "00000000" to "11111111" (inclusive).
# In the case of an empty input string, your function should return an empty string.


# Initial Submission
def csBinaryToASCII(binary, n=8):
    if binary == "": return ""
    
    split_string = [chr(int(binary[i:i+n], 2)) for i in range(0,len(binary),n)]
    return "".join(split_string)
    

# ********PROBLEM 3***************************************************************************** #
# Given a number, write a function that converts that number into a string that contains "raindrop sounds" corresponding to certain potential factors. A factor is a number that evenly divides into another number, leaving no remainder. The simplest way to test if one number is a factor of another is to use the modulo operator.

# Here are the rules for csRaindrop. If the input number:

# has 3 as a factor, add "Pling" to the result.
# has 5 as a factor, add "Plang" to the result.
# has 7 as a factor, add "Plong" to the result.
# does not have any of 3, 5, or 7 as a factor, the result should be the digits of the input number.

# Initial Submission
def csRaindrops(number):
    output = ""
    
    if number % 3 == 0:
        output += "Pling"
        
    if number % 5 == 0:
        output+= "Plang"
    
    if number % 7 == 0:
        output+= "Plong"
    
    return output if len(output) > 0 else str(number)


# ********Sprint 2.2 Challenge***************************************************************************** #
# ********PROBLEM 1***************************************************************************** #
# You are given a non-empty array of integers.

# One element appears exactly once, with every other element appearing at least twice, perhaps more.

# Write a function that can find and return the element that appears exactly once.

# Example 1:

# Input: [1,1,2,1]
# Output: 2
# Example 2:

# Input: [1,2,1,2,1,2,80]
# Output: 80
# Note: You should be able to develop a solution that has O(n) time complexity.

# Initial Submission
def csFindTheSingleNumber(nums):
    store = {}
    
    for n in nums:
        if n not in store: store[n] = 0
        store[n] += 1
    
    sorted_store = sorted(store.items(), key=lambda e: e[1])
    return sorted_store[0][0]


# ********PROBLEM 2***************************************************************************** #
# Given a list of different students' scores, write a function that returns the average of each student's top five scores. You should return the averages in ascending order of the students' id numbers.

# Each entry (scores[i]) has the student's id number (scores[i][0]) and the student's score (scores[i][1]). The averages should be calculated using integer division.

# Example 1:

# Input: [[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]]
# Output: [[1,87],[2,88]]
# Explanation:
# The average student `1` is `87`.
# The average of student `2` is `88.6`, but with integer division is `88`.
# Notes:

# The score of the students is between 1 and 100.

# Initial Submission
def csAverageOfTopFive(scores):
    store = {}
    
    for e in scores:
        id = e[0]
        if id not in store: store[id] = []
        store[id].append(e[1])
    
    output = []
    
    for item in store.items():
        id = item[0]
        scores = sorted(item[1], reverse=True)
        avg = sum(scores[:5]) // min(len(scores), 5)
        output.append([id, avg])
    
    return output


# ********PROBLEM 3***************************************************************************** #
# Given a string text, you need to use the characters of text to form as many instances of the word "lambda" as possible.

# You can use each character in text at most once.

# Write a function that returns the maximum number of instances of "lambda" that can be formed.

# Example 1:

# Input: text = "mbxcdatlas"
# Output: 1
# Example 2:

# Input: text = "lalaaxcmbdtsumbdav"
# Output: 2
# Example 3:

# Input: text = "sctlamb"
# Output: 0
# Notes:

# text consists of lowercase English characters only

# Initial Submission
def csMaxNumberOfLambdas(text):
    store = {}
    
    for c in text:
        if c not in store: store[c] = 0
        store[c] += 1
        
    max_lambda = []
    lambda_name = [("l", 1), ("a", 2), ("m", 1), ("b", 1), ("d", 1)]
    
    for k, v in lambda_name:
        if k not in store: return 0
        max_lambda.append(store[k]//v)
    
    return min(max_lambda)


# ********Sprint 2.3 Challenge***************************************************************************** #
# ********PROBLEM 1***************************************************************************** #
# Given two strings a and b, determine if they are isomorphic.

# Two strings are isomorphic if the characters in a can be replaced to get b.

# All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.

# Example 1:

# Input: 
# a = "odd"
# b = "egg"

# Output:
# true
# Example 2:

# Input:
# a = "foo"
# b = "bar"

# Output:
# false
# Example 3:

# Input:
# a = "abca"
# b = "zbxz"

# Output:
# true
# Example 4:

# Input:
# a = "abc"
# b = ""

# Output:
# false

# Initial Submission
def csIsomorphicStrings(a, b):
    if b == "" and a != "": return False
    if b != "" and a == "": return False
    
    store = {}
    
    for i, c in enumerate(a):
        print(i)
        print(c)
        if c not in store and len(b) > 0: store[c] = b[min(i, len(b) - 1)]
    print(store)
    
    for i, c in enumerate(b):
        if c != store[a[i]]: return False
    
    return True

# ********PROBLEM 2***************************************************************************** #
# Given a pattern and a string a, find if a follows the same pattern.

# Here, to "follow" means a full match, such that there is a one-to-one correspondence between a letter in pattern and a non-empty word in a.

# Example 1:

# Input:
# pattern = "abba"
# a = "lambda school school lambda"

# Output: true
# Example 2:

# Input:
# pattern = "abba"
# a = "lambda school school coding"

# Output:
# false
# Example 3:

# Input:
# pattern = "aaaa"
# a = "lambda school school lambda"

# Output: false
# Example 4:

# Input:
# pattern = "abba"
# a = "lambda lambda lambda lambda"

# Output: false
# Notes:

# pattern contains only lower-case English letters.
# a contains only lower-case English letters and spaces ' '.
# a does not contain any leading or trailing spaces.
# All the words in a are separated by a single space.

# Initial Submission
# Score: 243/300
def csWordPattern(pattern, a):
    all_words = a.split()
    unique_words = list(set(all_words))
    
    store = {c: unique_words[i] for i,c in enumerate(pattern) if i < len(unique_words)}
    
    print(store)
    
    for i,c in enumerate(pattern):
        if c not in store: return False
        if store[c] != all_words[i]: return False
    
    return True

# Second Submission
# Score: 300/300
def csWordPattern(pattern, a):
    all_words = a.split()
    if len(pattern) != len(all_words): return False
    
    store = {}
    for i in range(min(len(all_words), len(pattern))):
        if all_words[i] not in store.values():
            store[pattern[i]] = all_words[i]
    
    for i,c in enumerate(pattern):
        if c not in store: return False
        if store[c] != all_words[i]: return False
    
    return True


# ********PROBLEM 3***************************************************************************** #
# Given an array of strings strs, write a function that can group the anagrams. The groups should be ordered such that the larger groups come first, with subsequent groups ordered in descending order.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

# Example 1:

# Input:
# strs = ["apt","pat","ear","tap","are","arm"]

# Output:
# [["apt","pat","tap"],["ear","are"],["arm"]]
# Example 2:

# Input:
# strs = [""]

# Output:
# [[""]]
# Example 3:

# Input:
# strs = ["a"]

# Output:
# [["a"]]
# Notes:

# strs[i] consists of lower-case English letters.

# Initial Submission
def csGroupAnagrams(strs):
    store = {}
    
    for s in strs:
        hash_value = 0        
        for c in s:
            hash_value += ord(c)
        
        if hash_value not in store:
            store[hash_value] = [s]
        else:
            store[hash_value].append(s)
    
    return sorted(list(store.values()), key=lambda x: len(x), reverse=True)
        


# ********Sprint 3.1 Challenge***************************************************************************** #
# ********PROBLEM 1***************************************************************************** #
# Note: Your solution should have O(n) time complexity, where n is the number of elements in l, since this is what you will be asked to accomplish in an interview.

# You have a singly linked list l, which is sorted in strictly increasing order, and an integer value. Add value to the list l, preserving its original sorting.

# Note: in examples below and tests preview linked lists are presented as arrays just for simplicity of visualization: in real data you will be given a head node l of the linked list

# Example

# For l = [1, 3, 4, 6] and value = 5, the output should be
# insertValueIntoSortedLinkedList(l, value) = [1, 3, 4, 5, 6];
# For l = [1, 3, 4, 6] and value = 10, the output should be
# insertValueIntoSortedLinkedList(l, value) = [1, 3, 4, 6, 10];
# For l = [1, 3, 4, 6] and value = 0, the output should be
# insertValueIntoSortedLinkedList(l, value) = [0, 1, 3, 4, 6].
# Input/Output

# [execution time limit] 4 seconds (py3)

# [input] linkedlist.integer l

# A singly linked list of integers sorted in strictly increasing order. Thus, all integers in the list are pairwise distinct.

# Guaranteed constraints:
# 0 ≤ list size ≤ 104,
# -109 ≤ element value ≤ 109.

# [input] integer value

# A single integer value to be inserted into l. It is guaranteed that there is not an element equal to value in l before the insertion is performed.

# Guaranteed constraints:
# -109 ≤ value ≤ 109.

# [output] linkedlist.integer

# Initial Submission:
# Return l after inserting value into it, with the original sorting preserved.
# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def insertValueIntoSortedLinkedList(l, value):
    new_node = ListNode(value)

    if l is None:
        l = new_node
        return l
    
    if value < l.value:
        new_node.next = l
        l = new_node
        return l
    
    list_copy = l
    while list_copy.next is not None and list_copy.next.value < value:
        list_copy = list_copy.next
    
    new_node.next = list_copy.next
    list_copy.next = new_node
    
    return l

# ********PROBLEM 2***************************************************************************** #
# Note: Your solution should have O(l1.length + l2.length) time complexity, since this is what you will be asked to accomplish in an interview.

# Given two singly linked lists sorted in non-decreasing order, your task is to merge them. In other words, return a singly linked list, also sorted in non-decreasing order, that contains the elements from both original lists.

# Example

# For l1 = [1, 2, 3] and l2 = [4, 5, 6], the output should be
# mergeTwoLinkedLists(l1, l2) = [1, 2, 3, 4, 5, 6];
# For l1 = [1, 1, 2, 4] and l2 = [0, 3, 5], the output should be
# mergeTwoLinkedLists(l1, l2) = [0, 1, 1, 2, 3, 4, 5].

# Initial Submission:
# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def mergeTwoLinkedLists(l1, l2):
    if l1 is None:
        return l2
    elif l2 is None:
        return l1

    if l1.value < l2.value:
        l = ListNode(l1.value)
        cur1 = l1.next
        cur2 = l2
    else:
        l = ListNode(l2.value)
        cur1 = l1
        cur2 = l2.next
    
    merge = l
    while cur1 is not None or cur2 is not None:
        if cur1 is not None and cur2 is None:
            merge.next = cur1
            merge = merge.next
            cur1 = cur1.next  
        elif cur1 is None and cur2 is not None:
            merge.next = cur2
            merge = merge.next
            cur2 = cur2.next
        elif cur1.value < cur2.value:
            merge.next = cur1
            merge = merge.next
            cur1 = cur1.next
        else:
            merge.next = cur2
            merge = merge.next
            cur2 = cur2.next

    return l


# ********Sprint 3.2 Challenge************************************************ #
# ********PROBLEM 1*********************************************************** #
# Implement the missing code, denoted by ellipses. You may not modify the pre-existing code.
# Implement a queue using two stacks.

# You are given an array of requests, where requests[i] can be "push <x>" or "pop". Return an array composed of the results of each "pop" operation that is performed.

# Example

# For requests = ["push 1", "push 2", "pop", "push 3", "pop"], the output should be
# queueOnStacks(requests) = [1, 2].

# After the first request, the queue is {1}; after the second it is {1, 2}. Then we do the third request, "pop", and add the first element of the queue 1 to the answer array. The queue becomes {2}. After the fourth request, the queue is {2, 3}. Then we perform "pop" again and add 2 to the answer array, and the queue becomes {3}.
class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()


def queueOnStacks(requests):
    left = Stack()
    right = Stack()

    def insert(x):
        while left.isEmpty() is not True:
            right.push(left.pop())
        
        left.push(x)
        
        while right.isEmpty() is not True:
            left.push(right.pop())
            

    def remove():
        return left.pop()

    ans = []
    for request in requests:
        req = request.split(" ")
        if req[0] == 'push':
            insert(int(req[1]))
        else:
            ans.append(remove())
    return ans



# ********PROBLEM 2*********************************************************** #
# Given a string sequence consisting of the characters '(', ')', '[', ']', '{', and '}'. Your task is to determine whether or not the sequence is a valid bracket sequence.

# The Valid bracket sequence is defined in the following way:

# An empty bracket sequence is a valid bracket sequence.
# If S is a valid bracket sequence then (S), [S] and {S} are also valid.
# If A and B are valid bracket sequences then AB is also valid.
# Example

# For sequence = "()", the output should be validBracketSequence(sequence) = true;
# For sequence = "()[]{}", the output should be validBracketSequence(sequence) = true;
# For sequence = "(]", the output should be validBracketSequence(sequence) = false;
# For sequence = "([)]", the output should be validBracketSequence(sequence) = false;
# For sequence = "{[]}", the output should be validBracketSequence(sequence) = true.
def validBracketSequence(sequence):
    stack = []
    reference = {")": "(", "}": "{", "]": "["}
    
    for b in sequence:
        if len(stack) == 0:
            stack.append(b)
        elif b in reference.keys() and stack[-1] == reference[b]:
            stack.pop()
        else:
            stack.append(b)
    
    return True if len(stack) == 0 else False


# ********Sprint 3.3 Challenge************************************************ #
# ********PROBLEM 1*********************************************************** #
# You are given a binary tree and you need to write a function that can determine if it is height-balanced.

# A height-balanced tree can be defined as a binary tree in which the left and right subtrees of every node differ in height by a maximum of 1.

# Example 1:
# Given the following tree [5,10,25,None,None,12,3]:

#     5
#    / \
#  10  25
#     /  \
#    12   3
# return True.

# Example 2:
# Given the following tree [5,6,6,7,7,None,None,8,8]:

#        5
#       / \
#      6   6
#     / \
#    7   7
#   / \
#  8   8
# return False.

# Initial Submission:
#
# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
def levelCounter(node):
    if node is None:
        return 0
    elif node.left is None and node.right is None:
        return 1
    elif node.left is None:
        return 1 + levelCounter(node.right)
    elif node.right is None:
        return 1 + levelCounter(node.left)
    else:
        return 1 + max(levelCounter(node.left), levelCounter(node.right))

def balancedBinaryTree(root):
    if root is None: return True
    
    leftLevels = levelCounter(root.left)
    rightLevels = levelCounter(root.right)
    
    
    if abs(leftLevels - rightLevels) > 1:
        return False
    else:
        return balancedBinaryTree(root.left) and balancedBinaryTree(root.right)
    

# ********PROBLEM 2*********************************************************** #
# You are given a binary tree and you are asked to write a function that finds its minimum depth. The minimum depth can be defined as the number of nodes along the shortest path from the root down to the nearest leaf node. As a reminder, a leaf node is a node with no children.

# Example:
# Given the binary tree [5,7,22,None,None,17,9],

#     5
#    / \
#   7  22
#     /  \
#    17   9
# your function should return its minimum depth = 2.

# Initial Submission:
#
# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
def minimumDepthBinaryTree(root):
    if root is None:
        return 0
    elif root.left is None and root.right is None:
        return 1
    elif root.left is None:
        return 1 + minimumDepthBinaryTree(root.right)
    elif root.right is None:
        return 1 + minimumDepthBinaryTree(root.left)
    else:
        return 1 + min(minimumDepthBinaryTree(root.right), minimumDepthBinaryTree(root.left))


# ********Sprint 3.4 Challenge************************************************ #
# ********PROBLEM 1*********************************************************** #
# You are given a binary tree. Write a function that returns the binary tree's node values using an in-order traversal.

# Example:
# Input: [2,None,3,4]

#    2
#     \
#      3
#     /
#    4
# Output: [2,4,3]

# Initial Submission:
#
# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
def search(root, res):
    if root is None:
        return
    search(root.left, res)
    res.append(root.value)
    search(root.right, res)

def binaryTreeInOrderTraversal(root):
    result = []
    search(root, result)
    return result

# ********PROBLEM 2*********************************************************** #
# Note: Try to solve this task without using recursion, since this is what you'll be asked to do during an interview.

# Given a binary tree of integers t, return its node values in the following format:

# The first element should be the value of the tree root;
# The next elements should be the values of the nodes at height 1 (i.e. the root children), ordered from the leftmost to the rightmost one;
# The elements after that should be the values of the nodes at height 2 (i.e. the children of the nodes at height 1) ordered in the same way;
# Etc.
# Example

# For

# t = {
#     "value": 1,
#     "left": {
#         "value": 2,
#         "left": null,
#         "right": {
#             "value": 3,
#             "left": null,
#             "right": null
#         }
#     },
#     "right": {
#         "value": 4,
#         "left": {
#             "value": 5,
#             "left": null,
#             "right": null
#         },
#         "right": null
#     }
# }
# the output should be
# traverseTree(t) = [1, 2, 4, 3, 5].

# Initial Submission:
from collections import deque
#
# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
def traverseTree(t):
    if t is None:
        return []
    
    result = []
    nodes = deque()
    nodes.append(t)
    
    while len(nodes) > 0:
        n = nodes.popleft()
            
        if n is not None:
            nodes.append(n.left)
            nodes.append(n.right)
            result.append(n.value)
    
    return result
            

# ********PROBLEM 3*********************************************************** #
# Given a binary tree of integers, return all the paths from the tree's root to its leaves as an array of strings. The strings should have the following format:
# "root->node1->node2->...->noden", representing the path from root to noden, where root is the value stored in the root and node1,node2,...,noden are the values stored in the 1st, 2nd,..., and nth nodes in the path respectively (noden representing the leaf).

# Example

# For

# t = {
#     "value": 5,
#     "left": {
#         "value": 2,
#         "left": {
#             "value": 10,
#             "left": null,
#             "right": null
#         },
#         "right": {
#             "value": 4,
#             "left": null,
#             "right": null
#         }
#     },
#     "right": {
#         "value": -3,
#         "left": null,
#         "right": null
#     }
# }
# the output should be
# treePaths(t) = ["5->2->10", "5->2->4", "5->-3"].

# The given tree looks like this:

#     5
#    / \
#   2  -3
#  / \
# 10  4

# Initial Submission:
#
# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
def search(root, res, tracker):
    if root is None:
        return
    
    res.append(root.value)
    search(root.left, res, tracker)
    search(root.right, res, tracker)
    
    if root.left is None and root.right is None:
        tracker.append("->".join([str(i) for i in res]))
    
    res.pop()

def treePaths(t):
    res = []
    tracker = []
    search(t, res, tracker)
    return tracker

# ********Sprint 3.5 Challenge************************************************ #
# ********PROBLEM 1*********************************************************** #
# Note: Your solution should have O(l.length) time complexity and O(1) space complexity, since this is what you will be asked to accomplish in an interview.

# Given a singly linked list, reverse and return it.

# Example

# For l = [1, 2, 3, 4, 5], the output should be
# reverseLinkedList(l) = [5, 4, 3, 2, 1].

# Initial Submission
# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def reverseLinkedList(l):
    if l is None or l.next is None:
        return l
    
    cur_node = l
    next_node = cur_node.next
    cur_node.next = None
    
    while next_node is not None:
        prev_node = cur_node
        cur_node = next_node
        next_node = cur_node.next
        cur_node.next = prev_node
    
    return cur_node

# ********PROBLEM 2*********************************************************** #
# You are given the root node of a binary search tree (BST).

# You need to write a function that returns the sum of values of all the nodes with a value between lower and upper (inclusive).

# The BST is guaranteed to have unique values.

# Example 1:

# Input:
# root = [10, 5, 15, 3, 7, null, 18]
# lower = 7
# upper = 15

#          10
#          / \
#         5  15
#        / \    \
#       3   7    18

# Output:
# 32
# Example 2:

# Input:
# root = [10,5,15,3,7,13,18,1,null,6]
# lower = 6
# upper = 10

#            10
#           /  \
#        5       15
#      / \     /   \ 
#     3   7  13   18
#    /   /
#   1   6

# Output:
# 23

# Initial Submission:
#
# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
def search(node, lower, upper, tracker):
    if node is None:
        return
    elif node.value < lower:
        search(node.right, lower, upper, tracker)
    elif node.value > upper:
        search(node.left, lower, upper, tracker)
    else:
        tracker.append(node.value)
        search(node.left, lower, upper, tracker)
        search(node.right, lower, upper, tracker)

def csBSTRangeSum(root, lower, upper):
    tracker = []
    search(root, lower, upper, tracker)
    return sum(tracker)

# Second Submission (more efficient because tracker is int):
#
# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
def search(node, lower, upper, tracker):
    if node is None:
        return tracker
    elif node.value < lower:
        tracker = search(node.right, lower, upper, tracker)
    elif node.value > upper:
        tracker = search(node.left, lower, upper, tracker)
    else:
        tracker += node.value
        tracker = search(node.left, lower, upper, tracker)
        tracker = search(node.right, lower, upper, tracker)
    
    return tracker

def csBSTRangeSum(root, lower, upper):
    tracker = 0
    return search(root, lower, upper, tracker)
    
    
# ********PROBLEM 3*********************************************************** #
# Given a binary tree, write a function that inverts the tree.

# Example:

# Input:
#      6
#    /   \
#   4     8
#  / \   / \
# 2   5 7   9

# Output:
#      6
#    /   \
#   8     4
#  / \   / \
# 9   7 5   2

# Initial Submission:
#
# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
def csBinaryTreeInvert(root):
    if root is None: return
    
    old_left = root.left
    root.left = root.right
    root.right = old_left
    csBinaryTreeInvert(root.left)
    csBinaryTreeInvert(root.right)
    
    return root

# ********Sprint 4.1 Challenge************************************************ #
# ********PROBLEM 1*********************************************************** #
# You are given a directed acyclic graph (DAG) that contains N nodes.

# Write a function that can find all the possible paths from node 0 to node N - 1.

# graph[a] is a list of all nodes b for which the edge a -> b exists.

# Input: graph = [[1, 2],[3],[3],[4],[]]
# Output: [[0,1,3,4], [0,2,3,4]]
# Note: The results must be returned in sorted order. You can use any built-in sort method on the results array at the end of your function before returning.

# Submission:
def csFindAllPathsFromAToB(graph, n=0, trace=[], paths=[]):
    trace = trace.copy()
    trace.append(n)
    for neighbor in graph[n]:
        if neighbor not in trace:
            paths = csFindAllPathsFromAToB(graph, neighbor, trace, paths)
    if n == len(graph) - 1:
        paths.append(trace)
    return sorted(paths)

# ********Sprint 4.2 Challenge************************************************ #
# ********PROBLEM 1*********************************************************** #
# There are N students in a baking class together. Some of them are friends, while some are not friends. The students' friendship can be considered transitive. This means that if Ami is a direct friend of Bill, and Bill is a direct friend of Casey, Ami is an indirect friend of Casey. A friend circle is a group of students who are either direct or indirect friends of some level. That is, the friend circle consists of a person, their friends, their friends-of-friends, their friends-of-friends-of-friends, and so on.

# Given a N*N matrix M representing the friend relationships between students in the class. If M[i][j] = 1, then the ith and jth students are direct friends with each other, otherwise not.

# You need to write a function that can output the total number of friend circles among all the students.

# Example 1:

# Input: 
# [[1,1,0],
#  [1,1,0],
#  [0,0,1]]
# Output: 2
# Explanation: The 0th and 1st students are direct friends, so they are in a friend circle. 
# The 2nd student himself is in a friend circle. So return 2.
# Example 2:

# Input: 
# [[1,1,0],
#  [1,1,1],
#  [0,1,1]]
# Output: 1
# Explanation: The 0th and 1st students are direct friends, the 1st and 2nd students are direct friends, 
# so the 0th and 2nd students are indirect friends. All of them are in the same friend circle, so return 1.

# Initial Submission
# Passes only some tests
# Something similar to this might work for car problem
def csFriendCircles(friendships):
    visited = set()
    count = 0
    
    def visit_friends(row, col):
        if ((row, col) in visited or
            row < 0 or
            row > len(friendships) - 1 or
            col < 0 or
            col > len(friendships[0]) - 1):
            return
        
        visited.add((row, col))
        
        if friendships[row][col] == 0:
            return
        
        visit_friends(row + 1, col)
        visit_friends(row - 1, col)
        visit_friends(row, col + 1)
        visit_friends(row, col - 1)
    
    for i in range(len(friendships)):
        for j in range(len(friendships[i])):
            if (i, j) not in visited:
                visit_friends(i, j)
                if friendships[i][j] == 1:
                    count += 1
    
    return count

# Second Submission
# Passes All Tests including INPUT: [[0,0], [0,0]] OUTPUT: 0
def csFriendCircles(friendships):
    visited = set()
    count = 0
    
    def visit_friends(row, col):
        if ((row, col) in visited or
            row < 0 or
            row > len(friendships) - 1 or
            col < 0 or
            col > len(friendships[0]) - 1):
            return
        
        visited.add((row, col))
        
        if friendships[row][col] == 1:
            visit_friends(col, row)
        
        visit_friends(row, col + 1)
        visit_friends(row, col - 1)
    
    for i in range(len(friendships)):
        for j in range(len(friendships[i])):
            if (i, j) not in visited:
                visit_friends(i, j)
                if sum(friendships[i]) > 0:
                    count += 1
    
    return count


# Third Submission
# Slight refactor to remove rows from if statement in visit_friends
def csFriendCircles(friendships):
    visited = set()
    count = 0
    
    def visit_friends(row, col):
        if ((row, col) in visited or
            col < 0 or
            col > len(friendships[0]) - 1):
            return
        
        visited.add((row, col))
        
        if friendships[row][col] == 1:
            visit_friends(col, row)
        
        visit_friends(row, col + 1)
        visit_friends(row, col - 1)
    
    for i in range(len(friendships)):
        for j in range(len(friendships[i])):
            if (i, j) not in visited:
                visit_friends(i, j)
                if sum(friendships[i]) > 0:
                    count += 1
    
    return count


# ********Final Sprint Challenge************************************************ #
# ********PROBLEM 1*********************************************************** #
# Given a linked list of integers, remove any nodes from the linked list that have values that have previously occurred in the linked list. Your function should return a reference to the head of the updated linked list.

# Example:
# Input: (3) -> (4) -> (3) -> (2) -> (6) -> (1) -> (2) -> (6) -> N
# Output: (3) -> (4) -> (2) -> (6) -> (1) -> N
# Explanation: The input list contains redundant nodes (3), (6), and (2), so those should be removed from the list.

# Submission:
# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def condense_linked_list(node):
    store = {node.value}
    head = node
    
    while node.next is not None:
        if node.next.value not in store:
            store.add(node.next.value)
            node = node.next
        else:
            cur = node.next
            node.next = cur.next
            cur.next = None
    
    return head


