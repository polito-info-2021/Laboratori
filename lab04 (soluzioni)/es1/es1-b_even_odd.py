##
#   Print the number of even values and the number of odd values entered by
#   the user.
#

# Read the first input value from the user.
input_str = input("Enter an integer (blank line to quit): ")

# As long as the user hasn't entered a blank line, convert the input to an
# integer and determine if it is even or odd.
even = 0
odd = 0
while input_str != "":
    value = int(input_str)

    if value % 2 == 0:
        even = even + 1
    else:
        odd = odd + 1

    input_str = input("Enter an integer (blank line to quit): ")

# Display the results.
print(f"The user entered {even} even values and {odd} odd values.")
