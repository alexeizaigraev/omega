from modules import *
import sqlite3 as sq
from datetime import datetime


def db_operator(execstr, vec=[]):
    try:
        con = sq.connect(db_path)
        cur = con.cursor()

        if vec:
            cur.execute(execstr, vec)
        else:
            cur.execute(execstr)
        con.commit()
        if verb:
            print(vec[0])
    except Exception as error:
        print('>>', error)
    finally:
        if con:
            cur.close()
            con.close()

            
def clear_table(table):
    db_operator(f'DELETE FROM {table}')
def clear_otbor():
    clear_table('otbor')
def clear_dep():
    clear_table('departments')
def clear_term():
    clear_table('terminals')


def insert_otbor(v):
    query = f""" INSERT INTO otbor (term, dep)
                              VALUES ({v[0]}, {v[1]});"""
    db_operator(query)

def insert_one_dep(v):
    #print('# insert_one_dep')
    q = '''INSERT INTO departments (department, region, district_region, district_city, city_type, city, street, street_type, hous, post_index, partner, status, register, edrpou, address, partner_name, id_terminal, koatu, tax_id)
VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);'''
    db_operator(q, v)
    
def insert_one_term(v):
    #print('# insert_one_term')
    q = '''INSERT INTO terminals (department, termial, model, serial_number, date_manufacture, soft, producer, rne_rro, sealing, fiscal_number, oro_serial, oro_number, ticket_serial, ticket_1sheet, ticket_number, sending, books_arhiv, tickets_arhiv, to_rro, owner_rro)
VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
'''
    db_operator(q, v)    



def title_string(s):
    return s.title()


def test_len(arr, goog_len):
    for line in arr:
        print('\t' + line)
        print(f'{line[0]} {len(line)}')
        if len(line) != goog_len:
            print(f'err: {line[0]=}\n {len(line)=}')



def insert_all_deps():
    clear_dep()
    q_err = 0
    query0 = '''INSERT INTO departments (department, region, district_region, district_city, city_type, city, street, street_type, hous, post_index, partner, status, register, edrpou, address, partner_name, id_terminal, koatu, tax_id, koatu2)
VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);'''
    query = '''INSERT INTO departments (department, region, district_region, district_city, city_type, city, street, street_type, hous, post_index, partner, status, register, edrpou, address, partner_name, id_terminal, koatu, tax_id)
VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);'''

    con = sq.connect(db_path)
    cur = con.cursor()
    data = file_to_arr(IN_DATA_PATH + 'departments.csv')
    if 'department' in data[0][0]:
        data = data[1:]
    size_line = len(data[0])
    #count_line = -1
    for vec in data:
        #vec.append('')
        try:
            cur.execute(query, vec)
        except Exception as ex:
                print(ex)
        
        con.commit()
        
    if con:
        cur.close()
        con.close()

    if q_err == 0:
        p_blue('refresh deps\n')
    else:
        print('refresh deps', 'errors:', q_err, '\n')







def insert_all_deps_ORIGINAL():
    clear_dep()
    q_err = 0
    query = '''INSERT INTO departments (department, region, district_region, district_city, city_type, city, street, street_type, hous, post_index, partner, status, register, edrpou, address, partner_name, id_terminal, koatu, tax_id, koatu2)
VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);'''

    con = sq.connect(db_path)
    cur = con.cursor()
    data = file_to_arr(IN_DATA_PATH + 'departments.csv')
    if 'department' in data[0][0]:
        data = data[1:]
    size_line = len(data[0])
    count_line = -1
    for vec in data:
        vec.append('')
        if vec[0] and len(vec) == size_line + 1:
            try:
                cur.execute(query, vec)
            except Exception as ex:
                print(ex)
        else:
            q_err += 1
            print(f'>> {vec[0]} {len(vec)=}')                    
        con.commit()
        
    if con:
        cur.close()
        con.close()

    if q_err == 0:
        p_blue('refresh deps\n')
    else:
        print('refresh deps', 'errors:', q_err, '\n')






