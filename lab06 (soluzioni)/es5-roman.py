"""
Convert from Roman numerals to a decimal number.
"""


def main():
    print(roman_to_decimal("I"))
    print(roman_to_decimal("MCMLXXVIII"))
    print(roman_to_decimal("MMMCMXCIX"))
    print(roman_to_decimal("MMMIM"))
    print(roman_to_decimal("MMXXI"))


def roman_to_decimal(roman):
    """
    Convert a string of Roman numerals to decimal.

    :param roman: the string of numerals to convert
    :return: the decimal equivalent of r
    """
    total = 0
    r = roman.upper()  # make a copy of the argument, so that we may modify its value
    while r != "":
        if len(r) == 1 or convert_digit(r[0]) >= convert_digit(r[1]):
            total = total + convert_digit(r[0])
            r = r[1:]  # eliminate 1st character
        else:
            total = total + (convert_digit(r[1]) - convert_digit(r[0]))
            r = r[2:]  # eliminate 1st and 2nd characters
    return total


def convert_digit(r):
    """
    Convert a *single* Roman numeral character to decimal.

    :param r: the character to convert
    :return: the decimal equivalent of r
    """
    if r == "I":
        return 1
    if r == "V":
        return 5
    if r == "X":
        return 10
    if r == "L":
        return 50
    if r == "C":
        return 100
    if r == "D":
        return 500
    if r == "M":
        return 1000


# Call the main function.
main()
