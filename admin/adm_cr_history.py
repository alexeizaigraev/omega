from modules import *
from papa_sq import db_operator

db_operator("""
            CREATE TABLE IF NOT EXISTS history (
            term TEXT DEFAULT '',
            dep TEXT DEFAULT '',
            serial TEXT DEFAULT '',
            adres TEXT DEFAULT '',
            date_hist TEXT DEFAULT '',
            kind TEXT DEFAULT ''
            )""")

print('ok')
