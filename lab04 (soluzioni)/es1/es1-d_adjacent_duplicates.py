##
#   Find the adjacent duplicates in the values entered by the user.
#

# Read the first value from the user, and save it as the previous value.
input_str = input("Enter an integer (blank line to quit): ")
prev = input_str

# Check each value read from the user.   
printed = False
while input_str != "":
    input_str = input("Enter an integer (blank line to quit): ")

    # If it matches the previous value and we have not already printed that the
    # value is a duplicate then display an appropriate message.
    if prev == input_str and not printed:
        print(f"{input_str} is a duplicate.")
        printed = True
    if prev != input_str:
        printed = False

    prev = input_str
