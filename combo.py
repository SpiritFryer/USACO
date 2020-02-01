"""
ID: seishin1
LANG: PYTHON3
TASK: combo
"""
# For one combination, if the error tolerance is 2, then for each dial, it can accept up to 2*2 + 1 combinations.
# However, N could reduce this.
# Given a combination lock with D dials, N dial positions, E error tolerance:
# Each dial accepts min(N, 2*E + 1) positions.
# Each lock, accepts min(N, 2*E + 1)^D combinations.

# For our problem, D = 3, 1 <= N <= 100, E = 2.
# So: each dial accepts min(N, 5) positions.
# Each lock accepts min(N, 5)^3 combinations.

fin = open('combo.in', 'r')
fout = open('combo.out', 'w')

D = 3
E = 2

n = int(fin.readline().strip())
john_combo = tuple(map(int, fin.readline().split()))
master_combo = tuple(map(int, fin.readline().split()))

ACCEPTABLE_DIAL_POSITIONS = min(n, 2*E + 1)
ACCEPTABLE_LOCK_COMBINATIONS = ACCEPTABLE_DIAL_POSITIONS ** D

print('Master:', master_combo)
print('John:', john_combo)
print('Acceptable dial positions:', ACCEPTABLE_DIAL_POSITIONS)
print('Acceptable lock combinations:', ACCEPTABLE_LOCK_COMBINATIONS)

assert D == len(master_combo) == len(john_combo)  # The locks should have the expected number of dials

if n <= ACCEPTABLE_DIAL_POSITIONS:  # Edge-case: if all combinations overlap. Otherwise, below approach figures it out.
  ans = ACCEPTABLE_LOCK_COMBINATIONS
else:
  # Find number of overlapping combos between John's and Master's combo.
  # And subtract it from 2*ACCEPTABLE_LOCK_COMBINATIONS to yield the answer.
  overlapping = 1  # Initialized as 1 as we will multiply into it, and it will become 0 when necessary as part of that.
  for i in range(D):  # For each dial, track number of overlapping acceptable positions.
    # Check distance between dial combos to establish overlapping acceptable positions.
    # If one dial's combo distance is too large (i.e. no overlaps), then formula  will be < 0, so max to 0.
    print('Dial #', i, ':', master_combo[i], john_combo[i], 'Distances:', abs(master_combo[i] - john_combo[i]),
          (min(master_combo[i], john_combo[i]) - 1) + (n - max(master_combo[i], john_combo[i])) + 1)
    overlapping *= max(
      0,
      ACCEPTABLE_DIAL_POSITIONS - min(abs(master_combo[i] - john_combo[i]),  # Along number line
                                      # Around number line: bigger to n + smaller to 1 (minimum dial is 1, not 0):
                                      (min(master_combo[i], john_combo[i]) - 1)
                                      + (n - max(master_combo[i], john_combo[i]))
                                      + 1  # If min is 1, max is n, their distance around the number line should be 1.
                                      )
    )
  print('Overlapping:', overlapping)
  ans = 2*ACCEPTABLE_LOCK_COMBINATIONS - overlapping

print('Answer:', ans)
fout.write(str(ans) + '\n')

fin.close()
fout.close()

# if(__name__ == '__main__'): # Local debug
#  import sys
#  import os
#  print('type {}.out'.format(sys.argv[0].lstrip('.\').split('.')[0])) #Debug
#  os.system('type {}.out'.format(sys.argv[0].lstrip('.\').split('.')[0]))

