"""
ID: seishin1
LANG: PYTHON3
TASK: preface
"""
#         I   1
#         V   5
#         X  10
#         L  50
#         C  100
#         D  500
#         M  1000

# As many as three of the same marks that represent 10n may be placed consecutively to form other numbers:
#
# III is 3
# CCC is 300
# Any mark that has the value 5x10n can not be used consecutively.
#
# Sometimes, a mark that represents 10^n is placed before a mark of one of the two next higher values
# (I before V or X; X before L or C; etc.).
#
# IV = 4
# IX = 9
# XL = 40
# XC = 90
# CD = 400
# CM = 900
#
# Biggest representable with above rules:
# MMMCMXCIX = 3000 + 900 + 90 + 9 = 3999
#
# Longest string representable with above rules:
# MMMDCCCLXXXVIII = 3000 + 500 + 300 + 50 + 30 + 5 + 3 = 3888
#
# Look at thousands digit:
# 0: '', 1: 'M', 2: 'MM', 3: 'MMM'
#
# Look at hundreds digit:
# 0: '', 1: 'C', 2: 'CC', 3: 'CCC', 4: 'CD', 5: 'D', 6: 'DC', 7: 'DCC', 8: 'DCCC', 9: 'CM'
#
# Look at tens digit:
# 0: '', 1: 'X', 2: 'XX', 3: 'XXX', 4: 'XL', 5: 'L', 6: 'LX', 7: 'LXX', 8: 'LXXX', 9: 'XC'
#
# Look at ones digit:
# 0: '', 1: 'I', 2: 'II', 3: 'III', 4: 'IV', 5: 'V', 6: 'VI', 7: 'VII', 8: 'VIII', 9: 'IX'

roman_numbers = [
  ['', 'M', 'MM', 'MMM'],  # Thousands
  ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM'],  # Hundreds
  ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC'],  # Tens
  ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX'],  # Ones
]

NUM_CHARS = 7
CHARS = ('I', 'V', 'X', 'L', 'C', 'D', 'M')

# used_characters for each "digit":
# used_chars = [[], [], [], []]
# for magnitude in range(4):  # Thousands, hundreds, tens, ones
#   for x in range(len(roman_numbers[magnitude])):
#     # Decimal: x * 10^magnitude
#     roman_digit = roman_numbers[magnitude][x]
#     chars_of_digit = [0] * NUM_CHARS  # I V X L C D M
#     for char_index in range(NUM_CHARS):
#       chars_of_digit[char_index] = roman_digit.count(CHARS[char_index])
#     used_chars[magnitude].append(chars_of_digit)
#
# print(repr(used_chars))

# Hardcoded using above
used_chars = [[[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 2], [0, 0, 0, 0, 0, 0, 3]], [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 2, 0, 0], [0, 0, 0, 0, 3, 0, 0], [0, 0, 0, 0, 1, 1, 0], [0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 1, 1, 0], [0, 0, 0, 0, 2, 1, 0], [0, 0, 0, 0, 3, 1, 0], [0, 0, 0, 0, 1, 0, 1]], [[0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0, 0], [0, 0, 2, 0, 0, 0, 0], [0, 0, 3, 0, 0, 0, 0], [0, 0, 1, 1, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0], [0, 0, 1, 1, 0, 0, 0], [0, 0, 2, 1, 0, 0, 0], [0, 0, 3, 1, 0, 0, 0], [0, 0, 1, 0, 1, 0, 0]], [[0, 0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0], [2, 0, 0, 0, 0, 0, 0], [3, 0, 0, 0, 0, 0, 0], [1, 1, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0], [1, 1, 0, 0, 0, 0, 0], [2, 1, 0, 0, 0, 0, 0], [3, 1, 0, 0, 0, 0, 0], [1, 0, 1, 0, 0, 0, 0]]]
# print('\n'.join(str(line) for line in used_chars))


def iterate_up_to(n):
  global roman_numbers
  global used_chars

  all_chars = [0] * NUM_CHARS
  x = 0
  for thousands in range(len(roman_numbers[0])):
    for hundreds in range(len(roman_numbers[1])):
      for tens in range(len(roman_numbers[2])):
        for ones in range(len(roman_numbers[3])):
          # current_chars = [0] * NUM_CHARS
          for char_index in range(NUM_CHARS):
            all_chars[char_index] += used_chars[0][thousands][char_index]
            all_chars[char_index] += used_chars[1][hundreds][char_index]
            all_chars[char_index] += used_chars[2][tens][char_index]
            all_chars[char_index] += used_chars[3][ones][char_index]
          # print(x,
          #       roman_numbers[0][thousands]
          #       + roman_numbers[1][hundreds]
          #       + roman_numbers[2][tens]
          #       + roman_numbers[3][ones],
          #       all_chars)
          x += 1
          if x > n:  # Do the loop on x == n
            return all_chars


fin = open('preface.in', 'r')
fout = open('preface.out', 'w')

n = int(fin.readline().strip())
ans = iterate_up_to(n)
print(ans)

largest_used_letter_index = NUM_CHARS - 1
while ans[largest_used_letter_index] == 0:
  largest_used_letter_index -= 1
print('\n'.join(
  (CHARS[char_index] + ' ' + str(ans[char_index]))
  for char_index in range(largest_used_letter_index + 1)))

fout.write(
  '\n'.join(
    (CHARS[char_index] + ' ' + str(ans[char_index]))
    for char_index in range(largest_used_letter_index + 1)
  )
  + '\n')

fin.close()
fout.close()

# if(__name__ == '__main__'): # Local debug
#  import sys
#  import os
#  print('type {}.out'.format(sys.argv[0].lstrip('.\').split('.')[0])) #Debug
#  os.system('type {}.out'.format(sys.argv[0].lstrip('.\').split('.')[0]))

