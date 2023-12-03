import csv

import pandas as pd
from datetime import datetime
def coluna_valor(valor, operador, alvo):
    try:
        if operador == '==':
            return valor == alvo
        elif operador == '!=':
            return valor != alvo
        elif operador == '<':
            return valor < alvo
        elif operador == '>':
            return valor > alvo
        elif operador == '<=':
            return valor <= alvo
        elif operador == '>=':
            return valor >= alvo
        else:
            return False
    except:
        return False

def deletar_dados(end, condicoes):
    # endereço
    arquivo_csv = end

    # Lista para armazenar linhas a serem mantidas
    linhas_mantidas = []

    with open(arquivo_csv, mode='r', newline='') as file:
        reader = csv.DictReader(file)

        # Adiciona cabeçalho ao início da lista
        linhas_mantidas.append(reader.fieldnames)

        # Itera sobre as linhas e mantém apenas aquelas que atendem a todas as condições
        for linha in reader:
            atende_todas_condicoes = all(
                coluna_valor(linha[col], operador, valor) for col, operador, valor in condicoes
            )
            if not atende_todas_condicoes:
                linhas_mantidas.append(linha)

    # Escreve as linhas mantidas de volta ao arquivo CSV
    with open(arquivo_csv, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=linhas_mantidas[0])
        writer.writeheader()
        writer.writerows(linhas_mantidas[1:])
    print(f'Dados excluídos com base nas condições: {condicoes}')


# # # Exemplo de uso delete
# end = r"E:\Nova pasta\Faculdade\BancoDeDados\trab\dados_salvos\employees\dept_emp.csv"
# tabela = "dept_emp"
# condicoes = {"dept_no": ("==", 'd001')}
# deletar_dados(end, condicoes)



def inserir_dados(end, novos_dados):    # Endereço do arquivo
    # Verifica se o arquivo já existe
    arquivo_existe = False
    try:
        with open(end, 'r'):
            arquivo_existe = True
    except FileNotFoundError:
        pass

    # Adiciona os novos dados ao arquivo CSV
    with open(end, mode='a', newline='') as file:
        if isinstance(novos_dados, dict):
            writer = csv.DictWriter(file, fieldnames=novos_dados.keys())
            writer.writerow(novos_dados)
        elif isinstance(novos_dados, list):
            writer = csv.writer(file)
            writer.writerow(novos_dados)

    # Imprime o resultado
    print(f'Dados inseridos com sucesso: {novos_dados}')

# def inserir_dados(end, colunas=None, novos_dados): #versão dicionario
#     # Endereço do arquivo
#     arquivo_csv = end

#     # Verifica se o arquivo já existe
#     arquivo_existe = False
#     try:
#         with open(arquivo_csv, 'r') as file:
#             leitor_csv = csv.reader(file)
#             # Lê a primeira linha para obter as colunas
#             colunas = next(leitor_csv)
#             arquivo_existe = True
#     except FileNotFoundError:
#         pass

#     # Adiciona os novos dados ao arquivo CSV
#     with open(arquivo_csv, mode='a', newline='') as file:
#         if not arquivo_existe:
#             # Se o arquivo não existia, escreve as colunas na primeira linha
#             writer = csv.writer(file)
#             writer.writerow(novos_dados.keys())

#         if isinstance(novos_dados, dict):
#             writer = csv.DictWriter(file, fieldnames=colunas)
#             writer.writerow({col: novos_dados[col] for col in colunas})
#         elif isinstance(novos_dados, list):
#             writer = csv.writer(file)
#             writer.writerow([novos_dados[col] for col in colunas])

#     print(f'Dados inseridos com sucesso: {novos_dados}')

# Exemplo de uso
# end = r"E:\Nova pasta\Faculdade\BancoDeDados\trab\dados_salvos\employees\dept_emp.csv"

# # novos_dados = {'emp_no': '10005', 'dept_no': 'd005', 'from_date':'1986-06-26','to_date':'9999-01-01'}
# novos_dados = ['10006', 'd005', '1986-06-26', '9999-01-01']
# inserir_dados(end, novos_dados)

# # Exemplo de uso
# end = r"E:\Nova pasta\Faculdade\BancoDeDados\trab\dados_salvos\employees\dept_emp.csv"
# dados = ['100001', 'd006', '2023-01-01', '2023-12-31']
# inserir_dados(end, dados)


def atualizar_dados(end, condicoes, novos_dados):
    print(end, condicoes, novos_dados)
    # Endereço do arquivo
    arquivo_csv = end

    # Lista para armazenar linhas atualizadas
    linhas_atualizadas = []

    with open(arquivo_csv, mode='r', newline='') as file:
        reader = csv.DictReader(file)

        # Adiciona cabeçalho ao início da lista
        linhas_atualizadas.append(reader.fieldnames)

        # Itera sobre as linhas e atualiza aquelas que atendem a todas as condições
        for linha in reader:
            atende_todas_condicoes = all(
                coluna_valor(linha[col], operador, valor) for col, operador, valor in condicoes
            )
            if atende_todas_condicoes:
                # Atualiza a linha com os novos dados
                linha[novos_dados[0]] = novos_dados[2]
            linhas_atualizadas.append(linha)

    # Escreve as linhas atualizadas de volta ao arquivo CSV
    with open(arquivo_csv, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=linhas_atualizadas[0])
        writer.writeheader()
        writer.writerows(linhas_atualizadas[1:])

    # Imprime o resultado
    print(f'Dados atualizados com base nas condições: {condicoes}')

