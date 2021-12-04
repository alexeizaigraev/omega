import os
import sys
import shutil

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)) 

from modules import *
from papa_pg import get_departments_list


class Gnetz():
    def __init__(self, kind):
        self.kind = kind

    def priznak_in_name(self, name):
        for priznak in self.priznaks:
            if priznak in name.lower():
                return True
        return False

    def get_files(self):
        send = []
        for ag_folder in self.ag_folders:
            path = os.path.join(GDRIVE_PATH, ag_folder)
            for top, dirs, files in os.walk(path):
                for nm in files:
                    name_full = os.path.join(top, nm)
                    sname = name_full.split(os.sep)
                    fname_short = sname[-1]
                    dep = sname[-2]
                    
                    if self.priznak_in_name(name_full):
                        new_name = '_'.join([dep, fname_short])
                        new_name_full = os.path.join(self.outpath, new_name)
                        try:
                            if self.choise == 'move':
                                shutil.move(name_full, new_name_full)
                            else:
                                shutil.copy(name_full, new_name_full)
                            if dep not in send:
                                send.append(dep)
                            #print(choise, new_name_full)
                        except Exception as ex:
                            print(ex)
        return send

    def mk_rezdict(self):
        sum = 0
        h = dict() 
        a = os.listdir(self.outpath)
        for fname in a:
            sum += 1
            dep = fname[:7]
            if dep in h:
                h[dep] += 1
            else:
                h[dep] = 1
        return h, sum
            
    
    def gnetz_main(self):
        
        choise = self.kind
        info = f'{choise}\n'

        self.priznaks = ('foto', 'photo', 'фото',)
        self.outpath = DATA_PATH + 'gnetz/'
        self.ag_folders = comon_data_list(3)

        self.get_files()

        rez_dict, sum = self.mk_rezdict()

        info = (f'\ndepatrtments: {len(rez_dict)}\n files: {sum}\n\nsend:\n\n')

        for key in rez_dict:
            info += f'{key} {rez_dict[key]}\n'

        info += '\n\nno send:\n'

        all_deps = get_departments_list()

        bed = [dep for dep in all_deps if dep not in rez_dict]
        bed_text = '\n'.join(bed)
        info += f'\nno send {len(bed)}:\n\n{bed_text}'

        save_and_show(info, 'info.txt')
        self.info = info