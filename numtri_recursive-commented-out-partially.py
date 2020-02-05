"""
ID: seishin1
LANG: PYTHON3
TASK: numtri
"""


# Needs max_depth > 1. # Recursion depth exceeded for max_depth >= 998.
def dfs_binary_tree(triangle, current_depth, current_index, max_depth, current_sum, max_sums):
  if current_depth == max_depth - 1:
    # print('  ' * current_depth, current_depth, current_index, 'Reached bottom, returning ',
    #       current_sum + triangle[current_depth][current_index] + max(
    #         triangle[current_depth + 1][current_index],
    #         triangle[current_depth + 1][current_index + 1])
    #       )
    return current_sum + triangle[current_depth][current_index] + max(
      triangle[current_depth + 1][current_index],
      triangle[current_depth + 1][current_index + 1]
    )

  if max_sums[current_depth + 1][current_index] == -1:
    #print('  ' * current_depth, current_depth + 1, current_index, 'max_sums not found, calculating')
    max_sums[current_depth + 1][current_index] = \
      dfs_binary_tree(triangle, current_depth + 1, current_index, max_depth, current_sum, max_sums)
  # else:
  #   print('  ' * current_depth, current_depth + 1, current_index, 'available:',
  #         max_sums[current_depth + 1][current_index])

  if max_sums[current_depth + 1][current_index + 1] == -1:
    #print('  ' * current_depth, current_depth + 1, current_index + 1, 'max_sums not found, calculating')
    max_sums[current_depth + 1][current_index + 1] = \
      dfs_binary_tree(triangle, current_depth + 1, current_index + 1, max_depth, current_sum, max_sums)
  # else:
  #   print('  ' * current_depth, current_depth + 1, current_index + 1, 'available:',
  #         max_sums[current_depth + 1][current_index + 1])

  # print('  ' * current_depth, current_depth, current_index, 'Returning ',
  #       max(
  #         max_sums[current_depth + 1][current_index],
  #         max_sums[current_depth + 1][current_index + 1]
  #       ))
  return triangle[current_depth][current_index] + max(
    max_sums[current_depth + 1][current_index],
    max_sums[current_depth + 1][current_index + 1]
  )


fin = open('numtri.in', 'r')
fout = open('numtri.out', 'w')

n = int(fin.readline().strip())

rows = [list(map(int, line.split())) for line in fin]
#print('\n'.join(' '.join(str(x) for x in row) for row in rows))

max_sums = []
for i in range(n):
  max_sums.append([-1] + [-1 for _ in range(i)])
#print(max_sums)

if len(rows) == 1:
  max_sum = rows[0][0]
else:
  #max_sum = dfs_binary_tree(rows, 0, 0, n - 1, 0, max_sums)
  max_sum = "whatever"
#print('\n'.join(' '.join(str(x) for x in row) for row in max_sums))

max_sums2 = []
for i in range(n - 1):
  max_sums2.append([-1] + [-1 for _ in range(i)])

max_sums2.append([x for x in rows[-1]])
for i in range(len(rows) - 2, -1, -1):
  for j in range(len(rows[i])):
    max_sums2[i][j] = rows[i][j] + max(max_sums2[i + 1][j], max_sums2[i + 1][j + 1])
max_sum2 = max_sums2[0][0]

print(max_sum)
print(max_sum2)
fout.write(str(max_sum) + '\n')

fin.close()
fout.close()

# if(__name__ == '__main__'): # Local debug
#  import sys
#  import os
#  #print('type {}.out'.format(sys.argv[0].lstrip('.\').split('.')[0])) #Debug
#  os.system('type {}.out'.format(sys.argv[0].lstrip('.\').split('.')[0]))

