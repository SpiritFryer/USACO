"""
ID: seishin1
LANG: PYTHON3
TASK: beads
"""
fin = open('beads.in', 'r')
fout = open('beads.out', 'w')

n = int(fin.readline().strip())
beads = fin.readline().strip()
# print(str(beads + beads))

# Could test for edge cases, e.g. only r, b, rw, bw -> then ans = n.
if beads.count('r') == 0 or beads.count('b') == 0:
  max_sequence = n
else:
  max_sequence = 0

  red_status = 0
  blue_status = 0

  red_sequence = 0
  blue_sequence = 0
  white_sequence = 0

  for c in str(beads + beads):
    if c == 'w':
      red_sequence += 1
      blue_sequence += 1
      white_sequence += 1

    if c == 'r':
      if red_status == 0:  # Continue red sequence.
        red_sequence += 1
      elif red_status == 1:  # red-blue sequence finished.
        red_status = 0
        if red_sequence > max_sequence:
          max_sequence = red_sequence
        red_sequence = white_sequence + 1

      if blue_status == 0:  # blue-red sequences starts red part.
        blue_status = 1
        blue_sequence += 1
      elif blue_status == 1:  # Continue red part of sequence.
        blue_sequence += 1

      white_sequence = 0

    if c == 'b':
      if blue_status == 0:  # Continue blue sequence.
        blue_sequence += 1
      elif blue_status == 1:  # blue-red sequence finished.
        blue_status = 0
        if blue_sequence > max_sequence:
          max_sequence = blue_sequence
        blue_sequence = white_sequence + 1

      if red_status == 0:  # red-blue sequences starts blue part.
        red_status = 1
        red_sequence += 1
      elif red_status == 1:  # Continue blue part of sequence.
        red_sequence += 1

      white_sequence = 0

if max_sequence > n:
  max_sequence = n

fout.write(str(max_sequence) + '\n')

fin.close()
fout.close()

# if(__name__ == '__main__'): # Local debug
#  import sys
#  import os
#  print('type {}.out'.format(sys.argv[0].lstrip('.\\').split('.')[0])) #Debug
#  os.system('type {}.out'.format(sys.argv[0].lstrip('.\\').split('.')[0]))

