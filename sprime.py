"""
ID: seishin1
LANG: PYTHON3
TASK: sprime
"""
from math import sqrt


prime_sieve = [2, 3, 5, 7]
sieve_max_number_checked = 9


def extend_prime_sieve(y):  # Extend the sieve to have primes up to y. y > 7, y > sieve_max_number_checked.
  global prime_sieve
  global sieve_max_number_checked

  if y % 2 == 0:
    y += 1  # Should be odd.

  for candidate in range(sieve_max_number_checked, y, 2):
    sqrt_y = int(sqrt(y))
    for prime in prime_sieve:
      if prime > sqrt_y:
        break
      if candidate % prime != 0:
        prime_sieve.append(candidate)

  sieve_max_number_checked = y


def is_prime(x):
  global prime_sieve
  global sieve_max_number_checked

  if x in prime_sieve:
    return True

  sqrt_x = int(sqrt(x))
  if sieve_max_number_checked < sqrt_x:
    extend_prime_sieve(sqrt_x)

  for divisor in prime_sieve:
    if divisor > sqrt_x:
      break
    if x % divisor == 0:
      return False
  return True


def generate_superprimes(n):  # 1 <=N<=8
  current_primes = [2, 3, 5, 7]  # Single digit primes

  for _ in range(2, n + 1):  # 2 to n, inclusive. Prime-length.
    next_primes = list()
    for prime in current_primes:
      # Update: Could have skipped 5. Numbers ending in 5 are divisible by 5.
      for candidate_digit in range(1, 10, 2):  # 1, 3, 5, 7, 9
        candidate = prime*10 + candidate_digit
        if is_prime(candidate):
          next_primes.append(candidate)

    current_primes = next_primes

  return current_primes


fin = open('sprime.in', 'r')
fout = open('sprime.out', 'w')

n = int(fin.readline().strip())

sprimes = generate_superprimes(n)
print(sprimes)

fout.write('\n'.join(str(x) for x in sprimes) + '\n')

fin.close()
fout.close()

# if(__name__ == '__main__'): # Local debug
#  import sys
#  import os
#  print('type {}.out'.format(sys.argv[0].lstrip('.\').split('.')[0])) #Debug
#  os.system('type {}.out'.format(sys.argv[0].lstrip('.\').split('.')[0]))

