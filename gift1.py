"""
ID: seishin1
LANG: PYTHON3
TASK: gift1
"""
fin = open('gift1.in', 'r')
fout = open('gift1.out', 'w')

np = int(fin.readline().strip())
#s1 = fin.readline().strip()

banks = {}
for _ in range(np):
  banks[fin.readline().strip()] = 0

#print(banks) #Debug

for _ in range(np):
  p = fin.readline().strip()
  amount, num_friends = map(int,fin.readline().split())
  #print(p, amount, num_friends) #Debug
  
  if num_friends == 0:
    banks[p] += amount
  else:
    banks[p] -= amount - (amount % num_friends)
  for _ in range(num_friends):
    banks[fin.readline().strip()] += int(amount / num_friends)

#print(banks) #Debug

for k, v in banks.items():
  fout.write(k + ' ' + str(v) + '\n')

fin.close()
fout.close()

if(__name__ == '__main__'): # Local debug
  import sys
  import os
  #print('type {}.out'.format(sys.argv[0].lstrip('.\\').split('.')[0])) #Debug
  os.system('type {}.out'.format(sys.argv[0].lstrip('.\\').split('.')[0]))

