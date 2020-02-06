"""
ID: seishin1
LANG: PYTHON3
TASK: pprime
"""
from math import sqrt

# Assumes prime_sieve contains at least [2, 3, 5, 7, 11, 13]. Uses globals: prime_sieve, max_prime.
def is_prime(x):
  # global max_prime
  # global prime_sieve

  if x <= 1:
    return False

  if x == 2:
    return True

  if x % 2 == 0:
    return False

  sqrt_x = int(sqrt(x))
  for divisor in range(3, sqrt_x + 2, 2):
    if x % divisor == 0:
      return False

  return True


# print(is_prime(0))
# print(is_prime(1))
# print(is_prime(2))
# print(is_prime(3))
# print(is_prime(4))
# print(is_prime(5))
# print(is_prime(31))
# print(is_prime(37))


fin = open('pprime.in', 'r')
fout = open('pprime.out', 'w')

a,b = map(int, fin.readline().split())

# Generate palindromes and check them for primality. BFS all palindromes up to b.
# states = [str(x) for x in range(10)] + \
#          [str(x) + str(x) for x in range(10)]  # ['0', '1', ..., '8', '9', '00', '11', ..., '88', '99']
# while states:
#   palindrome = states.pop(0)
#   if is_prime(int(palindrome)):
#     print(palindrome)
#     fout.write(palindrome + '\n')
#
#   for x in range(1, 10):  # Can't have leading 0 in a palindrome.
#     print('Adding', str(x) + palindrome + str(x))
#     states.append(str(x) + palindrome + str(x))

# Generate palindromes and check them for primality.

pals = [str(x) for x in range(10)] + [str(x)+str(x) for x in range(10)]
#print(pals)

finished = False
for x in pals:
  #print('Trying', x)
  x_int = int(x)
  if x_int < a:
    continue
  if x_int > b:
    finished = True
    break
  if is_prime(x_int):
    #print(x)
    fout.write(x + '\n')

half_count = 1
if not finished:
  while True:
    new_pals = list()
    finished = False
    half_count *= 10

    for half_index in range(1, 3):  # 1, 2
      for x in range(10):
        for p in pals[0 if half_index == 1 else half_count
                      : half_count * half_index]:
          new_p = str(x) + p + str(x)
          #print('Trying', new_p)

          if x != 0:
            new_p_int = int(new_p)

            if new_p_int > b:
              finished = True
              break

            if is_prime(new_p_int):
              if new_p_int >= a:
                #print(new_p)
                fout.write(new_p + '\n')

          new_pals.append(new_p)
        if finished:
          break
      if finished:
        break
    if finished:
      break
    pals = new_pals


# 0 1 2 3 4 5 6 7 8 9 |
# 00 11 22 33 44 55 66 77 88 99 |

# 000 010 ... 090 ... 101 111 121 131 141 151 161 171 181 191 202 212 222 ... 989 999 |
# 0000 0110 ... 0990 ... 1001 1111 1221 ... 1991 2002 2112 ... 9889 9999 |

# 00000 00100 ... 09990 ... 10001 ... 99899 99999 |

# print(''.join(str(prime) + '\n' if prime >= a else '' for prime in pprimes), end='')
# fout.write(''.join(str(prime) + '\n' if prime >= a else '' for prime in pprimes))

fin.close()
fout.close()

# if(__name__ == '__main__'): # Local debug
#  import sys
#  import os
#  print('type {}.out'.format(sys.argv[0].lstrip('.\').split('.')[0])) #Debug
#  os.system('type {}.out'.format(sys.argv[0].lstrip('.\').split('.')[0]))

