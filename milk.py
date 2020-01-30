"""
ID: seishin1
LANG: PYTHON3
TASK: milk
"""
fin = open('milk.in', 'r')
fout = open('milk.out', 'w')

n,m = map(int, fin.readline().split())

farmers = []
for _ in range(m):  # O(m * O(1))
  farmers.append(tuple(map(int, fin.readline().split())))

print(farmers)
print(sorted(farmers))

cost = 0
for farmer in sorted(farmers):  # Sort: O(m log m). Loop: O(m).
  if(farmer[1] > n):
    #print("Ending w/ farmer:", farmer)
    cost += n * farmer[0]
    break
  else:
    n -= farmer[1]
    cost += farmer[1] * farmer[0]
    #print("Processing farmer:", farmer, "New n:", n, "New cost:", cost)

print(cost)
fout.write(str(cost) + '\n')

fin.close()
fout.close()

# if(__name__ == '__main__'): # Local debug
#  import sys
#  import os
#  print('type {}.out'.format(sys.argv[0].lstrip('.\').split('.')[0])) #Debug
#  os.system('type {}.out'.format(sys.argv[0].lstrip('.\').split('.')[0]))