# Função auxiliar para avaliar as condições
def coluna_valor(valor, operador, alvo):
    try:
        # if isinstance(alvo, str) and '-' in valor:
        #     valor = datetime.strptime(valor, '%Y-%m-%d').date()

        if operador == '==':
            return valor == alvo
        elif operador == '!=':
            return valor != alvo
        elif operador == '<':
            return valor < alvo
        elif operador == '>':
            return valor > alvo
        elif operador == '<=':
            return valor <= alvo
        elif operador == '>=':
            return valor >= alvo
        else:
            return False
    except:
        return False

# # Exemplo de uso
# condicoes = {'emp_no': ('==', '10001')}
# novos_dados = {'dept_no': '01'}
# end = r"E:\Nova pasta\Faculdade\BancoDeDados\trab\dados_salvos\employees\dept_emp.csv"
# atualizar_dados(end, condicoes, novos_dados)



def selecionar_dados(end, or_condition, condicoes=None, colunas=None):
    # Endereço do arquivo
    arquivo_csv = end

    # Lista para armazenar linhas selecionadas
    linhas_selecionadas = []

    with open(arquivo_csv, mode='r', newline='') as file:
        reader = csv.DictReader(file)

        # Adiciona cabeçalho ao início da lista
        if colunas is None:
            linhas_selecionadas.append(reader.fieldnames)
        else:
            linhas_selecionadas.append(colunas)

        # Itera sobre as linhas e seleciona aquelas que atendem às condições
        if not or_condition:
            for linha in reader:
                atende_todas_condicoes = condicoes is None or all(
                    coluna_valor(linha[col], operador, valor) for col, operador, valor in condicoes
                )
                if atende_todas_condicoes:
                    if colunas is None:
                        linhas_selecionadas.append(linha)
                    else:
                        linha_selecionada = {col: linha[col] for col in colunas}
                        linhas_selecionadas.append(linha_selecionada)
        else:
            for linha in reader:
                atende_pelo_menos_uma_condicao = condicoes is None or any(
                    coluna_valor(linha[col], operador, valor) for col, operador, valor in condicoes
                )
                if atende_pelo_menos_uma_condicao:
                    if colunas is None:
                        linhas_selecionadas.append(linha)
                    else:
                        linha_selecionada = {col: linha[col] for col in colunas}
                        linhas_selecionadas.append(linha_selecionada)

    # Imprime o resultado
    print(f'Dados selecionados com base nas condições: {condicoes}')
    for linha_selecionada in linhas_selecionadas[1:]:
        print(linha_selecionada)

# Função auxiliar para avaliar as condições
def coluna_valor(valor, operador, alvo):
    try:
        # if isinstance(alvo, str) and '-' in valor:
        #     valor = datetime.strptime(valor, '%Y-%m-%d').date()

        if operador == '==':
            return valor == alvo
        elif operador == '!=':
            return valor != alvo
        elif operador == '<':
            return valor < alvo
        elif operador == '>':
            return valor > alvo
        elif operador == '<=':
            return valor <= alvo
        elif operador == '>=':
            return valor >= alvo
        else:
            return False
    except:
        return False



# end = r"E:\Nova pasta\Faculdade\BancoDeDados\trab\dados_salvos\employees\dept_emp.csv"

# # Exemplo de uso sem condições específicas
# # selecionar_dados(end)

# # Exemplo de uso com condições e colunas específicas
# condicoes = {'to_date':('==', "9999-01-01"), 'emp_no':('==', "55") }
# # colunas_selecionadas = ['emp_no', 'from_date']
# selecionar_dados(end, condicoes)


def order_by(tabela, parametro, reverse = False):
    if not tabela or parametro not in tabela[0]:
        print("errado")
        return
    tabela_organizada = sorted(tabela, key=lambda x: x[parametro], reverse = reverse)
    return tabela_organizada
    
def add_columns(tabela, new_columns_list):
    if len(tabela) == len(new_columns_list):
        for i in range(len(tabela)):
            tabela[i].extend(new_columns_list[i])


def innerJoin(table_1, table_2, p_1, p_2):
    # Check if the common column exists in both tables
    if p_1 not in table_1[0] or p_2 not in table_2[0]:
        return False
    
    common_index_1 = table_1[0].index(p_1)
    common_index_2 = table_2[0].index(p_2)
    
    tam_1 = len(table_1)
    tam_2 = len(table_2)
    
    #caso o tamanho da tabela 1 seja maior q o da tabela 2, os valores da tabela 2 são copiados para a tabela 1
    if tam_1 > tam_2:
        new_values = []
        new_values.append(table_2[0])
        for i in range(1,tam_1):
            for j in range(1,tam_2):
                if table_1[i][common_index_1] == table_2[j][common_index_2]:
                    #print("primeiro: " + table_1[i][common_index_1],"segundo: " +table_2[j][common_index_2])
                    #print( "table_1[i][common_index_1]: " + str(table_1[i][common_index_1]) + " table_2[j]" + str(table_2[j]))
                    new_values.append(table_2[j])
                    break
        add_columns(table_1, new_values)
        print(table_1)
        #write_to_csv('./dados_salvos/universidade/teste_inner_join.csv', table_1)

    else: #caso contrário, o oposto é feito
        new_values = []
        new_values.append(table_1[0])
        for i in range(1, tam_2):
            for j in range(1, tam_1):
                if table_1[j][common_index_1] == table_2[i][common_index_2]:
                    #print("primeiro: " + table_1[j][common_index_1],"segundo: " +table_2[i][common_index_2])
                    
                    new_values.append(table_1[j])
                    break
        add_columns(table_2, new_values)
        
        #write_to_csv('./dados_salvos/universidade/teste_inner_join_2.csv', table_2)

