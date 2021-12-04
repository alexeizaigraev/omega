import os.path, sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)) 

from modules import *
from papa_pg import *

class DelActualAll():

    def main_del_actual_all(self):
        self.info = ''
        clear_table('departmentsnew')
        self.info += '\n\tclear all actual'