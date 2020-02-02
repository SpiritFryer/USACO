"""
ID: seishin1
LANG: PYTHON3
TASK: skidesign
"""

TAX_LIMIT = 17

fin = open('skidesign.in', 'r')
fout = open('skidesign.out', 'w')

n = int(fin.readline().strip())
hills = list(int(x.strip()) for x in fin)
print(hills)

hills = sorted(hills)
print(hills)

smallest_limit = hills[0] + TAX_LIMIT
largest_limit = hills[-1] - TAX_LIMIT
if hills[0] >= largest_limit and hills[-1] <= smallest_limit:  # Nothing to do
  print('Largest <= smallest,', largest_limit, smallest_limit)
  min_cost = 0
else:
  min_cost = None
  min_height = hills[0]
  max_height = hills[0] + TAX_LIMIT
  # Overall time complexity: O(t n).
  while max_height <= hills[-1]:  # TAX_LIMIT = t. Worst-case: t to 100. (For us: 17 to 100.) Loop: O(t), for us O(1)
    # All hills must fall within [min_height, max_height] range of heights.
    cost = 0
    for h in hills:  # Loop: O(n)
      if h < min_height:
        cost += (min_height - h) ** 2
      elif h > max_height:
        cost += (h - max_height) ** 2

    print('Updating min_cost:', cost, min_cost, min_height, max_height)
    min_cost = min(cost, min_cost if min_cost is not None else cost)  # TODO Is there a way to micro-optimize this?

    min_height += 1
    max_height += 1

print(min_cost)
fout.write(str(min_cost) + '\n')

fin.close()
fout.close()

# if(__name__ == '__main__'): # Local debug
#  import sys
#  import os
#  print('type {}.out'.format(sys.argv[0].lstrip('.\').split('.')[0])) #Debug
#  os.system('type {}.out'.format(sys.argv[0].lstrip('.\').split('.')[0]))

# OLD
# Try cost by raising
# cost_raise = 0
# for i in range(len(hills)):
#   if hills[-1] - hills[i] > 17:
#     print('Raising hill #', i, ' (', hills[i], ') Cost:', (hills[-1] - hills[i] - 17) ** 2, sep='')
#     cost_raise += (hills[-1] - hills[i] - 17) ** 2
#   else:
#     break
#
# # Try cost by lowering
# cost_lower = 0
# for i in range(len(hills) - 1, -1, -1):
#   print('Lowering hill #', i, ' (', hills[i], ') Cost:', (hills[i] - hills[0] - 17) ** 2, sep='')
#   if hills[i] - hills[0] > 17:
#     cost_lower += (hills[i] - hills[0] - 17) ** 2
#   else:
#     break
#
# # Choose the lower
# print(cost_raise, cost_lower)
# cost = min(cost_raise, cost_lower)