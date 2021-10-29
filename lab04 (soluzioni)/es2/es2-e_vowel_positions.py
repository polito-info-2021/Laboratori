##
#  Print the positions of all of the vowels in the string.
#

# Read input from the user.
input_str = input("Enter a string: ")

# Check each character.  If it is a vowel display its position.
print("The vowels are at positions: ", end="")
for i in range(0, len(input_str)):
    if input_str[i] in "aeiouAEIOU":
        print(i + 1, end=" ")

print()
