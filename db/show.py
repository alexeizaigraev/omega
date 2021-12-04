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

def show_act(item):
    if len(item) == 7:
        kind = 'departmentsnew'
        data = get_one_dep_data(item)[0]
    elif len(item) == 8:
        kind = 'terminalsnew'
        data = get_one_term_data(item)[0]
    head = file_to_arr(IN_DATA_PATH + kind[:-3] + '.csv')[0]
    text = ''
    for i in range(len(head)):
        text += f'{head[i]};{data[i]}\n'
    save_and_show(text, 'item.txt')




def proc():
    if choise == 'dep_actual':
        item = otbor[1]
        show_act(item)
    elif choise == 'term_actual':
        item = otbor[0]
        show_act(item)
    elif choise == 'dep_futur':
        item = otbor[1]
        show(item)
    elif choise == 'term_futur':
        item = otbor[0]
        show(item)


quest = ['dep_actual',
        'term_actual',
        'dep_futur',
        'term_futur',]
choise = ask(quest)

print(choise)

otbor = select_table('otbor')[0]
print(otbor)

ask_simpl()
proc()