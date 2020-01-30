"""
ID: seishin1
LANG: PYTHON3
TASK: crypt1
"""
from itertools import product

# current_perm: list, current permutation, list of numbers 0 to len(options) - 1, indicating which numbers we picked
# options: list
# Returns next permutation, given current_perm using list of options
# Returns None if we were at the last permutation
# There are len(options) ^ permutation_length possible permutations.
def permute_next(options, permutation_length, *, current_perm=None):  # Worst-case: O(len(options))
  i = 0
  if current_perm is None:
    return [0 for _ in range(permutation_length)]
  new_perm = list(current_perm)
  new_perm[i] += 1
  while new_perm[i] == len(options):
    new_perm[i] = 0
    i += 1
    if i == permutation_length:
      return None
    new_perm[i] += 1
  return new_perm



def check_mult(m1, m2, m1_int, m2_int, check_digits):  # O(len(str(m1 * m2))
  # Full product
  product = str(m1_int * m2_int)
  if len(product) > 4:
    return 0
  for x in product:  # str(product)
    if x not in check_digits:
      return 0

  # Partial product #1
  product = str(m1_int * m2[1])
  if len(product) > 3:
    return 0
  for x in product:  # str(product)
    if x not in check_digits:
      return 0

  # Partial product #2
  product = str(m1_int * m2[0])
  if len(product) > 3:
    return 0
  for x in product:  # str(product)
    if x not in check_digits:
      return 0

  print("Good: ", m1, m2)
  return 1


fin = open('crypt1.in', 'r')
fout = open('crypt1.out', 'w')

_ = int(fin.readline().strip())
#digits = list(map(int, fin.readline().split()))
digits = [int(x) for x in fin.readline().split()]
check_digits = set(str(x) for x in digits)

print(digits)
print(check_digits)

current = permute_next(digits, 3)
three_digits = []
while current is not None:  # Generates all length 3 permutations. There n^3 of them. O(n^3)
  three_digits.append([digits[x] for x in current])
  current = permute_next(digits, 3, current_perm=current)
  
current = permute_next(digits, 2)
two_digits = []
while current is not None: # O(n^2)
  two_digits.append([digits[x] for x in current])
  current = permute_next(digits, 2, current_perm=current)

# print("Let's try this")
# for x in three_digits:
#   print(list(x))

# print(len(three_digits), list(list(x) for x in three_digits))
# print(len(two_digits), list(list(x) for x in two_digits))

ans = 0
# Loop: O(n ^ 3). Overall: O(n^3 * n^2) = O(n^5), 1 <= n <= 9. Worst-case: 9^5 = 59049. 900*90 = 81000.
for m1 in three_digits:  # First multiplicand --
  # for x in m1:
  #   print("Hello0", x)
  # print("HELLO?", m1)
  # print("HELLO2?", ''.join(str(x) for x in m1))
  m1_int = int(''.join(str(x) for x in m1))
  for m2 in two_digits:  # Second multiplicand -- Loop: O(len(digits) ^ 2)
    m2_int = int(''.join(str(x) for x in m2))
    ans += check_mult(m1, m2, m1_int, m2_int, check_digits)


'''Using itertools.product'''
# Loop: O(n ^ 3). Overall: O(n^3 * n^2) = O(n^5), 1 <= n <= 9. Worst-case: 9^5 = 59049. 900*90 = 81000.
ans2 = 0
for m1 in product(digits, repeat=3):  # First multiplicand -- itertools.product()
  # for x in m1:
  #   print("Hello0", x)
  # print("HELLO?", m1)
  # print("HELLO2?", ''.join(str(x) for x in m1))
  m1_int = int(''.join(str(x) for x in m1))
  for m2 in product(digits, repeat=2):  # Second multiplicand -- Loop: O(len(digits) ^ 2)
    m2_int = int(''.join(str(x) for x in m2))
    ans2 += check_mult(m1, m2, m1_int, m2_int, check_digits)


print(ans)
print(ans2)
fout.write(str(ans2) + '\n')

fin.close()
fout.close()

# if(__name__ == '__main__'): # Local debug
#  import sys
#  import os
#  print('type {}.out'.format(sys.argv[0].lstrip('.\').split('.')[0])) #Debug
#  os.system('type {}.out'.format(sys.argv[0].lstrip('.\').split('.')[0]))

