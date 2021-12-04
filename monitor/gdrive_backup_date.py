import os
import sys
import shutil

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)) 

from modules import *
from papa_pg import get_departments_list


class GdriveBackDate():
    
    def mk_ag_folders(self):
        outlist = []
        for folder in comon_data_dict(3).values():
            if folder != 'nodata':
                outlist.append(folder)
        return outlist

    def good_path(self, path):
        for good_fold in self.ag_folders:
            if  good_fold in path:
                return True
        return False

    def copytree(self, src, dst, symlinks=False, ignore=None):
        for item in os.listdir(src):
            s = os.path.join(src, item)
            if not self.good_path(s):
                continue
            d = os.path.join(dst, item)
            try:
                if os.path.isdir(s):
                    shutil.copytree(s, d, symlinks, ignore, dirs_exist_ok=True)
                    self.info += d + '\n'
                else:
                    shutil.copy2(s, d)
                    self.info += d + '\n'
            except Exception as ex:
                pass


    def gdrive_back_date_main(self):
        self.info = ''
        self.ag_folders = self.mk_ag_folders()
        inpath = GDRIVE_PATH
        outpath = GDRIVE_BACKUP_PATH + now_date_log()
        self.copytree(inpath, outpath, symlinks=False, ignore=None)
        self.info += '\n\twell'