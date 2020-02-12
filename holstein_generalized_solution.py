"""
ID: seishin1
LANG: PYTHON3
TASK: holstein
"""
MAX_SCOOPS = 1000


def good_solution(overall_candidate_feeds, min_v_reqs, feeds):
  candidate_vitamin_amounts = [0] * len(min_v_reqs)

  for vitamin_index in range(len(min_v_reqs)):
    for feed_index in range(len(overall_candidate_feeds)):
      candidate_vitamin_amounts[vitamin_index] += overall_candidate_feeds[feed_index] * feeds[feed_index][vitamin_index]
  # print('Trying ', overall_candidate_feeds, ':', candidate_vitamin_amounts)

  for i in range(len(candidate_vitamin_amounts)):
    if candidate_vitamin_amounts[i] < min_v_reqs[i]:
      # print('    false :c')
      return False
  # print('    TRUUUUUUUUUUUUUUUUUUUUUUUUUU')
  return True


def try_feeds(max_scoops, overall_candidate_feeds, num_feeds, min_v_reqs, feeds):
  # print('        try_feeds:', max_scoops, overall_candidate_feeds, num_feeds)
  if max_scoops == 0:
    overall_candidate_feeds += [0]*num_feeds
    num_feeds = 0

  if num_feeds == 0:
    # print('        Base case:', overall_candidate_feeds)
    if good_solution(overall_candidate_feeds, min_v_reqs, feeds):
      # print('YIELDING!')
      yield overall_candidate_feeds
    return

  for earliest_feed_index in range(num_feeds):
    # print('    Trying earliest_feed_index:', earliest_feed_index)
    added_candidate_feeds = []
    for irrelevant_feeds in range(earliest_feed_index):
      added_candidate_feeds.append(0)

    for scoop_amount in range(max_scoops, 0, -1):  # Down to 1 inclusive
      # print('      Trying scoop_amount:', scoop_amount, '-- executing try_feeds')
      yield from try_feeds(max_scoops - scoop_amount,
                           overall_candidate_feeds + added_candidate_feeds + [scoop_amount],
                           num_feeds - earliest_feed_index - 1,
                           min_v_reqs,
                           feeds)

      if earliest_feed_index == num_feeds - 1:
        # Already tried 'max_scoops'. Can't break it down further cos no feeds left.
        break
      # print('      ### Execution complete!')


#DEBUG_LIMIT = 4
def bfs_permutations(min_v_reqs, feeds):
  if min_v_reqs.count(0) == len(min_v_reqs):
    return [0] * len(feeds)

  # Max scoops loops
  # print('bfs_permutations')
  max_scoops = 1
  num_feeds = len(feeds)
  while True:
    # print('  Trying max_scoops:', max_scoops, '-- executing try_feeds')
    yield from try_feeds(max_scoops, [], num_feeds, min_v_reqs, feeds)
    # print('  # Execution complete!')

    max_scoops += 1
    # if max_scoops == DEBUG_LIMIT:
    #   return None
    if max_scoops > MAX_SCOOPS:
      return None  # No answer


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

gen = bfs_permutations(min_v_reqs, feeds)
good_feed_allocation = next(gen)
print(good_feed_allocation)

num_scoops = sum(good_feed_allocation)
#relevant_feeds = ' '.join(str(feed_index + 1) for feed_index in filter(lambda x: x > 0, good_feed_allocation))
relevant_feed_indeces = []
for i in range(len(good_feed_allocation)):
  if good_feed_allocation[i] > 0:
    relevant_feed_indeces.append(i)

relevant_feeds = ' '.join(str(index + 1) for index in relevant_feed_indeces)

ans = str(num_scoops) + ' ' + relevant_feeds
print(ans)
fout.write(str(ans) + '\n')

fin.close()
fout.close()

# if(__name__ == '__main__'): # Local debug
#  import sys
#  import os
#  print('type {}.out'.format(sys.argv[0].lstrip('.\').split('.')[0])) #Debug
#  os.system('type {}.out'.format(sys.argv[0].lstrip('.\').split('.')[0]))

