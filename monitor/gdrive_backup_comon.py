import os
import sys
import shutil

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)) 

from modules import *
from papa_pg import get_departments_list


class GdriveBackComon():
    
    def count_files(self, path):
        count = 0
        for top, dirs, files in os.walk(path):
            for nm in files:
                count += len(files)
                #print(len(files), files)
                #print os.path.join(top, nm)
        return count

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
                    #p_green(d)
                else:
                    shutil.copy2(s, d)
                    #p_cyan(d)
            except Exception as ex:
                pass

    def recurcive_deletion(self, folder_name):
        try:
            shutil.rmtree(folder_name)
            #p_cyan(f'delete * in {folder_name}')
        except:
            pass
            #p_red('no folder')

    def gdriveback_comon_main(self):
        info = ''
        self.ag_folders = self.mk_ag_folders()
        inpath = GDRIVE_PATH
        outpath = GDRIVE_BACKUP_PATH + '0_comon/'

        info += f'\nGdrive: {self.count_files(inpath)} files\n\n'
        
        self.recurcive_deletion(outpath)
        self.copytree(inpath, outpath)

        info += f'\n{self.count_files(outpath)} files\n'
        self.info = info

