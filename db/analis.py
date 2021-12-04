import os.path, sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)) 

from modules import *
from papa_pg import *

class Analis():
        
    def verify(self, fufu, act):
        t = ''
        col_num = 14
        if fufu[col_num] != act[col_num]:
                s = f'verify {fufu[0]}\ndep {fufu[col_num]}\ndepNew {act[col_num]}\n\n'
                t += s
                #print(s)
        return(t)


    def main_analis(self):
        info = ''
        futur_all = get_all_dep_data()
        actual_all = get_all_dep_new_data()

        futur = get_departments_list()
        actual = get_departments_new_list()
        arr = []
        for unit in actual:
            arr.append(unit[0])
        actual = arr

        for act in actual:
            if act not in futur:
                s = f'not in futur {act}\n'
                info += s
                #print(s)

        info += '\n\n'

        for fufu in futur:
            if fufu not in actual:
                s = f'not in actual {fufu}\n'
                info += s
                print(s)

        info += '\n\nverify:\n'

        for fufu in futur_all:
            for act in actual_all:
                if fufu[0] == act[0]:
                    rez = self.verify(fufu, act)
                    if rez:
                        info += rez
        self.info = info
        #print(actual)
        save_and_show(info, 'info.txt')

#u = Analis()
#u.main_analis()
