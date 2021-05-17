# ******************************************************************* #

# You have been given a string s, which is supposed to be a sentence. However, someone forgot to put spaces between the different words, and for some reason they capitalized the first letter of every word. Return the sentence after making the following amendments:

# Put a single space between the words.
# Convert the uppercase letters to lowercase.
# Example

# For s = "CodesignalIsAwesome", the output should be
# amendTheSentence(s) = "codesignal is awesome";
# For s = "Hello", the output should be
# amendTheSentence(s) = "hello".

# ******************************************************************* #

# With loop
def amendTheSentence(s):
    store = s[0].lower()
    
    for c in s[1:]:
        if ord(c) > 90:
            store += c
        else: 
            store += " "
            store += c.lower()
    
    return store

# With regex
def amendTheSentence(s):
    return " ".join(re.findall(r"[A-Za-z][a-z]*", s)).lower()


# ******************************************************************* #

# Avoid using built-in functions to solve this challenge. Implement them yourself, since this is what you would be asked to do during a real interview.

# Implement a function that takes two strings, s and x, as arguments and finds the first occurrence of the string x in s. The function should return an integer indicating the index in s of the first occurrence of x. If there are no occurrences of x in s, return -1.

# Example

# For s = "CodefightsIsAwesome" and x = "IA", the output should be
# strstr(s, x) = -1;
# For s = "CodefightsIsAwesome" and x = "IsA", the output should be
# strstr(s, x) = 10.

# ******************************************************************* #

# Brute force with loop (not performant in all cases)
def strstr(s, x):
    if s == x:
        return 0
    
    for i, c in enumerate(s):
        if c == x[0]:
            for j in range(1, len(x)):
                if i + j > len(s) - 1 or s[i + j] != x[j]:
                    break
                
                if j == len(x) - 1:
                    return i
    
    return -1

# Performant solution (don't fully understand)
def findFirstSubstringOccurrence(s, x):

    ''' Find the first occurrances of @patt in @text
    '''
    patt = x
    text = s
    if not patt or not text: 
        return -1

    # First build the pattern lookup table
    tbl = [0] * (1 + len(patt))
    i = 1; j = 0;
    while i < len(patt):
        if patt[i] == patt[j]:
            i += 1; j += 1; tbl[i] = j
        elif 0 == j:
            i += 1
        else:
            j = tbl[j]
    
    # Search over the query text
    i = 0; j = 0;
    while i < len(text):
        if text[i] == patt[j]:
            i += 1; j += 1;
            if len(patt) == j:
                assert(text[i - len(patt): i] == patt)
                return i - len(patt)
        elif j == 0:
            i += 1
        else:
            j = tbl[j]

    return -1
