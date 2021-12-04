# -*- coding: utf-8 -*-
import os.path, sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)) 

from modules import *
import os
import shutil
#from papa_pg import get_otbor_deps


class GetRpAll():
    def __init__(self, folder_choise):
        self.folder = folder_choise

    
    def get_all_fnames(self):
        out = []
        folders = os.listdir(GDRIVE_PATH + self.folder)
        for folder in folders:
            try:
                work_dir = GDRIVE_PATH + self.folder + '/' + folder
                fnames = os.listdir(work_dir)
                for fname in fnames:
                    if 'RP' not in fname:
                        continue
                    
                    fname_full = work_dir + '/' + fname
                    out.append(fname_full)
            except:
                pass
            
        return out


    def short_name(self, name):
        return name.split('/')[-1]


    def get_rp_all_main(self):
        info = ''
        sum = 0
        out_path = KABINET_DIR
        old = os.listdir(out_path)
        for fname in old:
            try:
                if '.pdf' in fname:
                    os.remove(out_path + fname)
            except:
                print('err remove', fname)


        info += f'\n{self.folder}\n'

        a = self.get_all_fnames()
        for aa in a:
            old_name = aa
            new_name = out_path + self.short_name(aa)
            sum += 1
            info += coper(old_name, new_name)


        info += f'\n\t{sum=}\n'
        self.info = info
