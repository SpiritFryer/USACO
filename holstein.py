"""
ID: seishin1
LANG: PYTHON3
TASK: holstein
"""
from itertools import combinations

fin = open('holstein.in', 'r')
fout = open('holstein.out', 'w')

vitamin_types_count = int(fin.readline().strip())
min_v_reqs = list(map(int, fin.readline().split()))
print(vitamin_types_count)
print(min_v_reqs)

feed_types_count = int(fin.readline().strip())
feeds = [list(map(int, line.split())) for line in fin]

print(feed_types_count)
print(feeds)

ans = None
feed_indices = list(range(len(feeds)))
print(feed_indices)

for scoops in range(feed_types_count + 1):
  for try_feeds in combinations(feed_indices, scoops):
    # print('Trying:', try_feeds)
    for vitamin_index in range(vitamin_types_count):
      curr_vitamin_intake = 0

      good = True
      for feed_index in try_feeds:
        curr_vitamin_intake += feeds[feed_index][vitamin_index]
      if curr_vitamin_intake < min_v_reqs[vitamin_index]:
        good = False
        break

    if good:
      ans = try_feeds
      break

  if ans:
    break

ans_feeds = str(len(ans))
ans_indices = ' '.join(str(x + 1) for x in ans)
print(ans_feeds + ' ' + ans_indices)
fout.write(ans_feeds + ' ' + ans_indices + '\n')

fin.close()
fout.close()

# if(__name__ == '__main__'): # Local debug
#  import sys
#  import os
#  print('type {}.out'.format(sys.argv[0].lstrip('.\').split('.')[0])) #Debug
#  os.system('type {}.out'.format(sys.argv[0].lstrip('.\').split('.')[0]))

