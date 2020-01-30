"""
ID: seishin1
LANG: PYTHON3
TASK: ride
"""
fin = open ('ride.in', 'r')
fout = open ('ride.out', 'w')

#x,y = map(int, fin.readline().split())
comet = fin.readline().rstrip()
group = fin.readline().rstrip()

a = ord('A') - 1
comet_num = 1
for c in comet:
  comet_num = (comet_num * (ord(c) - a)) % 47

group_num = 1
for c in group:
  group_num = (group_num * (ord(c) - a)) % 47

if(comet_num == group_num):
  fout.write('GO' + '\n')
else:
  fout.write('STAY' + '\n')
fout.close()

if(__name__ == '__main__'): # Local debug
  import sys
  import os
  os.system('type {}.out'.format(sys.argv[0].split('.')[0]))

