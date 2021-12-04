from modules import *
#from papa_sq import db_operator
from papa_pg import dbexec


dbexec("""
            CREATE TABLE IF NOT EXISTS departments (
            department TEXT PRIMARY KEY DEFAULT '',
            region TEXT DEFAULT '',
            district_region TEXT DEFAULT '',
            district_city TEXT DEFAULT '',
            city_type TEXT DEFAULT '',
            city TEXT DEFAULT '',
            street TEXT DEFAULT '',
            street_type TEXT DEFAULT '',
            hous TEXT DEFAULT '',
            post_index TEXT DEFAULT '',
            partner TEXT DEFAULT '',
            status TEXT DEFAULT '',
            register TEXT DEFAULT '',
            edrpou TEXT DEFAULT '',
            address TEXT DEFAULT '',
            partner_name TEXT DEFAULT '',
            id_terminal TEXT DEFAULT '',
            koatu TEXT DEFAULT '',
            tax_id TEXT DEFAULT '',
            koatu2 TEXT DEFAULT ''
            )""")
    
print('ok')
