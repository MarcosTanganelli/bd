import mysql.connector
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
            print(query)
            resultados = cursor.fetchall()
            print(resultados)
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


def export(db, table_name):
    header, rows = fetch_table_data(db, table_name)

    # Create csv file
    f = open(table_name + '.csv', 'w')

    # Write header
    f.write(','.join(header) + '\n')

    for row in rows:
        f.write(','.join(str(r) for r in row) + '\n')

    f.close()
    print(str(len(rows)) + ' rows written successfully to ' + f.name)


# export("employees", "dept_emp")