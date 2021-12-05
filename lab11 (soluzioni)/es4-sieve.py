##
#  Implement the sieve of Eratosthenes.
#
from math import sqrt, floor

# Read input from the user.
n = int(input("Enter a positive integer: "))

# Start with all numbers from 2 to n.
primes = set(range(2, n + 1))
for i in range(2, floor(sqrt(n)) + 1):
    for j in range(i**2, n+1, i):
        primes.discard(j)

# Display primes.
print("The primes less than or equal to", n, "are:")
for p in sorted(primes):
    print(" ", p)

