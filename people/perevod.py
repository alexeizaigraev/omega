import os.path, sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)) 

from modules import *
from papa_class import *

class Perevod(Papa):

    def perevod_main(self):
        info = ''
        self.ColFioOne = 0
        self.ColDepOne = 1

        fname_out = 'OutPerevod.csv'
        out_text = ''
        out_text_unfind = ''

        #self.kass_all = self.mk_kass_all_full()
        self.kass_all = self.mk_kass_all_full()
        
        for line_str in open(IN_DATA_PATH + 'perevod.csv', 'r', encoding="UTF-8"):
            self.work_vec = line_str.strip().split(';')
            self.surname, self.firstname, self.lastname = self.mk_fio_split()
            
            my_login = self.login()
            
            if not self.login_ok:
                out_text_unfind += f'{self.work_vec[0]};{self.work_vec[1]};{self.work_vec[2]}\n'
                continue
            else:
                for unit in my_login:
                    out_text += unit + ';' + self.work_vec[1] + ';' + self.work_vec[2] + "\n"

        full_out_fname = OUT_DATA_PATH + fname_out
        info += text_to_file(out_text_unfind + out_text, full_out_fname)
        #save_and_show(out_text_unfind + out_text, full_out_fname)
        
        
        #print('\n\n')
        if out_text_unfind:
            info += '\n' + out_text_unfind + '\n'
        info += '\n' + out_text + '\n'

        if out_text_unfind:
            info += '\n\tunfind\n'
        else:
            info += '\n\twell\n'
        self.info = info

u = Perevod()
u.perevod_main()
