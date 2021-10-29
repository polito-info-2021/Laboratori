##
#  Read a word from the user, and display its characters in reverse order.
#

# a.
# Read input from the user.
input_str = input("Enter a word: ")

# String length
str_len = len(input_str)

# Display the result.
print(f"{input_str} reversed is {input_str[str_len::-1]}") # with string slicing

print()

