import mysql.connector
import os
# impor config

def conectar_mysql(bd):
    config = {
        'host': 'localhost',
        'user': 'root',
        'password': 'root',
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
            resultados = cursor.fetchall()
            return resultados if resultados else "Comando executado com sucesso!"

    except mysql.connector.Error as erro:
        print (f"Erro ao executar a consulta: {erro}")
        return 0


    finally:
        if conexao_mysql.is_connected():
            cursor.close()
            conexao_mysql.close()

def fetch_table_data(db, table_name):
    cnc = conectar_mysql(db)

    cursor = cnc.cursor()
    cursor.execute('select * from ' + table_name)

    header = [row[0] for row in cursor.description]

    rows = cursor.fetchall()

    cnc.close()

    return header, rows


def export(db, table_name, path):
    direc = os.getcwd()
    os.chdir(path)
    header, rows = fetch_table_data(db, table_name)

    f = open(table_name + '.csv', 'w')
    
    f.write(','.join(header) + '\n')

    for row in rows:
        f.write(','.join(str(r) for r in row) + '\n')

    f.close()
    os.chdir(direc)
    print(str(len(rows)) + ' rows written successfully to ' + f.name)

import shutil

def save_csv_system(source_path, csv_name, database):
    current_path = os.getcwd()

    file_name = csv_name

    saved_data_directory = os.path.join(current_path, 'dados_salvos')
    os.makedirs(saved_data_directory, exist_ok=True)

    database_directory = os.path.join(saved_data_directory, database)
    os.makedirs(database_directory, exist_ok=True)

    destination_file_path = os.path.join(database_directory, file_name)

    shutil.copy(source_path, destination_file_path)
