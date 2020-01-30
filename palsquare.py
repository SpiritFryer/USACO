"""
ID: seishin1
LANG: PYTHON3
TASK: palsquare
"""
fin = open('palsquare.in', 'r')
fout = open('palsquare.out', 'w')

m = {
  0: '0',
  1: '1',
  2: '2',
  3: '3',
  4: '4',
  5: '5',
  6: '6',
  7: '7',
  8: '8',
  9: '9',
  10: 'A',
  11: 'B',
  12: 'C',
  13: 'D',
  14: 'E',
  15: 'F',
  16: 'G',
  17: 'H',
  18: 'I',
  19: 'J',
  20: 'K'
}


def base_convert(x, base):
  output = []
  while x > 0:
    output.append(x % base)
    x = int(x / base)
    #print(x, rem)
  #print(x, base, output)
  return str(''.join(m[x] for x in output[::-1]))


START = 1
END = 300

base = int(fin.readline().strip())

output = []
for i in range(START, END + 1):
  sq = i ** 2
  converted = base_convert(sq, base)
  if(converted == converted[::-1]):
    output.append((base_convert(i, base), converted))

print('\n'.join(x[0] + ' ' + x[1] for x in output) + '\n')
fout.write('\n'.join(x[0] + ' ' + x[1] for x in output) + '\n')

# print("#####################")
# print(base_convert(123, 2))
# print(base_convert(123, 8))
# print(base_convert(123, 16))

fin.close()
fout.close()

# if(__name__ == '__main__'): # Local debug
#  import sys
#  import os
#  print('type {}.out'.format(sys.argv[0].lstrip('.\').split('.')[0])) #Debug
#  os.system('type {}.out'.format(sys.argv[0].lstrip('.\').split('.')[0]))

