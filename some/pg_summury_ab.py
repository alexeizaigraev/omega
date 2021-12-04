import os.path, sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)) 

from modules import *
from papa_pg import *


class SummuryAb():

    def get_summury_data(self):
        u = "'1700999'"
        query = f'''SELECT department, address, partner
    FROM departmentsnew
    WHERE department != {u}
    ORDER BY department;'''
        return get_data(query)

    def main_summury_ab(self):
        info = ''
        head = '№ п/п;"№ Відділення ТОВ ""ЕПС""";Адреса;Партнер\n'
        out_text = head

        data = self.get_summury_data()

        natasha = mk_natasha()
        my_deps = []
        sum = 1
        count_line = 0
        for line in data:
            if line[0] not in natasha:
                continue
            sum += 1
            count_line += 1
            out_line = f'{count_line};{line[0]};{line[1]};{line[2]}'
            out_text += out_line + '\n'

            
        ofName = OUT_DATA_PATH + 'summury_ab.csv'
        info += text_to_file(out_text, ofName)
        info += f'\n\t{sum - 1}'
        self.info = info

#u = SummuryAb()
#u.main_summury_ab()
