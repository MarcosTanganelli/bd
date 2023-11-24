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
            cursor = conexao_mysql.cursor(dictionary=True)
            cursor.execute(query)
            conexao_mysql.commit()
            resultados = cursor.fetchall()
            print(resultados)
            return resultados if resultados else "Comando executado com sucesso!"

    except mysql.connector.Error as erro:
        return f"Erro ao executar a consulta: {erro}"

    finally:
        if conexao_mysql.is_connected():
            cursor.close()
            conexao_mysql.close()
