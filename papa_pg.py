from modules import *
import psycopg2
from datetime import datetime

def dbexec(execstr):
    info = ''
    try:
        con = psycopg2.connect(database="postgres", user = "postgres", password = "postgres", host = "127.0.0.1", port = "5432")
        cur = con.cursor()
        cur.execute(execstr)
        con.commit()
    except (Exception) as error:
        info += str(error) + '\n'
    finally:
        if con:
            cur.close()
            con.close()
        
def db_exec_vec(execstr, vec):
    info = ''
    try:
        con = psycopg2.connect(database="postgres", user = "postgres", password = "postgres", host = "127.0.0.1", port = "5432")
        cur = con.cursor()
        cur.execute(execstr, vec)
        con.commit()
    except Exception as error:
        info += str(error) + '\n'
    finally:
        if con:
            cur.close()
            con.close()
    return info
 
            
def clear_table(table):
    execstr =  f'DELETE FROM {table}'
    dbexec(execstr)

def table_from_file_to_arr(fname):
    return file_to_arr(IN_DATA_PATH + fname)[1:]

def refresh_table(table_name, fname):
    info = ''
    clear_table(table_name)
    arr = table_from_file_to_arr(fname)
    con = psycopg2.connect(database="postgres", user = "postgres", password = "postgres", host = "127.0.0.1", port = "5432")
    cur = con.cursor()
    for vec in arr:
        if table_name == 'departments':
            query = f'''INSERT INTO departments (department, region, district_region, district_city, city_type, city, street, street_type, hous, post_index, partner, status, register, edrpou, address, partner_name, id_terminal, koatu, tax_id)
VALUES ('{vec[0]}', '{vec[1]}', '{vec[2]}', '{vec[3]}', '{vec[4]}', '{vec[5]}', '{vec[6]}', '{vec[7]}', '{vec[8]}', '{vec[9]}', '{vec[10]}', '{vec[11]}', '{vec[12]}', '{vec[13]}', '{vec[14]}', '{vec[15]}', '{vec[16]}', '{vec[17]}', '{vec[18]}');'''
        elif table_name == 'terminals':
            query = f'''INSERT INTO terminals (department, termial, model, serial_number, date_manufacture, soft, producer, rne_rro, sealing, fiscal_number, oro_serial, oro_number, ticket_serial, ticket_1sheet, ticket_number, sending, books_arhiv, tickets_arhiv, to_rro, owner_rro)
VALUES ('{vec[0]}', '{vec[1]}', '{vec[2]}', '{vec[3]}', '{vec[4]}', '{vec[5]}', '{vec[6]}', '{vec[7]}', '{vec[8]}', '{vec[9]}', '{vec[10]}', '{vec[11]}', '{vec[12]}', '{vec[13]}', '{vec[14]}', '{vec[15]}', '{vec[16]}', '{vec[17]}', '{vec[18]}', '{vec[19]}')
'''
        elif table_name == 'otbor':
            query = f''' INSERT INTO otbor (term, dep)
VALUES ('{vec[0]}', '{vec[1]}')'''
        try:
            cur.execute(query)
        except Exception as ex:
            info += str(ex) + '\n'
    con.commit()
    if con:
        cur.close()
        con.close()
    info += f'refresh {table_name}\n\n'
    return info


def title_string(s):
    return s.title()



def insert_all_deps():
    return refresh_table('departments', 'departments.csv')


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
    return refresh_table('terminals', 'terminals.csv')




def insert_all_otbor():
    return refresh_table('otbor', 'otbor.csv')

  

def table_to_file(tname):
    info = ''
    q_err = 0
    arr = []
    try:
        con = psycopg2.connect(database="postgres", user = "postgres", password = "postgres", host = "127.0.0.1", port = "5432")
        cur = con.cursor()
        cur.execute(f'SELECT *  FROM {tname}')
        rows = cur.fetchall()
    except (Exception) as error:
        q_err += 1
        info == str(error) + '\n'
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
    fname = OUT_DATA_PATH + f'pg_{tname}.csv'
    text_to_file(text, fname)
    info += fname + '\n'
    return info


def select_terms_to_file():
    return table_to_file('terminals')
 
def select_deps_to_file():
    return table_to_file('departments')


