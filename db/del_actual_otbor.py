import os.path, sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)) 

from modules import *
from papa_pg import *

class DelActualOtbor():

    def main_del_actual_otbor(self):
        info = ''
        q = 'SELECT * FROM OTBOR'
        otbor = get_data(q)
        for line in otbor:
            dep = line[1]
            del_dep_new(dep)
            info += f'- {dep}\n'
        self.info = info


