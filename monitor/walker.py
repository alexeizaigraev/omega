# -*- coding: utf-8 -*-
import os.path, sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)) 

from modules import *
import os
import shutil

class Walker():

    def dir_in_walk(self):
        return file_to_arr(CONFIG_PATH + 'ConfigRaskladPath.txt')[0]

    def dir_out_walk(self):
            return file_to_arr(CONFIG_PATH + 'ConfigGdrivePath.txt')[0]
        
    def show(self):
        a = os.listdir(self.dir_in_walk())
        for aa in a:
            self.info += aa + '\n'
        if not a:
            self.info += '\nnothing show\n'


    def mk_agents(self):
        return file_to_dict_one(COMON_DATA_PATH, 3)

    def mover(self):
        agents = self.mk_agents()
        a = os.listdir(self.dir_in_walk())
        if len(a) < 1:
                self.info += '\n\tno files found\n'
        old_dir = self.dir_in_walk()
        for aa in a:
            fname = os.path.abspath(aa).split(os.sep)[-1]
            old_fname = os.path.join(old_dir, fname)
            folder = fname[:7]
            key = fname[:3]
            new_root = os.path.join(self.dir_out_walk(), agents[key])
            new_dir = os.path.join(new_root, folder)
            new_fname = os.path.join(new_dir, fname)
            backup_fname = 'R:/DRM/ЗАИГРАЕВ ОБМЕН АРХИВ/Архив/' + fname
            if not os.path.exists(new_dir):
                try:
                    os.mkdir(new_dir)
                    self.info += '\tnew folder\n'
                except:
                    self.info += new_dir + '\n'
            try:
                shutil.copy(old_fname, backup_fname)
            except:
                pass
            
            try:
                shutil.move(old_fname, new_fname)
                self.info += new_fname + '\n'
            except:
                self.info += f'>> {new_fname}\n'
            
            
    def walker_main(self):
        self.info = ''        
        self.mover()

        self.info += '\n\n\nОстаток в rasklad:\n'
        self.show()


#u = Walker()
#u.walker_main()