def select_table(tname):
    info = ''
    q_err = 0
    arr = []
    try:
        con = psycopg2.connect(database="postgres", user = "postgres", password = "postgres", host = "127.0.0.1", port = "5432")
        cur = con.cursor()
        cur.execute(f'SELECT *  FROM {tname}')
        rows = cur.fetchall()
    except (Exception) as error:
        q_err += 1
        info += str(error) + '\n'
    finally:
        if con:
            cur.close()
            con.close()
    return rows, info

def select_deps():
    return select_table('departments')
        
def select_terms():
    return select_table('terminals')


def get_data(query):
    info = ''
    q_err = 0
    arr = []
    try:
        con = psycopg2.connect(database="postgres", user = "postgres", password = "postgres", host = "127.0.0.1", port = "5432")
        cur = con.cursor()
        cur.execute(query)
        rows = cur.fetchall()
    except (Exception) as error:
        q_err += 1
        info += str(error) + '\n'
    finally:
        if con:
            cur.close()
            con.close()
    
    return rows


    



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
        con = psycopg2.connect(database="postgres", user = "postgres", password = "postgres", host = "127.0.0.1", port = "5432")
        cur = con.cursor()
        cur.execute(query)
        rows = cur.fetchall()

    except (Exception) as error:
        q_err += 1
    finally:
        if con:
            cur.close()
            con.close()
    
    for line in rows:
        if line[0]:
            arr.append(line[0])
    return arr




def get_terminals_list():
    q_err = 0
    query = f'''SELECT termial FROM terminals
ORDER BY termial'''
    arr = []
    try:
        con = psycopg2.connect(database="postgres", user = "postgres", password = "postgres", host = "127.0.0.1", port = "5432")
        cur = con.cursor()
        cur.execute(query)
        rows = cur.fetchall()

    except (Exception) as error:
        q_err += 1
    finally:
        if con:
            cur.close()
            con.close()
    out_list = []
    for unit in rows:
        out_list.append(unit[0])
    
    return out_list


def get_terminals_list_partner(partner):
    q_err = 0
    query = f'''SELECT termial FROM terminals, departments
    WHERE departments.department = terminals.department
    AND departments.partner = '{partner}'
ORDER BY termial;'''
    arr = []
    try:
        con = psycopg2.connect(database="postgres", user = "postgres", password = "postgres", host = "127.0.0.1", port = "5432")
        cur = con.cursor()
        cur.execute(query)
        rows = cur.fetchall()

    except (Exception) as error:
        q_err += 1
    finally:
        if con:
            cur.close()
            con.close()
    out_list = []
    for unit in rows:
        out_list.append(unit[0])
    
    return out_list


def get_departments_list():
    q_err = 0
    query = f'''SELECT department FROM departments
ORDER BY department'''
    arr = []
    try:
        con = psycopg2.connect(database="postgres", user = "postgres", password = "postgres", host = "127.0.0.1", port = "5432")
        cur = con.cursor()
        cur.execute(query)
        rows = cur.fetchall()

    except (Exception) as error:
        q_err += 1
    finally:
        if con:
            cur.close()
            con.close()
    out_list = []
    for unit in rows:
        out_list.append(unit[0])
    
    return out_list

def get_departments_new_list():
    q_err = 0
    query = f'''SELECT department FROM departmentsnew
ORDER BY department'''
    arr = []
    try:
        con = psycopg2.connect(database="postgres", user = "postgres", password = "postgres", host = "127.0.0.1", port = "5432")
        cur = con.cursor()
        cur.execute(query)
        rows = cur.fetchall()

    except (Exception) as error:
        q_err += 1
    finally:
        if con:
            cur.close()
            con.close()
    out_list = []
    for unit in rows:
        out_list.append(unit)
    
    return out_list



def get_otbor_deps():
    query = f'''SELECT dep FROM otbor
ORDER BY dep'''
    q_err = 0
    arr = []
    try:
        con = psycopg2.connect(database="postgres", user = "postgres", password = "postgres", host = "127.0.0.1", port = "5432")
        cur = con.cursor()
        cur.execute(query)
        rows = cur.fetchall()

    except (Exception) as error:
        q_err += 1
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








def get_kabinet_pereezd_old_data():
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




def get_history_data():
    query = '''SELECT terminals.termial, terminals.department,
terminals.serial_number, departments.address
FROM terminals, departments, otbor
WHERE terminals.department = departments.department
AND terminals.termial = otbor.term
ORDER BY terminals.termial;'''
    return get_data(query)

def get_activ_term_data():
    query = '''SELECT terminals.termial, terminals.department,
departments.address, departments.partner
FROM terminals, departments
WHERE terminals.department = departments.department
ORDER BY terminals.termial;'''
    return get_data(query)

