from functions import *

import sys

if len(sys.argv) < 3:
    raise ValueError('Please provide arguments')

l= [i.split(':') for i in sys.argv[1:])

print(l)
