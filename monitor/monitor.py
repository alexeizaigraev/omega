# -*- coding: utf-8 -*-
import os.path, sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)) 

import os
import shutil
from pathlib import Path
from modules import *

class Monitor():

    def monitor_main(self):
        info = ''
        in_dirs = file_to_arr(os.path.join(CONFIG_DIR_PATH, 'PathMonitor.txt'))
        out_path = file_to_arr(os.path.join(CONFIG_DIR_PATH, 'PathMonitorOut.txt'))[0]

        flag = False
        start_dirs = in_dirs
        for dir in start_dirs:
            fnames = os.listdir(dir)
            for fname in fnames:
                if '.pdf' in fname:
                    flag = True
                    old_name = dir + fname
                    new_name = out_path + fname
                    info += mover(old_name, new_name)
        if not flag:
            info += '\n\tempty\n'
        self.info = info