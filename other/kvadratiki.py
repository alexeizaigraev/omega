# -*- coding: utf-8 -*-
import os.path, sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)) 

from modules import *

class Kvadratiki():

    def main_kvadratiki(self):
        dir_in = IN_DATA_PATH
        dir_out = OUT_DATA_PATH

        a = file_to_arr(dir_in + "kvadratiki.csv")
        fname_out = 'OutKvadratiki.csv'

        for aa in a:
            for x in aa:
                if not x:
                    x = " "
            

        hor_size_a = len(a[0])
        header = ""
        max = [7, 8, 5, 1, 36, 1, 35, 1, 1, 1, 28, 32, 7, 1, 27, 1, 1, 1, 7, 10, 6]
        head = []
        count_word = -1
        content = []
        for word in a[0]:
            content_line = []
            count_word += 1
            for i in range(1, max[count_word] +1):
                name_col = word + str(i)
                head.append(name_col)
                content_line.append("")
    
        b = a[1:]
        outline = (";").join(head) + "\n"
        lines = head

        for b_line in b:
            start=0
            count_leter = -1
            line = []
            count_word = -1
            for word in b_line:
                count_word += 1
                start += max[count_word]
                for leter in word:
                    try:
                        leter = leter.upper()
                    except:
                        x = 0
                    count_leter += 1
                    line.append(leter)
                if len(line) < start:
                    for i in range(start - len(line)):
                        line.append(" ")
                count_leter = len(line)
            outline += (";").join(line) + "\n"
            lines.append(line)
    
        #with open(dir_out + "out_kvadratiki.csv", 'w', encoding="UTF-8") as out_object:
            #out_object.write(outline)
        full_out_fname = OUT_DATA_PATH + fname_out
        save_and_show(outline, full_out_fname)
        print('## Ok')

z = Kvadratiki()
z.main_kvadratiki()
