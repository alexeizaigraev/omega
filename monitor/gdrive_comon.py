import os.path, sys, shutil


#from monitor.get_rp_all import ag_folders
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)) 
from modules import *


def count_files(path):
    count = 0
    for top, dirs, files in os.walk(path):
        for nm in files:
            count += len(files)
            #print(len(files), files)
            #print os.path.join(top, nm)
    return count

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
                #p_cyan(d)
        except Exception as ex:
            print(ex)

def recurcive_deletion(folder_name):
    try:
       shutil.rmtree(folder_name)
       p_cyan(f'delete * in {folder_name}')
    except:
        p_red('no folder')

ag_folders = mk_ag_folders()
inpath = GDRIVE_PATH
outpath = GDRIVE_BACKUP_PATH + '0_comon/'

p_yellow(f'\nGdrive: {count_files(inpath)} files')
choise = ask_no_cls(['backup', 'no'])
if choise == 'backup':
    recurcive_deletion(outpath)
    copytree(inpath, outpath)

choise = ask_no_cls(['summury', 'no'])
if choise == 'summury':
    p_yellow(f'\n{count_files(outpath)} files')

