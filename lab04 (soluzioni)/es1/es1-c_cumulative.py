##
#  Display the cumulative totals of the values entered by the user.
#

# Read input from the user.
input_str = input("Enter an integer (blank line to quit): ")

# Add each value to the total as it is read, and display the cumulative total.
total = 0
while input_str != "":
    value = int(input_str)
    total = total + value
    print(f"The cumulative total is {total}")

    input_str = input("Enter an integer (blank line to quit): ")
