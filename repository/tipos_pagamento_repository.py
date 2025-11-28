import mysql.connector as mysql

DB_CONFIG = {
    'host': 'localhost',
    'user': 'root', 
    'password': 'root', 
    'database': 'pagamento_finpulse'
}

def get_db_connection():
    return mysql.connect(**DB_CONFIG)

class tipos_pagamento_repository:

    def __init__ (self):
        self.db = get_db_connection()

    def get_tipos_pagamento():
        query = "SELECT * from tipos_pagamento"
        con = get_db_connection()

        cursor = con.cursor()
        cursor.execute(query)
        resultados = cursor.fetchall()
        for l in resultados:
            print(l)
        cursor.close()
        con.close()

