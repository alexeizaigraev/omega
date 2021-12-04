import os.path, sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)) 

from papa_pg import *

verb = True
#verb = False

insert_all_terms()
insert_all_deps()
insert_all_otbor()