def mk_finish0(reg_date, mod):
    
    didi = {
        'Екселліо FP-280': 7,
        'Екселліо FP-700': 7,
        'Екселліо FPP-350': 0,
        'Екселліо FPU-550ES': 7,
        'Екселліо FPU-550ES': 7,
        'Екселліо FP-280': 5,
        'ПРРО': 10,
        'УЕ РККС': 0,
        }
    dd, mm, yy = reg_date.split('.')
    #yy = yy[:4]
    new_year = int(yy) + didi[mod]
    return f'{dd}.{mm}.{new_year}'


def good_date(vec):
    positions = [4, 15, 20, 21,]
    for pos in positions:
        vec[pos] = vec[pos][:10]
    return vec

def make_finish(vec):
    model = vec[2]
    register = vec[20]
    finish = vec[21]
    if not finish and register and model:
        try:
            vec[21] = mk_finish0(register, model)
        except:
            pass
            return vec



def insert_all_terms():
    clear_term()
    q_err = 0
    query = '''INSERT INTO terminals (department, termial, model, serial_number, date_manufacture, soft, producer, rne_rro, sealing, fiscal_number, oro_serial, oro_number, ticket_serial, ticket_1sheet, ticket_number, sending, books_arhiv, tickets_arhiv, to_rro, owner_rro, register, finish)
VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
'''

    con = sq.connect(db_path)
    cur = con.cursor()
    #p_blue('db open ok')
    data = file_to_arr(IN_DATA_PATH + 'terminals.csv')
    if 'department' in data[0][0]:
        data = data[1:]
    size_line = len(data[0])
    for vec in data:
        # cat time
        #vec = good_date{vec}
            
        # make finish
        #vec = make_finish(vec)
             
        if vec[1] and len(vec) == size_line:
            try:
                cur.execute(query, vec)
            except:
                p_red(query)
                q_err += 1
        else:
            print(f'>> {vec[1]} {len(vec)=}')
        if verb:
            print(vec[1])                
    con.commit()
        
    if con:
        cur.close()
        con.close()

    if q_err == 0:
        p_blue('refresh terms\n')
    else:
        print('refresh terms', 'errors:', q_err, '\n')


def insert_all_otbor00000():
    #print('# insert_all_otbor')
    clear_otbor()
    con = sq.connect(db_path)
    cur = con.cursor()
    data = file_to_arr(IN_DATA_PATH + 'otbor.csv')
    if 'term' in data[0][0]:
       data = data[1:]
    query = f""" INSERT INTO otbor (term, dep)
VALUES (?, ?);"""
    cur.executemany(query, data)
    con.commit()
    
    if con:
        cur.close()
        con.close()
    print('refresh otbor\n')




def insert_all_otbor():
    #print('# insert_all_otbor')
    clear_otbor()
    q_err = 0

    con = sq.connect(db_path)
    cur = con.cursor()
    #p_blue('db open ok')

    data = file_to_arr(IN_DATA_PATH + 'otbor.csv')
    if 'term' in data[0][0]:
       data = data[1:]
    size_line = len(data[0])
        
    for vec in data:
        if vec[0] and vec[1] and len(vec) == size_line:
            query = f""" INSERT INTO otbor (term, dep)
VALUES ({vec[0]}, {vec[1]});"""
            try:
                cur.execute(query)
            except Exception as ex:
                print(ex)
                q_err += 1
        else:
            print(f'>> {vec[1]} {len(vec)=}')                    
        #con.commit()
        if verb:
            print(vec[1])                
    con.commit()
    
    if con:
        cur.close()
        con.close()

    if q_err == 0:
        p_blue('refresh otbor\n')
    else:
        print('refresh otbor', 'errors:', q_err, '\n')



def send_to_gdrive(tname):
    #print(f'# send {tname} to Gdrive')
    q_err = 0
    arr = []
    try:
        con = sq.connect(db_path)
        cur = con.cursor()
        #p_blue('db open ok')
        cur.execute(f'SELECT *  FROM {tname}')
        rows = cur.fetchall()
        
    except (Exception) as error:
        q_err += 1
        print('>>', error)
    
    finally:
        if con:
            cur.close()
            con.close()
    
    text = ''
    for vec in rows:
        text += ';'.join(vec) + ';' + datetime.strftime(datetime.now(), "%Y.%m.%d %H:%M:?") + '\n'
    
    text_add_file(text, GDRIVE_PATH + f'arhiv/{tname}.csv')



