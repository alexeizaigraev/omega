import os.path, sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)) 

from modules import *
from papa_class import *

class Priem(Papa):  

    def mk_term(self):
        return f'{self.mk_dep()}1'

    def mk_short_name(self):
        return f'{self.surname} {self.mk_initial_one_dot()} {self.mk_initial_two_dot()}'

    def mk_name_for_login(self):
        return f'{self.firstname[:2].lower()}{self.lastname[:2].lower()}{self.surname.lower()}'
        

    def mk_shablon(self):
            return self.def_agent()['shablon']
        
    def mk_login(self):
        d = {
            'а': 'a',
            'б': 'b',
            'в': 'v',
            'г': 'g',
            'ґ': 'gh',
            'д': 'd',
            'е': 'e',
            'є': 'ye',
            'ж': 'zh',
            'з': 'z',
            'и': 'y',
            'і': 'i',
            'ї': 'ji',
            'й': 'j',
            'к': 'k',
            'л': 'l',
            'м': 'm',
            'н': 'n',
            'о': 'o',
            'п': 'p',
            'р': 'r',
            'с': 's',
            'т': 't',
            'у': 'u',
            'ф': 'f',
            'х': 'h',
            'ц': 'tz',
            'ч': 'ch',
            'ш': 'sh',
            'щ': 'sch',
            'ь': 'j',
            'ю': 'yu',
            'я': 'ya',
            "'": "y",
            '-': ''}
            
        login = ''
        n = self.mk_name_for_login()
        
        for bukva_ua in n:
            if bukva_ua in d:
                login += d[bukva_ua]
            
        return f'{login}{self.mk_pasp_num()[-4:]}'

    def def_agent(self):
        ag_cod = self.mk_dep()[:3]
        h = dict()
        h['shablon'] = ''
        h['mail'] = ''
        
        for line in open(COMON_DATA_PATH, 'r', encoding="UTF-8"):
            vec = line.split(';')
            if ag_cod in vec[0]:
                h['shablon'] = vec[1]
                h['mail'] = vec[2]
                break
        if not h['shablon']:
            sos('Незнакомый агент', ag_cod)
        return h

    def mk_mail(self):
        mail = self.def_agent()['mail']
        return self.work_vec[self.col_mail] or mail

    def mk_phone(self):
        phone = '380999999999'
        phone2 = self.work_vec[self.col_phone]
        if phone2 \
            and ('-' in phone2) \
            and (len(phone2.replace( "-","" )) == 10 ):
            phone = "38" + phone2.replace( "-","" )
        return phone

    def mk_pasp_seria(self):
        return self.work_vec[self.col_pasp_seria] or "id"

    def mk_pasp_num(self):
        return self.work_vec[self.col_pasp_num] or "3333"

    def mk_pasp_date(self):
        pasp_date = "2020-01-01"
        if self.work_vec[self.col_pasp_date] \
            and (len(self.work_vec[self.col_pasp_date]) ==10 ) \
            and ('.' in self.work_vec[self.col_pasp_date]):
            date = self.work_vec[self.col_pasp_date].split(".")
            pasp_date = f'{date[2]}-{date[1]}-{date[0]}'
        return pasp_date
        
    def mk_pasp_vydan(self):
        pasp_get = "3333"
        try:
            if self.work_vec[self.col_pasp_vydan] and len(self.work_vec[self.col_pasp_vydan]) > 1:
                pasp_get = self.work_vec[self.col_pasp_vydan]
        except:
            pass
        return pasp_get

    
    def priem_main(self):
        info = ''
        self.ColFioOne = 0
        self.ColDepOne = 1
        self.col_phone = 2
        self.col_mail = 3
        self.col_pasp_seria = 4
        self.col_pasp_num = 5
        self.col_pasp_date = 6
        self.col_pasp_vydan = 7

        ofname = OUT_DATA_PATH + 'OutPriem.csv'
        out_text = "Логин;Пароль;ФИО;;;Агент;Терминал;;;;;\n"

        file = file_to_arr(IN_DATA_PATH + 'priem.csv')

        for line in file:
            self.work_vec = line
            self.surname, self.firstname, self.lastname = self.mk_fio_split()
            out_text += (self.mk_login() + ';'
                    + self.mk_login() + ';'
                    + self.mk_short_name() + ';'
                    + self.mk_mail() + ';'
                    + self.mk_phone() + ';'
                    + self.mk_shablon() + ';'
                    + self.mk_term() + ';'
                    + self.mk_pasp_seria() + ';'
                    + self.mk_pasp_num() + ';'
                    + self.mk_pasp_vydan() + ';'
                    + self.mk_pasp_date()
                    + '\n')
        
        info += out_text
        info += '\n\twell\n'
        info += text_to_file(out_text, ofname)
        self.info = info

#u = Priem()
#u.priem_main()
