##
#  Count the number of digits in a string.
#

# Read input from the user.
input_str = input("Enter a string: ")

# Check each character.  If it is a digit, add it to the count.
count = 0
for ch in input_str:
    if ch.isdigit():  # or: "0" <= ch <= "9"
        count = count + 1

print(f"The string contains {count} digits.")
