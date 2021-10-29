##
#  Read a word from the user, and display its characters in reverse order.
#
# b.
# Read input from the user.
input_str = input("Enter a word: ")

for ch in "aeiou":
  input_str = input_str.replace(ch, '')

# String length
str_len = len(input_str)

# Reverse
input_str[str_len::-1]
# Display the result.
print(input_str)

print()

