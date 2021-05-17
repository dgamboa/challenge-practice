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

def amendTheSentence(s):
    store = s[0].lower()
    
    for c in s[1:]:
        if ord(c) > 90:
            store += c
        else: 
            store += " "
            store += c.lower()
    
    return store

def amendTheSentence(s):
    return " ".join(re.findall(r"[A-Za-z][a-z]*", s)).lower()
