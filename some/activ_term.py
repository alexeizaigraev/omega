# -*- coding: utf-8 -*-
import os.path, sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)) 


from modules import *
#from papa import *
from papa_pg import *

class ActivTerm():

    def main_activ_term(self):
        info = ''
        term_management = file_to_arr(IN_DATA_PATH + 'terminals_management_2_col.csv')
        tm = [line[0] for line in term_management if 'true' in line[1] and len(line[0]) > 7]
        data = get_activ_term_data()
        natasha = mk_natasha()
        outtext = 'Терминал;Отделение;Адрес;Партнёр\n'
        sum = 0
        h_partner = dict()
        for data_line in data:
            data_term = data_line[0]
            data_dep = data_line[0][:7]
            if data_dep not in natasha or data_term not in tm:
                continue
            outtext += ';'.join(data_line) + '\n'
            partner = data_line[-1]
            if partner in h_partner:
                h_partner[partner] += 1
            else:
                h_partner[partner] = 1
            sum += 1

        outtext += f'\n{sum=}\n\n'
        #print(f'\n{sum=}\n\n')
        info += f'\n{sum=}\n\n'

        for partner in h_partner:
            outtext += f'{partner};{h_partner[partner]}\n'
            #print(f'{partner};{h_partner[partner]}')
            info += f'{partner};{h_partner[partner]}\n\n'
            
        fout = OUT_DATA_PATH + 'activ_term.csv'

        info += text_to_file(outtext, fout)
        #save_and_show(outtext, fout)
        self.info = info
        #print(tm)

