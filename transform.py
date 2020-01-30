"""
ID: seishin1
LANG: PYTHON3
TASK: transform
"""

# Below methods take n sized matrix m. Returns m post-transform.
'''
  #1: 90 Degree Rotation: The pattern was rotated clockwise 90 degrees.
  #2: 180 Degree Rotation: The pattern was rotated clockwise 180 degrees.
  #3: 270 Degree Rotation: The pattern was rotated clockwise 270 degrees.
  #4: Reflection: The pattern was reflected horizontally (turned into a mirror image of itself by reflecting around a vertical line in the middle of the image).
  #5: Combination: The pattern was reflected horizontally and then subjected to one of the rotations (#1-#3).
  #6: No Change: The original pattern was not changed.
  #7: Invalid Transformation: The new pattern was not obtained by any of the above methods.
'''


def t1(n, m):  # 90 degree clockwise
  new = ['' for _ in range(n)]
  for j in range(n):
    for i in range(n - 1, -1, -1):
      new[j] += m[i][j]
  return new


def t2(n, m):  # 180 degree clockwise
  new = ['' for _ in range(n)]
  for i in range(n - 1, -1, -1):
    for j in range(n - 1, -1, -1):
      new[n - i - 1] += m[i][j]
  return new


def t3(n, m):  # 270 degree clockwise
  new = ['' for _ in range(n)]
  for j in range(n - 1, -1, -1):
    for i in range(n):
      new[n - j - 1] += m[i][j]
  return new


def t4(n, m, *, next_transform=None):  # Horizontal reflect
  new = ['' for _ in range(n)]
  for i in range(n):
    for j in range(n - 1, -1, -1):
      new[i] += m[i][j]

  if next_transform:
    return next_transform(n, new)
  else:
    return new


def find_transform(pre, post, funcs):
  for i in range(4):
    new = funcs[i](n, pre)
    if new == post:
      return i + 1

  for j in range(3):
    if funcs[j](n, new) == post:
      return 5

  if pre == post:
    return 6
  else:
    return 7


def str_kw(*args, **kwargs):
  output = ''
  for arg in args:
    output += str(arg) + ', '
  #print("#### str_kw kwargs: ", kwargs)
  for key, arg in kwargs.items():
    output += str(key) + ': ' + str(arg) + ', '
  return output

def find_transform2(pre, post, funcs2):
  for i in range(len(funcs2)):
    # print("Executing #{}, func: {}\nfuncs2[_][1]: {}\n**funcs2[_][1]: {}\n".format(
    #   str(i), str(funcs2[i]), str(funcs2[i][1]), "" if funcs2[i][1] is None else str_kw(**funcs2[i][1])))
    new = funcs2[i][0](n, pre) if funcs2[i][1] is None else funcs2[i][0](n, pre, **funcs2[i][1])
    if new == post:
      return i + 1 if i <= 3 else 5

  if pre == post:
    return 6
  else:
    return 7


fin = open('transform.in', 'r')
fout = open('transform.out', 'w')

# x,y = map(int, fin.readline().split())
n = int(fin.readline().strip())

pre = []
for _ in range(n):
  pre.append(fin.readline().strip())

post = []
for _ in range(n):
  post.append(fin.readline().strip())

print("Pre:", pre)

print("Pre + t1:", t1(n, pre), '\n' + '\n'.join(t1(n, pre)))
print("Pre + t2:", t2(n, pre), '\n' + '\n'.join(t2(n, pre)))
print("Pre + t3:", t3(n, pre), '\n' + '\n'.join(t3(n, pre)))
print("Pre + t4:", t4(n, pre), '\n' + '\n'.join(t4(n, pre)))
print("Pre + t4 + t1:", t1(n, t4(n, pre)), '\n' + '\n'.join(t1(n, t4(n, pre))))
print("Pre + t4 + t2:", t2(n, t4(n, pre)), '\n' + '\n'.join(t2(n, t4(n, pre))))
print("Pre + t4 + t3:", t3(n, t4(n, pre)), '\n' + '\n'.join(t3(n, t4(n, pre))))

print("Post:", post)

funcs = [t1, t2, t3, t4]
funcs2 = [(t1, None), (t2, None), (t3, None), (t4, None),
          (t4, {'next_transform': t1}),
          (t4, {'next_transform': t2}),
          (t4, {'next_transform': t3})]
ans = find_transform(pre, post, funcs)
print("funcs2:", '\n'.join(map(str, enumerate(funcs2))))
ans2 = find_transform2(pre, post, funcs2)

print("Ans:", ans)
print("Ans2:", ans2)
fout.write(str(ans2) + '\n')

fin.close()
fout.close()

# if(__name__ == '__main__'): # Local debug
#  import sys
#  import os
#  print('type {}.out'.format(sys.argv[0].lstrip('.\').split('.')[0])) #Debug
#  os.system('type {}.out'.format(sys.argv[0].lstrip('.\').split('.')[0]))
