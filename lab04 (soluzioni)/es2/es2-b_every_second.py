##
#  Print every second letter in a string.
#

# Read input from the user.
input_str = input("Enter a string: ")

# Display every second letter.
for i in range(1, len(input_str), 2):
    print(input_str[i], end='')

print()
