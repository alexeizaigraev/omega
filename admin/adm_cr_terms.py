from modules import *
from papa_sq import db_operator 

db_operator("""
            CREATE TABLE IF NOT EXISTS terminals (
            department TEXT DEFAULT '',
            termial TEXT PRIMARY KEY DEFAULT '',
            model TEXT DEFAULT '',
            serial_number TEXT DEFAULT '',
            date_manufacture TEXT DEFAULT '',
            soft TEXT DEFAULT '',
            producer TEXT DEFAULT '',
            rne_rro TEXT DEFAULT '',
            sealing TEXT DEFAULT '',
            fiscal_number TEXT DEFAULT '',
            oro_serial TEXT DEFAULT '',
            oro_number TEXT DEFAULT '',
            ticket_serial TEXT DEFAULT '',
            ticket_1sheet TEXT DEFAULT '',
            ticket_number TEXT DEFAULT '',
            sending TEXT DEFAULT '',
            books_arhiv TEXT DEFAULT '',
            tickets_arhiv TEXT DEFAULT '',
            to_rro TEXT DEFAULT '',
            owner_rro TEXT DEFAULT '',
            register TEXT DEFAULT '',
            finish TEXT DEFAULT ''
            )""")

print('ok')
