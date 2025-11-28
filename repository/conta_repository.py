import mysql.connector as mysql

DB_CONFIG = {
    'host': 'localhost',
    'user': 'root', 
    'password': 'root', 
    'database': 'pagamento_finpulse'
}

def get_db_connection():
    return mysql.connect(**DB_CONFIG)

class conta_repository:

    def __init__ (self):

        self.db = get_db_connection()

    def get_saldos(self):
        query = """SELECT saldo from conta"""
        cursor = self.db.cursor(dictionary=True)
        cursor.execute(query)
        resultados = cursor.fetchall()
        cursor.close()
        return resultados
    
    def get_saldo(self, id_usuario, id_conta):

        query = """SELECT saldo from conta WHERE id_usuario = %s AND id_conta = %s"""
        cursor = self.db.cursor()
        cursor.execute(query, (id_usuario, id_conta))
        resultado = cursor.fetchone()
        cursor.close()
        if resultado:
            return resultado[0]
        return 0.0
    
    def criar_conta(self, id_conta, id_usuario, saldo):

        query = """
        INSERT INTO conta(id_usuario, id_conta, saldo)
        VALUES(%s, %s, %s)
        """

        cursor = self.db.cursor()
        cursor.execute(query,(id_usuario, id_conta, saldo))
        self.db.commit()
        cursor.close()
    

    def atualizar_saldo(self, id_usuario, id_conta, saldo):

        query = """
            UPDATE conta
            SET saldo = %s
            WHERE id_usuario = %s AND id_conta = %s
            """
        
        valores = (saldo, id_usuario, id_conta)
        cursor = self.db.cursor()
        cursor.execute(query, valores) 
        self.db.commit() 
        rows = cursor.rowcount
        cursor.close()
        return rows
    
    def deletar_conta(self, id_usuario, id_conta):

        query = """
            DELETE FROM conta
            WHERE id_usuario = %s AND id_conta = %s
            """
        
        valores = (id_usuario, id_conta)

        cursor = self.db.cursor()
        cursor.execute(query, valores)
        self.db.commit()
        rows = cursor.rowcount
        cursor.close()
        return rows