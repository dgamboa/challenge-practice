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
