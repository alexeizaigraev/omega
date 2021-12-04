import os.path, sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)) 

from modules import *
import os
import shutil

class Papa():
    
    def mk_fio(self):
        fio_split = self.work_vec[self.ColFioOne].replace('  ', ' ' ).strip().split(' ')
        
        if len(fio_split) < 3:
            return fio_split[0] + ' ' \
                + fio_split[1] + ' ' \
                + fio_split[1]
        return ' '.join(fio_split)

    def mk_fio_split(self):
        fio_split = self.work_vec[self.ColFioOne].replace('  ', ' ' ).strip().split(' ')
        
        if len(fio_split) < 3:
            return fio_split[0], fio_split[1], fio_split[1]
        return fio_split[0], fio_split[1], fio_split[2]

    def mk_initial_one_dot(self):
        return f'{self.firstname[0]}.'

    def mk_initial_two_dot(self):
        return f'{self.lastname[0]}.'

    def mk_dep(self):
        if '№' in self.work_vec[self.ColDepOne]:
            return self.work_vec[self.ColDepOne].split('№')[-1].strip()
        return self.work_vec[self.ColDepOne].strip()

    def mk_fio_white(self, fff):
        fs = fff.replace('  ', ' ').strip().split(' ')
        surn = fs[0]
        out = surn
        other = ''.join(fs[1:]).replace('.', '').replace(' ', '')
        for leter in other:
            if leter.isupper() and leter.isalpha():
                out += leter
        return out


    def mk_fierd(self):
        all_otpuska = file_to_arr(IN_DATA_PATH + 'all_otpuska.csv')
        a = [line[0] for line in all_otpuska
            if line and 'nul' not in line[3]]
        return a

    
    def mk_kass_all_full(self):
        kass = file_to_arr(IN_DATA_PATH + 'kass_all.csv')
        a = [(line[0], self.mk_fio_white(line[2]), line[3]) for line in kass
            if 'tru' in line[1] and line[-1] and line[-2]]
        return a
   

    def mk_kass_all(self):
        fierd = self.mk_fierd()
        kass = file_to_arr(IN_DATA_PATH + 'kass_all.csv')
        a = [(line[0], self.mk_fio_white(line[2]), line[3]) for line in kass
            if 'tru' in line[1] and line[-1] and line[-2] and line[0] not in fierd]
        return a


    def login_deep(self, nama, parDep):
        logins = [line[0] for line in self.kass_all
            if ( parDep in line[2][1:4]
                and  
                    ( 
                        nama == line[1]
                        or nama in line[1]
                        or line[1] in nama
                    ) 
            )]
        
        if logins and ( 1 == len(logins) ):
            self.login_ok = True

        return logins

 
    
    def login(self):
        parDep = self.mk_dep()
        self.login_ok = False
        nama = self.mk_fio_white(self.mk_fio())

        logins = [line[0] for line in self.kass_all
            if parDep in line[2] and nama == line[1] ]
        
        if logins:
            self.login_ok = True
            return logins

        return self.login_deep(nama, parDep[:3])


    def mk_clear_deps(self, deps):
        outDeps = []
        try:
            dd = deps.replace('[', '').replace(']', '').replace(' ', '')
            if ',' in dd:
                outDeps.append(dd[:7])
            else:
                units = dd.split(',')
                for unit in units:
                    outDeps.append(unit[:7])
        except:
            outDeps.append("0000000")
        return outDeps
        