def select_deps_to_gdrive():
    send_to_gdrive('departments')

def select_terms_to_gdrive():
    send_to_gdrive('terminals')
    
    
  

def table_to_file(tname):
    print(f'# {tname} to file')
    q_err = 0
    arr = []
    try:
        con = sq.connect(db_path)
        cur = con.cursor()
        #p_blue('db open ok')
        cur.execute(f'SELECT *  FROM {tname}')
        rows = cur.fetchall()
        #arr_to_file(rows, IN_DATA_PATH + 'pg_departments.csv')      

    except (Exception) as error:
        q_err += 1
        print('>>', error)
    finally:
        if con:
            cur.close()
            con.close()

    if tname == 'departments':
        text = 'department;region;district_region;district_city;city_type;city;street;street_type;hous;post_index;partner;status;register;edrpou;address;partner_name;id_terminal;koatu;tax_id;koatu2\n'
    else:
        text = 'department;termial;model;serial_number;date_manufacture;soft;producer;rne_rro;sealing;fiscal_number;oro_serial;oro_number;ticket_serial;ticket_1sheet;ticket_number;sending;books_arhiv;tickets_arhiv;to_rro;owner_rro;register;finish\n'

    for vec in rows:
        text += ';'.join(vec) + '\n'
    
    text_to_file(text, OUT_DATA_PATH + f'pg_{tname}.csv')


def select_terms_to_file():
    table_to_file('terminals')
 
def select_deps_to_file():
    table_to_file('departments')


def select_table(tname):
    q_err = 0
    arr = []
    try:
        con = sq.connect(db_path)
        cur = con.cursor()
        cur.execute(f'SELECT *  FROM {tname}')
        rows = cur.fetchall()
        
    except (Exception) as error:
        q_err += 1
        print('>>', error)
    finally:
        if con:
            cur.close()
            con.close()
    return rows

def select_deps():
    return select_table('departments')
        
def select_terms():
    return select_table('terminals')


def get_data(query):
    q_err = 0
    arr = []
    try:
        con = sq.connect(db_path)
        cur = con.cursor()
        cur.execute(query)
        rows = cur.fetchall()

    except (Exception) as error:
        q_err += 1
        print('>>', error)
    finally:
        if con:
            cur.close()
            con.close()
    
    return rows


    

def get_terms_data():
    query = '''SELECT otbor.term, departments.id_terminal, departments.city,departments.region, 
departments.street_type, departments.street, departments.hous, 
terminals.serial_number, terminals.fiscal_number
FROM otbor, terminals, departments
WHERE otbor.term = terminals.termial
AND departments.department = terminals.department
ORDER BY terminals.termial;'''
    return get_data(query)

def get_deps_data():
    query = '''SELECT department, region, district_region, district_city, city_type, city, street, street_type, hous, post_index, partner, status, register, edrpou, address, partner_name, id_terminal, koatu, tax_id, koatu2
	FROM public.departments;'''
    return get_data(query)


def get_partners():
    u = "'1700999'"
    q_err = 0
    query = f'''SELECT DISTINCT partner
FROM departments
WHERE department != {u}
ORDER BY partner;'''
    arr = []
    try:
        con = sq.connect(db_path)
        cur = con.cursor()
        cur.execute(query)
        rows = cur.fetchall()

    except (Exception) as error:
        q_err += 1
        print('>>', error)
    finally:
        if con:
            cur.close()
            con.close()
    
    for line in rows:
        if line[0]:
            arr.append(line[0])
    return arr



def get_summury_data():
    u = "'1700999'"
    query = f'''SELECT department, address, partner
FROM departments
WHERE department != {u}
ORDER BY department;'''
    return get_data(query)

