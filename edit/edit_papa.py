import os.path, sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)) 


from papa_pg import *
import os

def show(item):
    if len(item) == 7:
        kind = 'departments'
        data = get_one_dep_data(item)[0]
    elif len(item) == 8:
        kind = 'terminals'
        data = get_one_term_data(item)[0]
    head = file_to_arr(IN_DATA_PATH + kind + '.csv')[0]
    text = ''
    for i in range(len(head)):
        text += f'{head[i]};{data[i]}\n'
    save_and_show(text, 'item.txt')

show('1010110')
    
    