"""
ID: seishin1
LANG: PYTHON3
TASK: namenum
"""
fin = open('namenum.in', 'r')
fout = open('namenum.out', 'w')

m = {  # Dictionary of mapping
  'A': '2',
  'B': '2',
  'C': '2',
  'D': '3',
  'E': '3',
  'F': '3',
  'G': '4',
  'H': '4',
  'I': '4',
  'J': '5',
  'K': '5',
  'L': '5',
  'M': '6',
  'N': '6',
  'O': '6',
  'P': '7',
  'Q': '?',
  'R': '7',
  'S': '7',
  'T': '8',
  'U': '8',
  'V': '8',
  'W': '9',
  'X': '9',
  'Y': '9',
  'Z': '?',
}


def valid(name, num):
  if len(name) != len(num):
    return False
  for i, c in enumerate(name):
    if m[c] != num[i]:
      return False
  return True
    

names = []
with open('dict.txt', 'r') as dict_in:
  for line in dict_in:
    names.append(line.strip())

num = fin.readline().strip()

# for i in range(8):
#   out = ''
#   for k, v in m.items():
#     if v == i + 2:
#       out += k + ','
#   print(str(i + 2) + ': ' + out)

print(names)
#print ('\n'.join(names))

valid_names = []
for name in names:
  if(valid(name, num)):
    valid_names.append(name)

print(valid_names)

if(valid_names):
  fout.write('\n'.join(valid_names) + '\n')
else:
  fout.write('NONE\n')

# Potential optimization: Pre-compute break-points in dictionary of names.
# I.e. For each letter depth, where does the next letter start? This would enable jumping to the relevant parts.
# E.g. Given 321, iterate through only where letter-depth 0, letter #3 words, then letter-depth 1, letter #2 words, etc.

fin.close()
fout.close()

# if(__name__ == '__main__'): # Local debug
#  import sys
#  import os
#  print('type {}.out'.format(sys.argv[0].lstrip('.\').split('.')[0])) #Debug
#  os.system('type {}.out'.format(sys.argv[0].lstrip('.\').split('.')[0]))

