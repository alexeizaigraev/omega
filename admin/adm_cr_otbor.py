from modules import *
from papa_sq import db_operator

db_operator("""
            CREATE TABLE IF NOT EXISTS otbor (
            term TEXT PRIMARY KEY DEFAULT '',
            dep TEXT DEFAULT ''
            )""")

print('ok')
