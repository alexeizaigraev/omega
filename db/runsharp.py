import os.path, sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)) 

import subprocess
from modules import file_to_vec


def file_to_vec0(path):
    """ Читает файл в массив. имя файла: path """
    b = []
    with open(path, 'r', encoding="UTF-8") as file:
        for line in file:
            b.append(line.strip())
    return b


app_path = file_to_vec('Config/app_path.txt')[0]
try:
  #os.startfile('C:/Users/a.zaigraev/source/repos/alexeizaigraev/SharpForPy/bin/Release/SharpForPy.exe')
  subprocess.run(app_path)
except Exception as ex:
   print(ex)
