import os
import sys
import shutil

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)) 

from modules import *

#from modules import DATA_PATH, GDRIVE_PATH, comon_data_list

def priznak_in_name(name):
    for priznak in priznaks:
        if priznak in name.lower():
            return True
    return False

def get_all_deps(path):
    rez = []
    for top, dirs, files in os.walk(path):
        for dir in dirs:
            try:
                rez.append(dir)
            except:
                pass
    return rez


def get_files(path):
    for top, dirs, files in os.walk(path):
        for nm in files:
            name_full = os.path.join(top, nm)
            if priznak_in_name(name_full):
                sname = name_full.split(os.sep)
                fname_short = sname[-1]
                dep = sname[-2]
                #new_name = os.path.join(outputpath, fname_short)
                new_name = '_'.join([dep, fname_short])
                new_name_full = os.path.join(outputpath, new_name)
                try:
                    if choise == 'move':
                        shutil.move(name_full, new_name_full)
                    else:
                        shutil.copy(name_full, new_name_full)
                    print(choise, new_name_full)
                except Exception as ex:
                    print(ex)
        
quest = ['copy', 'move']
choise = ask(quest)
print(f'{choise=}')

gdrive_path = GDRIVE_PATH
outputpath = DATA_PATH + 'gnetz/'
priznaks = ('foto', 'photo', 'фото',)
ag_folders = comon_data_list(3)
all_deps = []
for ag_folder in ag_folders:
    try:
        path = os.path.join(gdrive_path, ag_folder)
        get_files(path)
        deps = get_all_deps(path)
        if deps:
            for dep in deps:
                all_deps.append(dep)
    except Exception as ex:
        print(ex)

out_files = os.listdir(outputpath)
good_deps = []
for fname in out_files:
    if fname[:7] not in good_deps:
        good_deps.append(fname[:7])

#print(out_files)
#print(all_deps)

#print('\nEmpty:\n')
info = f'\nget {len(out_files)} files\nfrom deps:\n'

sended_text = '\n'.join(good_deps)
info += f'\n{sended_text}\n'


info += '\n\nempty folders: \n\n'


for dep in all_deps:
    flag = False
    for fname in out_files:
        if dep in fname:
            flag = True
            break
    if not flag:
        info += dep + '\n'
        #print(dep)

save_and_show(info, 'info.txt')
print(f'\n get: {len(out_files)} files')
