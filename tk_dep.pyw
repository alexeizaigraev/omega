from tkinter import *
#import tkinter
from typing import Any
from modules import *
import os
import sys
import subprocess
from papa_pg import get_partners, get_terminals_list

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))

 
root = Tk()

data = [
['department', ''],
['region', ''],
['district_region', ''],
['district_city', ''],
['city_type', ''],
['city', ''],
['street', ''],
['street_type', ''],
['hous', ''],
['post_index', ''],
['partner', ''],
['status', ''],
['register', ''],
['edrpou', ''],
['address', ''],
['partner_name', ''],
['id_terminal', ''],
['koatu', ''],
['tax_id', ''],
['koatu2', ''],
]
Button(text="Справка").grid(row=0, column=0)
Button(text="Knopka").grid(row=0, column=1)
STEP = 1
PEREHOD = 15
WIGHT_ENTRY = 50
for i in range(len(data)):
    
    col = 1
    col_step = 0
    my_row = i + STEP
    
    if i >= PEREHOD:
        col_step = 2
        my_row = i + STEP - PEREHOD
    vec = data[i]
    
    label = Label(text=vec[0])\
        .grid(row=my_row, column=0 + col_step)
    #entry = Entry(width=WIGHT_ENTRY)
    entry = Entry(width=WIGHT_ENTRY)
    entry.grid(row=my_row, column=1 + col_step)

    entry.insert(0, vec[1])
        #.grid(row=0, column=1, columnspan=3)
 
 
#Button(text="Справка").grid(row=2, column=0)



root.mainloop()