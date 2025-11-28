import mysql.connector as mysql

DB_CONFIG = {
    'host': 'localhost',
    'user': 'root', 
    'password': 'root', 
    'database': 'pagamento_finpulse'
}

def get_db_connection():
    return mysql.connect(**DB_CONFIG)

class usuarios_repository:

    def __init__ (self):
        self.db = get_db_connection()

    def get_usuarios(self):
        query = "SELECT * from usuarios"
        cursor = self.db.cursor(dictionary=True)
        cursor.execute(query)
        resultados = cursor.fetchall()
        cursor.close()
        return resultados



    def get_usuario(self, id_usuario):

        query = "SELECT * from usuarios WHERE id_usuario = %s"
        cursor = self.db.cursor(dictionary=True)
        cursor.execute(query, (id_usuario,))
        resultado = cursor.fetchall()
        cursor.close()
        return (resultado[0])
    

    def criar_usuario(self, id_usuario, nome, email, senha_hash, data_cadastro):

        query = """
        INSERT INTO usuarios(id_usuario, nome, email, data_cadastro, senha_hash)
        VALUES(%s, %s, %s, %s, %s)
        """
        cursor = self.db.cursor()
        cursor.execute(query,(id_usuario, nome, email, data_cadastro, senha_hash))
        self.db.commit()
        cursor.close()


    def atualizar_nome(self, id_usuario, nome):

        query = """
            UPDATE usuarios,
            SET nome = %s,
            WHERE id_usuario = %s
            """
        
        nomes = (nome, id_usuario)


        self.cursor.execute(query, nomes)
        self.con.commit()
        return self.cursor.rowcount


    def atualizar_email(self, id_usuario, email):

        query = """
            UPDATE usuarios,
            SET email = %s,
            WHERE id_usuario = %s
            """
        
        emails = (email, id_usuario)


        self.cursor.execute(query, emails)
        self.con.commit()

        return self.cursor.rowcount


    def atualizar_senha(self, id_usuario, senha_hash):

        query = """
            UPDATE usuarios,
            SET senha_hash = %s,
            WHERE id_usuario = %s
            """
        senhas = (senha_hash, id_usuario)


        self.cursor.execute(query, senhas)
        self.con.commit()

        return self.cursor.rowcount

    def deletar_usuario(self, id_usuario):

        query = """
            DELETE FROM usuarios,
            WHERE id_usuario = %s
            """
        
        usuario = (id_usuario)

        self.cursor.execute(query, usuario)
        self.con.commit()

        return self.cursor.rowcount