# **************************************************************************** #
# Enclose in Brackets
# **************************************************************************** #
# Given a string, enclose it in round brackets.

# Example

# For inputString = "abacaba", the output should be
# encloseInBrackets(inputString) = "(abacaba)".
def encloseInBrackets(inputString):
    return "(" + inputString + ")"

# **************************************************************************** #
# Proper Noun Correction
# **************************************************************************** #
# Proper nouns always begin with a capital letter, followed by small letters.

# Correct a given proper noun so that it fits this statement.

# Example

# For noun = "pARiS", the output should be
# properNounCorrection(noun) = "Paris";
# For noun = "John", the output should be
# properNounCorrection(noun) = "John".
def properNounCorrection(noun):
    return noun[0].capitalize() + noun[1:].casefold()
