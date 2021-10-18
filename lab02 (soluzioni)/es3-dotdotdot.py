##
#  Print the first 3 letters of a string, followed by ..., followed by the 
#  last 3 letters of a string.
#

# Initialize the string.
word = "Mississippi"

# Length of the String
lenString = len(word)

# Display the result.
print(word[0] + word[1] + word[2] + '...' + word[lenString - 3] + word[lenString - 2] + word[lenString - 1])

# Alternative, by using string slices
print(word[0:3] + '...' + word[-3:])

# Alternative, by using f-strings
print(f"{word[0:3]}...{word[-3:]}")

# Alternative, by using %-formatting
print("%s%s%s...%s%s%s" % (word[0], word[1], word[2], word[lenString - 3], word[lenString - 2], word[lenString - 1]))

