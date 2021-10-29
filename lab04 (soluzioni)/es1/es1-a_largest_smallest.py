##
#  Print the smallest and largest values entered by the user.  The user will
#  enter a blank line to quit.
#

# Read the first input value from the user.
input_str = input("Enter an integer (blank line to quit): ")

# If the first value was an integer, process it and the remaining input values.
# Otherwise an appropriate error message is displayed.
if input_str != "":
    value = int(input_str)
    smallest = value
    largest = value

    # As long as the user hasn't entered a blank line, convert the input to an
    # integer and determine if it is a new smallest or largest value.
    while input_str != "":
        value = int(input_str)

        if value < smallest:
            smallest = value
        if value > largest:
            largest = value

        input_str = input("Enter an integer (blank line to quit): ")

    # Display the results.
    print(f"The smallest value is {smallest} and the largest value is {largest}")

else:
    # Display an error message if no input values are provided.
    print("No input values were provided.")
