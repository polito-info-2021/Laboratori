##
#  Print the uppercase letters in a string.
#

# Read input from the user.
input_str = input("Enter a string: ")

# Find and display the uppercase letters.
for ch in input_str:
    if "A" <= ch <= "Z":  # or: ch >= "A" and ch <= "Z"
        print(ch, end="")

print()
