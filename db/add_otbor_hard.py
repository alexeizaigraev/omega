import os.path, sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)) 

from modules import *
from papa_pg import *

class OtborHard():
    def __init__(self, terms_choise):
        self.terms = terms_choise
        
    def main_otbor_hard(self):     
        head = 'term;dep\n'
        out = head
       
        for term in self.terms:
            dep = term[:7]
            out += term + ';' + dep + '\n'

        
        info = text_to_file(out, IN_DATA_PATH + 'otbor.csv')
        insert_all_otbor() + '\n\n'
        info += '\n' + out + '\n'
        self.info = info

#u = OtborHard(['10101101', '10101111'])
#u.main_otbor_hard()