def get_one_term_data(term):
    query = f'''SELECT * 
FROM terminals
WHERE terminals.termial = '{term}';'''
    return get_data(query)

def get_one_dep_data(dep):
    query = f'''SELECT * 
FROM departments
WHERE departments.department = '{dep}';'''
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

def loger_pg(kind):
    data = get_history_data()
    nau = date_log()
    con = psycopg2.connect(database="postgres", user = "postgres", password = "postgres", host = "127.0.0.1", port = "5432")
    cur = con.cursor()
    #p_blue('db open ok')
    
    for vec in data:
        query = f""" INSERT INTO logi (department, termial, serial_number, address, datalog, kind)
VALUES ('{vec[0]}', '{vec[1]}', '{vec[2]}', '{vec[3]}', '{nau}', '{kind}');"""
        try:
            cur.execute(query)
        except Exception as ex:
            pass               
    con.commit()
    
    if con:
        cur.close()
        con.close()

    now = str(datetime.strftime(datetime.now(), "%Y-%m-%d_%H_%M_%S"))
    out_path = 'R:/DRM/BackupAccess/db2_be_' + now + '_' + kind + '.accdb'
    in_path = IN_DATA_PATH + 'drm.db'
    try:
        shutil.copy(in_path, out_path)
    except:
        pass


#_actual___________________________




def del_dep_new(dep):
    q=f"""DELETE FROM public.departmentsnew
	WHERE department = '{dep}';
    """
    dbexec(q)

def del_dep(dep):
    q=f"""DELETE FROM public.departments
	WHERE department = '{dep}';
    """
    dbexec(q)


    
def get_all_dep_data():
    q = 'SELECT * FROM departments'
    return get_data(q)

def get_all_dep_new_data():
    q = 'SELECT * FROM departmentsnew'
    return get_data(q)

def get_one_dep_data(dep):
    q = f"""SELECT * FROM departments WHERE department = '{dep}';"""
    return get_data(q)

def get_one_dep_new_data(dep):
    q = f"""SELECT * FROM departments WHERE departmentnew = '{dep}';"""
    return get_data(q)


def refresh_table_actual():
    info = ''
    clear_table('departmentsnew')
    arr = get_all_dep_data()
    con = psycopg2.connect(database="postgres", user = "postgres", password = "postgres", host = "127.0.0.1", port = "5432")
    cur = con.cursor()
    for vec in arr:
        query = f'''INSERT INTO departmentsnew (department, region, district_region, district_city, city_type, city, street, street_type, hous, post_index, partner, status, register, edrpou, address, partner_name, id_terminal, koatu, tax_id)
VALUES ('{vec[0]}', '{vec[1]}', '{vec[2]}', '{vec[3]}', '{vec[4]}', '{vec[5]}', '{vec[6]}', '{vec[7]}', '{vec[8]}', '{vec[9]}', '{vec[10]}', '{vec[11]}', '{vec[12]}', '{vec[13]}', '{vec[14]}', '{vec[15]}', '{vec[16]}', '{vec[17]}', '{vec[18]}');'''
        try:
            cur.execute(query)
        except Exception as ex:
            info += str(ex) + '\n'
    con.commit()
    if con:
        cur.close()
        con.close()
    #info += f'refresh dep new\n\n'
    return info


def title_string(s):
    return s.title()

    
   
def act_refresh_one_dep(dep):
    dep = str(dep)
    vec = []
    try:
        vec = get_one_dep_data(dep)
    except Exception as ex:
        pass
    try:
        del_dep_new(dep)
    except:
        pass
    try:
        query = f"""INSERT INTO departmentsnew (department, region, district_region, district_city, city_type, city, street, street_type, hous, post_index, partner, status, register, edrpou, address, partner_name, id_terminal, koatu, tax_id, koatu2)
    VALUES ('{vec[0]}', '{vec[1]}', '{vec[2]}', '{vec[3]}', '{vec[4]}', '{vec[5]}', '{vec[6]}', '{vec[7]}', '{vec[8]}', '{vec[9]}', '{vec[10]}', '{vec[11]}', '{vec[12]}', '{vec[13]}', '{vec[14]}', '{vec[15]}', '{vec[16]}', '{vec[17]}', '{vec[18]}' , '{vec[19]}');"""
        dbexec(query)
    except:
        pass




verb = False



