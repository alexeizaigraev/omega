from modules import *
from papa_pg import dbexec

dbexec("""
            CREATE TABLE IF NOT EXISTS otbor (
            term TEXT PRIMARY KEY DEFAULT '',
            dep TEXT DEFAULT ''
            )""")

print('ok')
