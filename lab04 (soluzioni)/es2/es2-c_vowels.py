##
#  Print a string where the vowels have been replaced with underscores.
#

# Read input from the user.
input_str = input("Enter a string: ")

# Check each character.  If it is a vowel display an underscore instead of
# the character.
for ch in input_str:
    if ch in "aeiouAEIOU":  # or: ch.lower() in "aeiou"
        print("_", end="")
    else:
        print(ch, end="")

# Or using replace()
# for ch in "aeiouAEIOU":
#   input_str = input_str.replace(ch,"_")
# print(input_str)

print()

