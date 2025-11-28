import mysql.connector as mysql

DB_CONFIG = {
    'host': 'localhost',
    'user': 'root', 
    'password': 'root', 
    'database': 'pagamento_finpulse'
}

def get_db_connection():
    return mysql.connect(**DB_CONFIG)

class transacoes_repository:

    def __init__ (self):
        self.db = get_db_connection()

    def get_transacoes(self):
        query = """SELECT * FROM transacoes"""
        cursor = self.db.cursor(dictionary=True)
        cursor.execute(query)
        resultados = cursor.fetchall()
        cursor.close()
        return resultados

    def get_transacao(self, id_transacao):
        query = """SELECT * FROM transacoes WHERE id_transacao = %s"""
        cursor = self.db.cursor()
        cursor.execute(query, (id_transacao))
        resultado = cursor.fetchone()
        cursor.close()
        return (resultado[0])
    
    def get_historico(self, id_conta):
        query = """SELECT * FROM transacoes WHERE id_conta_remetente = %s OR id_conta_destinatario = %s ORDER by data_transacao DESC"""
        cursor = self.db.cursor()
        cursor.execute(query, (id_conta, id_conta))
        resultados = cursor.fetchall()
        cursor.close()
        return resultados


    def criar_transacao(self, id_transacao, id_usuario, id_tipo, valor, status, data_transacao, id_conta_remetente, id_conta_destinatario):

        query = """
        INSERT INTO transacoes(id_transacao, id_usuario, id_tipo, valor, status, data_transacao, id_conta_remetente, id_conta_destinatario)
        VALUES(%s, %s, %s, %s, %s, %s, %s, %s)
        """
        cursor = self.db.cursor()
        try:
            cursor.execute(query,(id_transacao, id_usuario, id_tipo, valor, status, data_transacao, id_conta_remetente, id_conta_destinatario))
            self.db.commit()
        except mysql.Error as err:
            print(f"Erro no banco: {err}")
            raise err
        finally:
            cursor.close()