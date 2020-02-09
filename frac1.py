"""
ID: seishin1
LANG: PYTHON3
TASK: frac1
"""


def gcd_recurse(a, b):
 if a == b:
   return a
 a, b = min(a, b), max(a, b)
 return gcd_recurse(a, b - a)


def gcd_iter_sub(a, b):
  curr_a, curr_b = a, b
  # print('gcd_iter:', curr_a, curr_b)
  while curr_a != curr_b:
    curr_a, curr_b = min(curr_a, curr_b), max(curr_a, curr_b)
    curr_b -= curr_a
    # print('  ', curr_a, curr_b)
  return curr_a


def gcd_iter_mod(a, b):
  curr_a, curr_b = a, b
  # print('gcd_iter:', curr_a, curr_b)
  while curr_b > 0:
    curr_a, curr_b = min(curr_a, curr_b), max(curr_a, curr_b)
    curr_b %= curr_a
    # print('  ', curr_a, curr_b)
  return curr_a


def reduced_fraction_form(numer, denom):
  num_gcd = gcd_iter_mod(numer, denom)
  # print('    gcd of', numer, denom, '=', num_gcd)
  return int(numer/num_gcd), int(denom/num_gcd)


fin = open('frac1.in', 'r')
fout = open('frac1.out', 'w')

n = int(fin.readline().strip())

nums = set()
nums.add((0, 1))
nums.add((1, 1))

for numer in range(1, n + 1):
  for denom in range(numer + 1, n + 1):
    # print('Trying:', numer, denom, end='')
    reduced_num = reduced_fraction_form(numer, denom)
    # print('  Reduced form:', reduced_num)
    if reduced_num not in nums:
      nums.add((reduced_num[0], reduced_num[1]))

list_nums = list(nums)
print(list_nums)

list_nums.sort(key=lambda x: x[0]/x[1])
print(list_nums)

print('\n'.join(str(x[0]) + '/' + str(x[1]) for x in list_nums))
fout.write('\n'.join(str(x[0]) + '/' + str(x[1]) for x in list_nums) + '\n')

fin.close()
fout.close()

# if(__name__ == '__main__'): # Local debug
#  import sys
#  import os
#  print('type {}.out'.format(sys.argv[0].lstrip('.\').split('.')[0])) #Debug
#  os.system('type {}.out'.format(sys.argv[0].lstrip('.\').split('.')[0]))

