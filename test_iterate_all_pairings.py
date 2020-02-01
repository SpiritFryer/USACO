#from itertools import *
from math import factorial

N = 24

o = ''
for i in range(N):
  o += chr(ord('A') + i)
print(o)
o = [x for x in o]
print(o)


def dfs_pairs(stack, pairs):  # n = len(stack). Number of recursive calls: O()
  #global num_calls
  if not stack:
    yield pairs
  else:
    pair_left = stack.pop(0)
    for i in range(len(stack)):  # Loop iterations: O(n - 1). Each iteration recurses with n - 2
      new_stack = list(stack)
      pair_right = new_stack.pop(i)

      new_pairs = list(pairs)
      new_pairs.append((pair_left, pair_right))

      #num_calls += 1
      #if(num_calls % 10000000 == 0):
      #  print("Another 10M:", num_calls)
      yield from dfs_pairs(new_stack, new_pairs)


for i in range(len(o)):
  count = 0
  num_calls = 0
  for x in dfs_pairs(list(o[:i]), []):
    count += 1

  adjusted_factorial = 1
  x = i - 1
  summed_factorial = x
  while x > 1:
    adjusted_factorial *= x
    summed_factorial += adjusted_factorial
    x -= 2
  print(i, count, num_calls, adjusted_factorial, summed_factorial)