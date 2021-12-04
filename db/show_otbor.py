import os.path, sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)) 

from modules import *
from papa_pg import *


print()
otbor = select_table('otbor')
for line in otbor:
    print(f' {line[0]}  {line[1]}')
