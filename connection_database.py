import mysql.connector

def conectar_mysql():
    config = {
        'host': 'localhost',
        'user': 'root',
        'password': 'root',
        'database': 'employees',
    }
    try:
        conexao = mysql.connector.connect(**config)
        return conexao

    except mysql.connector.Error as erro:
        print(f"Erro ao conectar ao MySQL: {erro}")

def executar_consulta(query):
    conexao_mysql = conectar_mysql()
    try:
        if conexao_mysql.is_connected():
            # Cria um cursor para executar a consulta
            cursor = conexao_mysql.cursor(dictionary=True)

            # Executa a consulta
            cursor.execute(query)

            # Obtém os resultados (se houver)
            resultados = cursor.fetchall()

            return resultados

    except mysql.connector.Error as erro:
        print(f"Erro ao executar a consulta: {erro}")

    finally:
        if conexao_mysql.is_connected():
            cursor.close()
            conexao_mysql.close()
