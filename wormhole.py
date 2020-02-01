"""
ID: seishin1
LANG: PYTHON3
TASK: wormhole
"""

# Affordance: Bessie only moves in the +x direction.
# [A.] Find the total number of possible pairings.
# [B.] Find the number of pairings that cannot yield an infinite loop.
#      Iterate through all pairings (a counter here could be used to calculate [A.],
#      Increment counter if it is not an illegal pairing.
#      Illegal pairings: pairs of wormholes that are on the same horizontal, i.e.: w1.y == w2.y.
# [A.] - [B.] is the answer.


def dfs_pairs(stack, pairs):  # n = len(stack). Number of recursive calls: O()
  #global num_calls
  if not stack:
    yield pairs
  else:
    pair_left = stack.pop(0)
    for i in range(len(stack)):  # Loop iterations: O(n - 1). Each iteration recurses with n - 2
      new_stack = list(stack)
      pair_right = new_stack.pop(i)

      new_pairs = list(pairs)
      new_pairs.append((pair_left, pair_right))

      #num_calls += 1
      #if(num_calls % 10000000 == 0):
      #  print("Another 10M:", num_calls)
      yield from dfs_pairs(new_stack, new_pairs)


fin = open('wormhole.in', 'r')
fout = open('wormhole.out', 'w')

n = int(fin.readline().strip())
# s1 = fin.readline().strip()

w = []  # Wormholes
for line in fin:
  w.append(tuple(map(int, line.split())))
print('Wormholes:', w)
w = sorted(w)
print('Wormholes:', w)
to_my_right = dict((key, None) for key in w)
for i in range(len(w)):
  for j in range(i + 1, len(w)):
    if w[i][1] == w[j][1]:
      # Assume no two wormholes are at the same coordinates.
      to_my_right[w[i]] = w[j]
      break
print("to_my_right:")
for lr in to_my_right:
  print(lr, to_my_right[lr])
print()
# # OLD
# # Generate dictionary as outlined in [B.]
# loop_pairs = dict((wormhole, set()) for wormhole in w)
# # print(loop_pairs)
# for i in range(len(w)):
#   for j in range(i + 1, len(w)):
#     if w[i][1] == w[j][1]:
#       loop_pairs[w[i]].add(w[j])
#       loop_pairs[w[j]].add(w[i])
# print('Loop pairs:\n', '\n'.join(str(x) + ': ' + str(loop_pairs[x]) for x in loop_pairs), sep='')

# Iterate through all pairings.
count_all_pairings = 0  # Counter for all possible pairings.
count_no_loop_pairings = 0  # Counter for pairings that cause no loops.
for pairing in dfs_pairs(list(w), []):
  count_all_pairings += 1

  # Check if it's a good pairing
  good = True
  traversed_jump = dict((wormhole, False) for wormhole in w)
  traversed_right_move = dict((wormhole, False) for wormhole in w)
  paired_with = dict()
  for p in pairing:
    paired_with[p[0]] = p[1]
    paired_with[p[1]] = p[0]
  for p in pairing:
      # If a wormhole has something to its right, traverse the pairing and see if it loops.
    for wormhole in p:
      #print('  Traversed check:', p, wormhole, traversed_jump, traversed_right_move)
      if (not traversed_jump[wormhole]) or (not traversed_right_move[wormhole]):
        print('    Moving right {} -> {}'.format(wormhole, to_my_right[wormhole]))
        next_wormhole = to_my_right[wormhole]
        traversed_right_move[wormhole] = True
        loop_check_right_move = {wormhole}
        loop_check_jump = set()
        while next_wormhole is not None:
          if next_wormhole in loop_check_jump or paired_with[next_wormhole] in loop_check_right_move:
            print('  Bad:', '(jump)' if next_wormhole in loop_check_jump else '(right move)',
                  next_wormhole, paired_with[next_wormhole], loop_check_jump, loop_check_right_move)
            good = False
            break
          
          traversed_jump[next_wormhole] = True
          loop_check_jump.add(next_wormhole)
          
          traversed_right_move[paired_with[next_wormhole]] = True
          loop_check_right_move.add(paired_with[next_wormhole])

          print('    Jumping {} -> {}'.format(next_wormhole, paired_with[next_wormhole]))
          print('    Moving right {} -> {}'.format(paired_with[next_wormhole], to_my_right[paired_with[next_wormhole]]))
          next_wormhole = to_my_right[paired_with[next_wormhole]]
        if not good:
          break
    if not good:
      break
  if good:
    count_no_loop_pairings += 1
    print('No loop pairing:', pairing, '\n')
  else:
    print('Loop pairing:', pairing, '\n')

print('All pairings:', count_all_pairings)
print('No loop pairings:', count_no_loop_pairings)
print('Loop pairings:', count_all_pairings - count_no_loop_pairings)
fout.write(str(count_all_pairings - count_no_loop_pairings) + '\n')

fin.close()
fout.close()

# if(__name__ == '__main__'): # Local debug
#  import sys
#  import os
#  print('type {}.out'.format(sys.argv[0].lstrip('.\').split('.')[0])) #Debug
#  os.system('type {}.out'.format(sys.argv[0].lstrip('.\').split('.')[0]))

