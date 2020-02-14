"""
ID: seishin1
LANG: PYTHON3
TASK: hamming
"""
# Given B bits, and minimum Hamming distance D:
# D = B: For 0b0^B there is only 1 codeword that is D distance away, 0b1^B
# D = B-1: There are B choose 1 codewords
# D = B-2: There are B choose 2 codewords
# So,
# There are B choose (B - D) codewords.
# If N > B choose (B - D), then definitely no possible set.
#
# 0   00000000
# 7   00000111
# 25  00011001
# 30  00011110
# 42  00101010
# 45  00101101
# 51  00110011
# 52  00110100
# 75  01001011
# 76  01001100
# 82  01010010
# 85  01010101
# 97  01100001
# 102 01100110
# 120 01111000
# 127 01111111


def increment_binary(binary):
  global ones
  global all_ones
  i = 0
  if binary[0] == 1:
    i = 0
    while True:
      binary[i] = 0
      ones -= 1
      i += 1
      if binary[i] == 0:
        binary[i] = 1
        ones += 1
        break
  else:
    binary[0] = 1
    ones += 1

  all_ones.append(ones)


# def hamming_distance(p, q):
#   global all_ones
#   xor = p ^ q
#   print('Xor: {} ^ {} = {} | {} ~ {}'.format(bin(p), bin(q), bin(xor), xor, all_ones[xor]))


fin = open('hamming.in', 'r')
fout = open('hamming.out', 'w')

n,b,d = map(int, fin.readline().split())
print(n, b, d)

limit = 2**b

binary = [0] * (b + 1)  # +1 to avoid overflow and reduce operations in increment_binary
ones = 0
all_ones = [0]
for x in range(1, limit):  # Up to 2**b - 1 inclusive
  increment_binary(binary)
  # print(x, binary, all_ones[x])

# print(bin(0), bin(1), bin(2), bin(3), bin(4), bin(5))
# hamming_distance(1, 2)
# hamming_distance(1, 3)
# hamming_distance(2, 3)
# hamming_distance(2, 4)
# hamming_distance(0, 127)

nums = []

for first_candidate in range(1, limit):
  if all_ones[first_candidate] >= d:
    nums.append(first_candidate)
    break

for candidate in range(first_candidate + 1, limit):  # Up to 2**b - 1 inclusive
  if all_ones[candidate] >= d:  # At least d Hamming distance from 0
    # print('Trying:', candidate)
    good = True
    for tester in nums:
      # print('  Testing against:', tester, '|', candidate ^ tester, all_ones[candidate ^ tester])
      if all_ones[candidate ^ tester] < d:  # Hamming distance
        good = False
        break
    if good:
      nums.append(candidate)
      if len(nums) == n - 1:  # -1 because 0 is technically in nums, just not added yet
        break
      # print('    >= d for all!', nums)

nums = [0] + nums  # Also 0 is implicitly contained
print(nums)

# print(int((9 - 1) / 10) + 1)
# print(int((10 - 1) / 10) + 1)
# print(int((11 - 1) / 10) + 1)
# print(int((19 - 1) / 10) + 1)
# print(int((20 - 1) / 10) + 1)
# print(int((21 - 1) / 10) + 1)
# print(int((100 - 1) / 10) + 1)

#print([nums[group*10 : (group+1)*10] for group in range(int((len(nums) - 1) / 10) + 1)])
print(''.join([str(nums[i]) + ('\n' if ((i > 8) and ((i + 1) % 10 == 0)) else ' ') for i in range(len(nums))]).strip())
fout.write(''.join([str(nums[i]) + ('\n' if ((i > 8) and ((i + 1) % 10 == 0)) else ' ') for i in range(len(nums))]).strip() + '\n')


fin.close()
fout.close()

# if(__name__ == '__main__'): # Local debug
#  import sys
#  import os
#  print('type {}.out'.format(sys.argv[0].lstrip('.\').split('.')[0])) #Debug
#  os.system('type {}.out'.format(sys.argv[0].lstrip('.\').split('.')[0]))

