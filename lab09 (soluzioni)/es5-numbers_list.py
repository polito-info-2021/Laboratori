# Exercise "list of numbers"

sequence = input('Insert a list of numbers (separated by :) ')

numbers_as_strings = sequence.split(':')

numbers = []
for s in numbers_as_strings:
    n = int(s)
    numbers.append(n)

print(numbers)

# all except min and max
numbers_without_min_max = list(numbers)
numbers_without_min_max.remove(min(numbers_without_min_max))
numbers_without_min_max.remove(max(numbers_without_min_max))
for i in range(len(numbers_without_min_max)):
    numbers_without_min_max[i] = str(numbers_without_min_max[i])
print(':'.join(numbers_without_min_max))

# only even numbers
numbers_even = []
for n in numbers:
    if n % 2 == 0:
        numbers_even.append(n)
for i in range(len(numbers_even)):
    numbers_even[i] = str(numbers_even[i])
print(':'.join(numbers_even))

# only 2-digit numbers
# may work directly on the list of strings
numbers_2digits_as_string = []
for s in numbers_as_strings:
    if len(s) == 2:
        numbers_2digits_as_string.append(s)
print(':'.join(numbers_2digits_as_string))
