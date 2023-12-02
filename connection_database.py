import mysql.connector
import os
# impor config
def conectar_mysql(bd):
    config = {
        'host': 'localhost',
        'user': 'root',
        'password': '1234',
        'database': bd,
    }
    try:
        conexao = mysql.connector.connect(**config)
        return conexao

    except mysql.connector.Error as erro:
        print(f"Erro ao conectar ao MySQL: {erro}")
        return 0

def executar_consulta(db, query):
    conexao_mysql = conectar_mysql(db)
    try:
        if conexao_mysql.is_connected():
            cursor = conexao_mysql.cursor(dictionary=True)
            cursor.execute(query)
            # conexao_mysql.commit()
            # print(query)
            resultados = cursor.fetchall()
            # print(resultados)
            return resultados if resultados else "Comando executado com sucesso!"

    except mysql.connector.Error as erro:
        print (f"Erro ao executar a consulta: {erro}")
        return 0


    finally:
        if conexao_mysql.is_connected():
            cursor.close()
            conexao_mysql.close()

def fetch_table_data(db, table_name):
    # The connect() constructor creates a connection to the MySQL server and returns a MySQLConnection object.
    cnc = conectar_mysql(db)

    cursor = cnc.cursor()
    cursor.execute('select * from ' + table_name)

    header = [row[0] for row in cursor.description]

    rows = cursor.fetchall()

    # Closing connection
    cnc.close()

    return header, rows


def export(db, table_name, path):
    direc = os.getcwd()
    os.chdir(path)
    header, rows = fetch_table_data(db, table_name)

    # Create csv file
    f = open(table_name + '.csv', 'w')
    
    # Write header
    f.write(','.join(header) + '\n')

    for row in rows:
        f.write(','.join(str(r) for r in row) + '\n')

    f.close()
    os.chdir(direc)
    print(str(len(rows)) + ' rows written successfully to ' + f.name)

import shutil

def save_csv_system(source_path, csv_name, database):
    current_path = os.getcwd()

    #nome do arquivo csv
    file_name = csv_name

    # Diretório onde os dados serão salvos
    saved_data_directory = os.path.join(current_path, 'dados_salvos')
    os.makedirs(saved_data_directory, exist_ok=True)

    # Diretório onde os dados específicos do banco de dados serão salvos
    database_directory = os.path.join(saved_data_directory, database)
    os.makedirs(database_directory, exist_ok=True)

    # Caminho completo do arquivo de destino
    destination_file_path = os.path.join(database_directory, file_name)

    # Copiar o arquivo de origem para o destino
    shutil.copy(source_path, destination_file_path)
# export("employees", "dept_emp")