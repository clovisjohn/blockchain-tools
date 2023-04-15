from functions import *
import sys

if len(sys.argv) < 3:
    raise ValueError('Please provide arguments')


l= [i.split(':') for i in sys.argv[1:]]

if l[0][0]=='size':
  size=int(l[0][1])
else:
  exit("you didn't provide a size")

pairs = [[x[0],x[1].lower()] for x in l[1:]]

common_inv = common_investors(pairs,size)

print(common_inv)
