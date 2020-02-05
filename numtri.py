"""
ID: seishin1
LANG: PYTHON3
TASK: numtri
"""

fin = open('numtri.in', 'r')
fout = open('numtri.out', 'w')

n = int(fin.readline().strip())
rows = [list(map(int, line.split())) for line in fin]
#print('\n'.join(' '.join(str(x) for x in row) for row in rows))

max_sums = []
for i in range(n - 1):
  max_sums.append([-1] + [-1 for _ in range(i)])

max_sums.append([x for x in rows[-1]])
for i in range(len(rows) - 2, -1, -1):
  for j in range(len(rows[i])):
    max_sums[i][j] = rows[i][j] + max(max_sums[i + 1][j], max_sums[i + 1][j + 1])
max_sum = max_sums[0][0]

print(max_sum)
fout.write(str(max_sum) + '\n')

fin.close()
fout.close()

# if(__name__ == '__main__'): # Local debug
#  import sys
#  import os
#  #print('type {}.out'.format(sys.argv[0].lstrip('.\').split('.')[0])) #Debug
#  os.system('type {}.out'.format(sys.argv[0].lstrip('.\').split('.')[0]))

