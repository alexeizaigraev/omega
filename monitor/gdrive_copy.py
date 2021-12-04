import os.path, sys, shutil


#from monitor.get_rp_all import ag_folders
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)) 
from modules import *


def mk_ag_folders():
    outlist = []
    for folder in comon_data_dict(3).values():
        if folder != 'nodata':
            outlist.append(folder)
    return outlist

def good_path(path):
    for good_fold in ag_folders:
        if  good_fold in path:
            return True
    return False

def copytree(src, dst, symlinks=False, ignore=None):
    for item in os.listdir(src):
        s = os.path.join(src, item)
        if not good_path(s):
            continue
        d = os.path.join(dst, item)
        try:
            if os.path.isdir(s):
                shutil.copytree(s, d, symlinks, ignore, dirs_exist_ok=True)
                #p_green(d)
            else:
                shutil.copy2(s, d)
                #p_blue(d)
        except Exception as ex:
            print(ex)


ag_folders = mk_ag_folders()
inpath = GDRIVE_PATH
outpath = GDRIVE_BACKUP_PATH + now_date_log()
copytree(inpath, outpath, symlinks=False, ignore=None)
p_yellow('\n\twell')