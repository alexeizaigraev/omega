import os.path, sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)) 

from modules import *
from papa_pg import *

class ActualAll():

    def main_actual_all(self):
        info = ''
        info += refresh_table_actual()
        info +='\nrefresh_all_deps_new\n'
        self.info = info