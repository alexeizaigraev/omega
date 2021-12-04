from modules import *
from papa_pg import dbexec

dbexec("""
            CREATE TABLE IF NOT EXISTS logi (
            department TEXT DEFAULT '',
            termial TEXT DEFAULT '',
            serial_number TEXT DEFAULT '',
            address TEXT DEFAULT '',
            datalog TEXT DEFAULT '',
            kind TEXT DEFAULT ''
            )""")

print('ok')
