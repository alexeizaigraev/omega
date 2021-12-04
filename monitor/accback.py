# -*- coding: utf-8 -*-
import os.path, sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)) 

import os
import shutil
from pathlib import Path
from modules import *
from datetime import datetime
import shutil
#from papa_pg import insert_all_depsarhiv, insert_all_termsarhiv


#insert_all_depsarhiv()
#insert_all_termsarhiv()

now = str(datetime.strftime(datetime.now(), "%Y-%m-%d_%H_%M_%S"))
#in_path = 'R:/DRM/Access/db2_be.accdb'
out_path = 'R:/DRM/BackupAccess/db2_be_' + now + '.accdb'
in_path = IN_DATA_PATH + 'drm.db'
#out_path = 'R:/DRM/BackupAccess/drm_' + now + '.db'
try:
    shutil.copy(in_path, out_path)
    print(f'\n{out_path}')
except:
    print('\n\tno accback')

