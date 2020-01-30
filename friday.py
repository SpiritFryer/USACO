"""
ID: seishin1
LANG: PYTHON3
TASK: friday
"""
from functools import reduce

fin = open('friday.in', 'r')
fout = open('friday.out', 'w')

STARTING_YEAR = 1900
X = 13 # We want weekday frequency for Xth of each month.
M = [ # [Non-Leap, Leap]
  [31,31], # Jan
  [28,29], # Feb
  [31,31], # Mar
  [30,30], # Apr .
  [31,31], # May
  [30,30], # Jun .
  [31,31], # Jul
  [31,31], # Aug
  [30,30], # Sep .
  [31,31], # Oct
  [30,30], # Nov .
  [31,31], # Dec
]

month = 0 # Current month. 0 to 11.
weekday = 2 # Current weekday. 0 to 6. 2 = Monday.
f = [0 for _ in range(7)] # Frequency of each weekday falling on Xth of month. 0 = Saturday.

# Move date to X Jan STARTING_YEAR, e.g. from 1 Jan 1900 to 13 Jan 1900
weekday = (weekday + X - 1) % 7 # Number of days passed
#print(str(X - 1)) #Debug
#print(weekday) #Debug

n = int(fin.readline().strip())
#n = 200 #Debug
for year in range(STARTING_YEAR, STARTING_YEAR + n):
  # year: Current year. 1900 to 1900+N-1. 0 < N <= 400.
  leap = 1 if ((year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)) else 0
  #if(leap == 1): #Debug
  #  print(year, leap) #Debug
  
  for days_passed in M:
    f[weekday] += 1 # Log frequency first.
    
    # Move date to next month's Xth.
    days_passed = days_passed[leap]
    weekday = (weekday + days_passed) % 7
  
#print(f) #Debug
#print(list(map(str,f))) #Debug
#print(reduce(lambda x, y: str(x) + ' ' + str(y), f)) #Debug
#print(' '.join(str(freq) for freq in f))
fout.write(' '.join(str(freq) for freq in f) + '\n')

fin.close()
fout.close()

if(__name__ == '__main__'): # Local debug
  import sys
  import os
  #print('type {}.out'.format(sys.argv[0].lstrip('.\\').split('.')[0])) #Debug
  os.system('type {}.out'.format(sys.argv[0].lstrip('.\\').split('.')[0]))

