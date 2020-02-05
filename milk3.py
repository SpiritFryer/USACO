"""
ID: seishin1
LANG: PYTHON3
TASK: milk3
"""
# Actions at each step:
#   Pour x y: Pours from x to y, until either x is empty or y is full.

# Pour options:
#   Pour a b
#   Pour a c
#   Pour b a
#   Pour b c
#   Pour c a
#   Pour c b


def pour(x, y, milks, caps):  # 0 <= x, y <= 2. x != y.
  # We will be pouring from x to y until either:
  # 1. x is empty.
  # 2. y is full.
  # Given caps[x] and caps[y], we can identify when 1. or 2. happens, as follows:
  # 1. caps[y] - milks[y] >= milks[x]
  # 2. caps[y] - milks[y] < milks[x]
  new_milks = list(milks)
  if caps[y] - milks[y] >= milks[x]:  # x is empty.
    new_milks[x] = 0
    new_milks[y] += milks[x]
  else:  # y is full. I.e.: caps[y] - milks[y] < milks[x].
    new_milks[x] -= caps[y] - milks[y]
    new_milks[y] = caps[y]

  return new_milks

#debug = -1  # Todo comment out
def dfs_milk(milks, caps, encountered, c_amounts):
  #global debug  # Todo comment out
  #debug += 1  # Todo comment out
  #print('  ' * debug, 'Searching', milks, encountered, c_amounts)  # Todo comment out

  if (milks[0], milks[1], milks[2]) in encountered:
    return
  else:
    encountered.add((milks[0], milks[1], milks[2]))

  if milks[0] == 0:
    c_amounts.add(milks[2])

  # Try all options
  dfs_milk(pour(0, 1, milks, caps), caps, encountered, c_amounts)
  #debug -= 1  # Todo comment out
  dfs_milk(pour(0, 2, milks, caps), caps, encountered, c_amounts)
  #debug -= 1  # Todo comment out
  dfs_milk(pour(1, 0, milks, caps), caps, encountered, c_amounts)
  #debug -= 1  # Todo comment out
  dfs_milk(pour(1, 2, milks, caps), caps, encountered, c_amounts)
  #debug -= 1  # Todo comment out
  dfs_milk(pour(2, 0, milks, caps), caps, encountered, c_amounts)
  #debug -= 1  # Todo comment out
  dfs_milk(pour(2, 1, milks, caps), caps, encountered, c_amounts)
  #debug -= 1  # Todo comment out




fin = open('milk3.in', 'r')
fout = open('milk3.out', 'w')

a,b,c = map(int, fin.readline().split())

milks = [0, 0, c]
caps = (a, b, c)
encountered = set()
c_amounts = set()  # When a is empty.
dfs_milk(milks, caps, encountered, c_amounts)

c_amounts = sorted(list(c_amounts))
print(c_amounts)

fout.write(' '.join(str(x) for x in c_amounts) + '\n')

fin.close()
fout.close()

# if(__name__ == '__main__'): # Local debug
#  import sys
#  import os
#  print('type {}.out'.format(sys.argv[0].lstrip('.\').split('.')[0])) #Debug
#  os.system('type {}.out'.format(sys.argv[0].lstrip('.\').split('.')[0]))

