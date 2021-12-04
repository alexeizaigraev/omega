import os.path, sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)) 


from papa_pg import *
import os
import shutil
import subprocess

class RefreshAll():

    def to_gdrive(self, fname):
        info = ''
        try:
            shutil.copy(IN_DATA_PATH + fname, GDRIVE_PATH + f'access_files/{fname}')
            info += GDRIVE_PATH + f'access_files/{fname}\n'
        except Exception as ex:
            info += str(ex) + '\n'
        return info

    def main_refresh(self):
        info = ''
        app_path = file_to_vec('Config/app_path.txt')[0]
        try:
            #os.startfile('C:/Users/a.zaigraev/source/repos/alexeizaigraev/SharpForPy/bin/Release/SharpForPy.exe')
            subprocess.run(app_path)
        except Exception as ex:
            info += str(ex) + '\n'

        verb = True

        info += insert_all_deps() + '\n'
        info += insert_all_terms() + '\n'
        info += insert_all_otbor() + '\n\n'

        fnames = ['otbor.csv', 'departments.csv', 'terminals.csv']
        for name in fnames:
            info += self.to_gdrive(name)
        self.info = info