def get_summury_partner_data(partner):
    u = "'1700999'"
    query = f'''SELECT department, region, district_region, post_index, city_type, city, district_city, street_type, street, hous, address, koatu, koatu2
FROM departments
WHERE department != {u} 
AND partner ='{partner}'
ORDER BY department;'''
    return get_data(query)


def get_site_data():
    query = f'''SELECT department, edrpou, address, register  FROM departments ORDER BY department'''
    return get_data(query)

def get_natasha_data():
    query = f'''SELECT department, edrpou, partner FROM departments
ORDER BY partner'''
    return get_data(query)

def get_terminals_list():
    q_err = 0
    print('# get_terminals_list')
    query = f'''SELECT termial FROM terminals
ORDER BY termial'''
    arr = []
    try:
        con = sq.connect(db_path)
        cur = con.cursor()
        cur.execute(query)
        rows = cur.fetchall()

    except (Exception) as error:
        q_err += 1
        print('>>', error)
    finally:
        if con:
            cur.close()
            con.close()
    out_list = []
    for unit in rows:
        out_list.append(unit[0])
    
    return out_list


def get_otbor_deps():
    query = f'''SELECT dep FROM otbor
ORDER BY dep'''
    q_err = 0
    arr = []
    try:
        con = sq.connect(db_path)
        cur = con.cursor()
        p_blue('db open ok')
        cur.execute(query)
        rows = cur.fetchall()

    except (Exception) as error:
        q_err += 1
        print('>>', error)
    finally:
        if con:
            cur.close()
            con.close()
    out_list = []
    for unit in rows:
        out_list.append(unit[0])
    
    return out_list



def col_key_pg(hh, key_col_num = -1):
    os.system('cls')
    print('\n\n')
    s = set()
    for line in hh:
        try:
            key = line[key_col_num]
            s.add(key)
        except:
            #('>> no key', key)
            pass
    
    listkey = list(s)
    for i in range(len(listkey)):
        if not listkey[i]:
            continue
        p_cyan(f'\t{i} {listkey[i]}')
    
    #print('')
    print('\n\n\n -> ', end = '')
    choise = int(input())
    os.system('cls')
    
    return listkey[choise]


def get_kabinet_prro_data():
    query = '''SELECT departments.tax_id, departments.koatu, departments.department,
departments.address
FROM otbor, departments
WHERE otbor.dep = departments.department
ORDER BY departments.department;'''
    return get_data(query)


def get_kabinet_knigi_data():
    query = '''SELECT terminals.fiscal_number, terminals.model, terminals.serial_number,
terminals.soft, terminals.rne_rro, terminals.department,
departments.address, departments.koatu, departments.tax_id,
terminals.oro_number, terminals.oro_serial,
otbor.term
FROM otbor, terminals, departments
WHERE otbor.term = terminals.termial
AND departments.department = terminals.department
ORDER BY terminals.termial;'''
    return get_data(query)


def get_kabinet_rro_data():
    query = '''SELECT terminals.department,
departments.post_index, departments.region, departments.district_region,
departments.city, departments.street, departments.hous,
departments.koatu, departments.tax_id,
terminals.model, terminals.serial_number, terminals.soft,
terminals.producer, terminals.date_manufacture,
terminals.rne_rro, terminals.oro_serial, terminals.ticket_serial,
otbor.term
FROM otbor, terminals, departments
WHERE otbor.term = terminals.termial
AND departments.department = terminals.department
ORDER BY terminals.termial;'''
    return get_data(query)


def get_kabinet_pereezd_data():
    query = '''SELECT terminals.department,
departments.post_index, departments.region,
departments.city, departments.street, departments.hous,
departments.koatu, departments.tax_id,
terminals.model, terminals.serial_number, terminals.soft,
terminals.producer, terminals.date_manufacture,
terminals.rne_rro, terminals.fiscal_number, terminals.oro_serial, terminals.ticket_serial,
terminals.to_rro,
otbor.term
FROM otbor, terminals, departments
WHERE otbor.term = terminals.termial
AND departments.department = terminals.department
ORDER BY terminals.termial;'''
    return get_data(query)

