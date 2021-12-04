
import os
import sys
#import tech
from modules import *
import datetime
import platform
#from colorama import Fore, Style, init


def mk_menu(kv, numm_color):
    #os.system(COM_CLEAR)
    print()
    init()
    my_keys = list(kv.keys())
    num = 0
    p_green('\n' + '_' * 75 + '\n')
    for point in kv:
        num += 1
        if num != numm_color:
            p_cyan(f'\t{num} {point}')
        else:
            p_green(f'\t{num} {point}')

    choice = '99'
    while choice != '0':
        print(f'{Fore.GREEN}\n\n -> ', end='')
        choice = input()
        if '' == choice:
            menu_main()
        elif 0 < int(choice) < len(my_keys) + 1:
            comand = PYTHON_NAME + ' ' + kv[my_keys[int(choice)-1]] + '.py'
            os.system(COM_CLEAR)
            os.system(comand)
            mk_menu(kv, numm_color)
        elif '0' == choice:
            sys.exit()
        else:
            print(f'{Fore.RED} >> wrong choice!')


def menu_main():
    os.system(COM_CLEAR)
    print('\n\n')
    menu = ['1 People',
            '2 Some',
            '3 Monitors',
            '4 Kabinet',
            '5 Other',
            '6 PgBase',]
    for point in menu:
        #print(f'{Fore.YELLOW} {point}', end = '  ')
        if point == menu[-1]:
            p_yellow(f'\t{point}')
        else:
            p_cyan(f'\t{point}')
        
    choise = -1
    while choise != 0:
        print('\n\n -> ', end='')
        choise = input()
        
        if "1"  == choise:
            os.system(COM_CLEAR)
            menu_people()

        if "2"  == choise:
            os.system(COM_CLEAR)
            menu_some()

        if "3"  == choise:
            os.system(COM_CLEAR)
            menu_monitor()

        if "4"  == choise:
            os.system(COM_CLEAR)
            menu_kabinet()
            
        if "5"  == choise:
            os.system(COM_CLEAR)
            menu_other()
        
        if "6"  == choise:
            os.system(COM_CLEAR)
            menu_db()

        elif '0' == choise:
            sys.exit()
        else:
            p_red('\n\twrong choise!')

def menu_people():
    h = {'Priem': 'people/priem',
        'Otpusk': 'people/otpusk',
        'Perevod': 'people/perevod',
        'PostAll': 'people/postall',}
    mk_menu(h, 4)
    
def menu_some():
    h = {'Term': 'some/pg_term',
        'Site': 'some/pg_site',
        'SummuryOtbor': 'some/pg_summury_otbor',
        'Summury': 'some/pg_summury',
        'Summury_ab': 'some/pg_summury_ab',
        'NatashaBig': 'some/natasha_big',
        'active_term': 'some/active_term',
        'Kvadratiki': 'some/kvadratiki',}
    mk_menu(h, len(h)-1)
    os.system(COM_CLEAR)

def menu_monitor():
    h = {'Walker': 'monitor/walker',
        'Monitor': 'monitor/monitor',
        'Accback': 'monitor/accback',
        'Get_RP_Fast': 'monitor/get_rp_fast',
        'Get_rp_all': 'monitor/get_rp_all',
        'gnetz': 'monitor/gnetz',}
    mk_menu(h, len(h))

def menu_kabinet():
    h = {'Rro': 'kabinet/rro',
        'Pereezd': 'kabinet/pereezd',
        'Otmena': 'kabinet/otmena',
        'Prro': 'kabinet/prro',
        'Knigi': 'kabinet/knigi',}
    os.system(COM_CLEAR)
    mk_menu(h, len(h)-1)



def menu_other():
    h = {'Kvadratiki': 'other/kvadratiki',}
    os.system(COM_CLEAR)
    mk_menu(h, 2)


def menu_db():
    h = {#'Refresh_Lite': 'refresh_lite',
        'Refresh_All': 'db/refresh_all',
        #'Runsharp': 'runsharp',
        #'Update_pg': 'update_pg',
        'Otbor': 'db/add_otbor',
        'OtborHard': 'db/add_otbor_hard',
        #'PgToFiles': 'pg_to_files',
        #'Arhiv': 'add_arhiv',
        }
    os.system(COM_CLEAR)
    mk_menu(h, 5)


init()

menu_main()
