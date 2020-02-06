"""
ID: seishin1
LANG: PYTHON3
TASK: pprime
"""
from math import sqrt

HARDCODED_TO = 13
prime_sieve = [2, 3, 5, 7, 11, 13]
pprimes = [2, 3, 5, 7, 11]


# Fills prime_sieve up to n with primes. Saves palindromic primes to pprimes.
# Assumes prime_sieve is filled up to 'HARDCODED_TO'. 'HARDCODED_TO' should be odd.
def pprime_sieve(n, prime_sieve, pprimes):
  if n <= HARDCODED_TO:
    return

  for x in range(HARDCODED_TO + 2, n, 2):
    # if x % 100001 == 0:
    #   print('  Trying x =', x)

    is_prime = True
    sqrt_x = sqrt(x)
    for prime in prime_sieve:
      if prime > sqrt_x:
        break

      if x % prime == 0:
        # print('    Divisible by', prime)
        is_prime = False
        break

    if is_prime:
      # print('    is a prime!')
      prime_sieve.append(x)
      if str(x) == str(x)[::-1]:
        pprimes.append(x)

  return


fin = open('pprime.in', 'r')
fout = open('pprime.out', 'w')

a,b = map(int, fin.readline().split())

pprime_sieve(b, prime_sieve, pprimes)
# print('Primes:', prime_sieve)
# print('Palindromic primes:', pprimes)

print(''.join(str(prime) + '\n' if prime >= a else '' for prime in pprimes), end='')
fout.write(''.join(str(prime) + '\n' if prime >= a else '' for prime in pprimes))

fin.close()
fout.close()

# if(__name__ == '__main__'): # Local debug
#  import sys
#  import os
#  print('type {}.out'.format(sys.argv[0].lstrip('.\').split('.')[0])) #Debug
#  os.system('type {}.out'.format(sys.argv[0].lstrip('.\').split('.')[0]))

