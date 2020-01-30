"""
ID: seishin1
LANG: PYTHON3
TASK: dualpal
"""
fin = open('dualpal.in', 'r')
fout = open('dualpal.out', 'w')

base_chars = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
def base_convert(x, base):
  output = []
  while x > 0:
    output.append(x % base)
    x = int(x / base)

  return ''.join(base_chars[d] for d in output[::-1])


# print('##############')
# print(base_convert(10, 2))
# print(base_convert(10, 8))
# print(base_convert(10, 16))


n, s = map(int, fin.readline().strip().split())
# print(n, s)
COUNT_REQ = 2

i = s + 1
output = []
while True:
  pal_count = 0
  for base in range(2, 11):
    converted = base_convert(i, base)
    if converted == converted[::-1]:
      pal_count += 1
      if pal_count >= COUNT_REQ:
        output.append(i)
        break
  if len(output) >= n:
    break
  i += 1

print('\n'.join(str(x) for x in output))
fout.write('\n'.join(str(x) for x in output) + '\n')

fin.close()
fout.close()

# if(__name__ == '__main__'): # Local debug
#  import sys
#  import os
#  print('type {}.out'.format(sys.argv[0].lstrip('.\').split('.')[0])) #Debug
#  os.system('type {}.out'.format(sys.argv[0].lstrip('.\').split('.')[0]))

