# Project Euler #3: https://projecteuler.net/problem=3

import math

def is_prime_number(n):
# Returns boolean that indicates if the given value is a prime number

  if float(n).is_integer() is not True:
    return False
  elif n <= 1:
    return False
  else:
    for i in range(2, int(n)):
      if (n % i) == 0:
        return False
        break

  return True

def get_next_prime_number(n):
  # Returns the first prime number that comes after "n"

  if (is_prime_number(n) is not True):
    raise Exception('Can only get next prime number if prime number is given. %s is not a prime number' % n)

  i = n + 1
  while i:
    if is_prime_number(i):
      return i
    else:
      i += 1

def get_prime_factors(n):
  # Returns the list factors that consist of prime numbers only

  if (is_prime_number(n)):
    raise Exception('Cannot get prime factors for prime number: %s' % n)

  factors = []
  n_decomposed = n

  i = 1

  while n_decomposed and n_decomposed > 0:
    # Start discovering the prime factors by decomposing "n"

    square_root = math.sqrt(n_decomposed)
    prime_number = 2

    while prime_number <= square_root and n_decomposed and n_decomposed > 0:
      devision = float(n_decomposed) / prime_number

      if devision.is_integer():
        # Devision is full number and prime number should be added to list of factors

        factors.append(prime_number)
        n_decomposed = int(n_decomposed / prime_number)

        if (is_prime_number(devision)):
          # Devision is prime number, which indicates all factors have been found

          factors.append(n_decomposed)
          n_decomposed = 0

        break

      # Try next prime number
      prime_number = get_next_prime_number(prime_number)

  return factors

n = 600851475143
factors = get_prime_factors(n)

print('The largest prime factor for %s is %s. Full list is: %s' % (n, max(factors), factors))
