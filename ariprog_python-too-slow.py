"""
ID: seishin1
LANG: PYTHON3
TASK: ariprog
"""
fin = open('ariprog.in', 'r')
fout = open('ariprog.out', 'w')

n = int(fin.readline())
m = int(fin.readline())
print(n, m)
# a, a+b, a+2b, ..., a+nb
# Each element must satisfy p^2 + q^2.

# Generate all p^2 + q^2, 0 <= p, q <= M
pqs = [True for _ in range(m**2 + m**2 + 1)]
pq_nums = []
# < O(m^2)
for p in range(m + 1):
  for q in range(p, m + 1):
    ## print(p, q, ':', p**2, q**2)
    curr = p**2 + q**2
    pqs[curr] = False  # Micro-optimization for loop later
    pq_nums.append(curr)
max_pq = 2 * m**2
#print(max_pq, pqs)
print(len(pq_nums), '\n', ','.join(str(x) for x in pq_nums), sep='')
pq_nums = sorted(pq_nums)
#print(len(pq_nums), pq_nums)

ans = []
print('Trying bs up to:', int(max_pq/(n - 1)) + 1)
loop_count = 0
for b in range(1, int(max_pq/(n - 1)) + 1):  # nb <= max_pq ... b <= max_pq/n
  #print('Trying b:', b)
  # if b == 24:
  #   # print('  b == 24, Trying as up to', max_pq - (n - 1)*b)
  a_limit = (max_pq - (n - 1)*b) + 1
  #print('    Trying as up to:', a_limit)
  #loop_count += a_limit  # TODO comment debug
  for a in pq_nums:  # a+nb <= max_pq ... a <= max_pq - nb
    if a > a_limit:
      break
    # print('Trying a/b:', a, b)
    good = True
    prod = b
    for i in range(1, n):
      # if a == 2 and b == 24:
      #  print('  a + b*', i, a + b*i, pqs[a + b*i], pqs[a + prod])
      if pqs[a + prod]:  # pqs contain True when it's not a bisquare
        good = False
        break
      prod += b
    if good:
      ans.append((a, b))

#print('Loop count:', loop_count)
print('\n'.join(str(x[0]) + ' ' + str(x[1]) for x in ans) if ans else 'NONE')
fout.write('\n'.join(str(x[0]) + ' ' + str(x[1]) for x in ans) + '\n' if ans else 'NONE\n')

fin.close()
fout.close()

# if(__name__ == '__main__'): # Local debug
#  import sys
#  import os
#  # print('type {}.out'.format(sys.argv[0].lstrip('.\').split('.')[0])) #Debug
#  os.system('type {}.out'.format(sys.argv[0].lstrip('.\').split('.')[0]))