def get_kabinet_otmena_data():
    query = '''SELECT terminals.ticket_number, terminals.serial_number,
terminals.model, terminals.soft, terminals.rne_rro, 
departments.address, departments.koatu, departments.tax_id,
terminals.fiscal_number, departments.department
FROM otbor, terminals, departments
WHERE otbor.term = terminals.termial
AND departments.department = terminals.department
ORDER BY terminals.termial;'''
    return get_data(query)


def insert_all_depsarhiv():
    now = str(datetime.strftime(datetime.now(), "%d.%m.%Y %H:%M:?"))
    data = select_deps()
    #print(data)
    q_err = 0
    query = '''INSERT INTO public.departmentsarhiv(
department, region, district_region, district_city, city_type, city, street, street_type, hous, post_index, partner, status, register, edrpou, address, partner_name, id_terminal, koatu, tax_id, koatu2, datetime)
VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);'''

    try:
        con = sq.connect(db_path)
        cur = con.cursor()
        q_err = 0
        
        for vec in data:
            if not vec:
                continue
            vec = list(vec)
            try:
                vec.append(now)
                #print(vec)
                cur.execute(query, vec)
                
            except (Exception) as error:
                q_err += 1
                print('>>', error)

            if verb:
                pass
                #print(vec[0])                
        con.commit()
    except:
        pass
    finally:
        if con:
            cur.close()
            con.close()

    if q_err == 0:
        p_blue('insert_all_depsarhiv\n')
    else:
        print('insert_all_depsarhiv', 'errors:', q_err, '\n')



def insert_all_termsarhiv():
    now = str(datetime.strftime(datetime.now(), "%d.%m.%Y %H:%M:?"))
    data = select_terms()
    #print(data)
    q_err = 0
    query = '''INSERT INTO public.terminalsarhiv(
	department, termial, model, serial_number, date_manufacture, soft, producer, rne_rro, sealing, fiscal_number, oro_serial, oro_number, ticket_serial, ticket_1sheet, ticket_number, sending, books_arhiv, tickets_arhiv, to_rro, owner_rro, register, finish, datetime)
	VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);'''

    try:
        con = sq.connect(db_path)
        cur = con.cursor()
        q_err = 0
        
        for vec in data:
            if not vec:
                continue
            vec = list(vec)
            try:
                vec.append(now)
                cur.execute(query, vec)
                
            except (Exception) as error:
                q_err += 1
                print('>>', error)

            if verb:
                pass
                #print(vec[0])                
        con.commit()
    except:
        pass
    finally:
        if con:
            cur.close()
            con.close()

    if q_err == 0:
        p_blue('insert_all_termsarhiv\n')
    else:
        print('insert_all_termsarhiv', 'errors:', q_err, '\n')




def get_history_data():
    query = '''SELECT terminals.termial, terminals.department,
terminals.serial_number, departments.address
FROM terminals, departments, otbor
WHERE terminals.department = departments.department
AND terminals.termial = otbor.term
ORDER BY terminals.termial;'''
    return get_data(query)




def date_log():
    ddd = datetime.now().date()
    d = str(ddd.day)
    if len(d) == 1:
        d = '0' + d
    m = str(ddd.month)
    if len(m) == 1:
        m = '0' + m
    y = str(ddd.year)
    return f'{y}.{m}.{d}'

def loger_sq(kind):
    data = get_history_data()
    nau = date_log()
    con = sq.connect(db_path)
    cur = con.cursor()
    #p_blue('db open ok')
    
    for vec in data:
        query = f""" INSERT INTO history (term, dep, serial, adres, date_hist, kind)
VALUES ('{vec[0]}', '{vec[1]}', '{vec[2]}', '{vec[3]}', '{nau}', '{kind}');"""
        try:
            cur.execute(query)
        except Exception as ex:
            print(ex)
        if verb:
            print(vec[1])                
    con.commit()
    
    if con:
        cur.close()
        con.close()

    try:
        os.system(PYTHON_NAME + ' accback.py')
    except Exception as ex:
        print(ex)








db_path = IN_DATA_PATH + 'drm.db'
verb = False
