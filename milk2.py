"""
ID: seishin1
LANG: PYTHON3
TASK: milk2
"""
fin = open('milk2.in', 'r')
fout = open('milk2.out', 'w')

# Input: [(700, 1200), (101, 1001), (1500, 2000), (400, 1000), (300, 1000), (100, 101), (1500, 2100), (1500, 2000)]
# 700.12 101.1001 1500.2 400.1 300.1 100.101 1500.21 1500.2

n = int(fin.readline().strip())

times = []
for line in fin.readlines():
  times.append(tuple(map(int, line.strip().split())))
print("Input:", times)

#times = sorted(times, key=lambda x: str(x[0]) + '.' + str(x[1]))
times = sorted(times)
print("Sorted:", times)

# Trim and keep track of the lengths
yes_milk_max = 0
no_milk_max = 0
i = 0
while i < len(times) - 1:
  if times[i][1] >= times[i + 1][0]:  # Current ending time >= next starting time, i.e. milking periods overlap
    if times[i + 1][1] > times[i][1]:  # Next ending time > current ending time
      times.insert(i, (times[i][0], times[i + 1][1]))
      times.pop(i + 1)
      times.pop(i + 1)
    else:  # Next ending time <= current ending time
      times.pop(i + 1)
  else:
    if i < len(times) - 1:
      no_milk_max = max(no_milk_max, times[i + 1][0] - times[i][1])
    i += 1
print("Trimmed:", times)

for time in times:  # Find longest consecutive milking time (at least 1 cow)
  yes_milk_max = max(yes_milk_max, time[1] - time[0])

print(yes_milk_max, no_milk_max)
fout.write(str(yes_milk_max) + ' ' + str(no_milk_max) + '\n')

fin.close()
fout.close()

# if(__name__ == '__main__'): # Local debug
#  import sys
#  import os
#  print('type {}.out'.format(sys.argv[0].lstrip('.\').split('.')[0])) #Debug
#  os.system('type {}.out'.format(sys.argv[0].lstrip('.\').split('.')[0]))

