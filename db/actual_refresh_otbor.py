import os.path, sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)) 

from modules import *
from papa_pg import *


class ActualRefreshOtbor():

    def main_actual_refresh_otbor(self):
        info = ''
        otbor, inf = select_table('otbor')
        info += inf + '\n'
        
        """
        refresh dep
        """
        for line in otbor:
            dep = line[1]
            try:
                act_refresh_one_dep(dep)
                info += f'+ {dep}\n'
            except Exception as ex:
                info += f'+ {ex}\n'
        info += '\n\t refreshed actual otbor\n'
        self.info = info
