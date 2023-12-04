import csv
import os
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
    try:
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
        retorno = f'Dados excluídos com base nas condições: {condicoes}'
    except:
        retorno = f'Houve um erro!, condição incorreta!'
    finally:
        return retorno

def deletar_dados(end, condicoes):
    # endereço
    try:
        arquivo_csv = end

        # Lista para armazenar linhas a serem mantidas
        linhas_mantidas = []
        allTrue = True
        if len(condicoes) > 1:
            if condicoes[1] == ['ou']:
                allTrue = True
                print("all true")
            else:
                allTrue = False
                print("all false")
        cond = []
        cond.append(condicoes[0])
        if len(condicoes) == 3:
            cond.append(condicoes[2])

        with open(arquivo_csv, mode='r', newline='') as file:
            reader = csv.DictReader(file)

            # Adiciona cabeçalho ao início da lista
            linhas_mantidas.append(reader.fieldnames)

            # Itera sobre as linhas e mantém apenas aquelas que atendem a todas as condições
            for linha in reader:
                if not allTrue:
                    atende_todas_condicoes = all(
                        coluna_valor(linha[col], operador, valor) for col, operador, valor in cond
                    )
                    if not atende_todas_condicoes:
                        linhas_mantidas.append(linha)
                else:
                    atende_uma_das_condicoes = any(
                        coluna_valor(linha[col], operador, valor) for col, operador, valor in cond
                    )
                    if not atende_uma_das_condicoes:
                        linhas_mantidas.append(linha)

        # Escreve as linhas mantidas de volta ao arquivo CSV
        with open(arquivo_csv, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=linhas_mantidas[0])
            writer.writeheader()
            writer.writerows(linhas_mantidas[1:])
        retorno = f'Dados excluídos com base nas condições: {condicoes}'
    except:
        retorno = f'Houve um erro!, condição incorreta!'
    finally:
        return retorno

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
    try:
        # Endereço do arquivo
        arquivo_csv = end

        # Lista para armazenar linhas atualizadas
        linhas_atualizadas = [] 

        if condicoes[1] == ['ou']:
            allTrue = True
            print("all true")
        else:
            allTrue = False
            print("all false")
        cond = []
        cond.append(condicoes[0])
        if len(condicoes) == 3:
            cond.append(condicoes[2])
        with open(arquivo_csv, mode='r', newline='') as file:
            reader = csv.DictReader(file)

            # Adiciona cabeçalho ao início da lista
            linhas_atualizadas.append(reader.fieldnames)

            # Itera sobre as linhas e atualiza aquelas que atendem a todas as condições
            for linha in reader:
                if not allTrue:
                    atende_todas_condicoes = all(
                        coluna_valor(linha[col], operador, valor) for col, operador, valor in cond
                    )
                    if atende_todas_condicoes:
                        # Atualiza a linha com os novos dados
                        linha[novos_dados[0]] = novos_dados[2]
                else:
                    atende_uma_das_condicoes = any(
                        coluna_valor(linha[col], operador, valor) for col, operador, valor in cond
                    )
                    if atende_uma_das_condicoes:
                        # Atualiza a linha com os novos dados
                        linha[novos_dados[0]] = novos_dados[2]
                linhas_atualizadas.append(linha)

        # Escreve as linhas atualizadas de volta ao arquivo CSV
        with open(arquivo_csv, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=linhas_atualizadas[0])
            writer.writeheader()
            writer.writerows(linhas_atualizadas[1:])
        retorno = f'Dados atualizados com base nas condições: {condicoes}'
    except:
        retorno = f'Ocorreu um erro na condição!'
    finally:
        return retorno
        # Imprime o resultado
        #print(f'Dados atualizados com base nas condições: {cond}')


# def atualizar_dados(end, condicoes, novos_dados):
#     try:
#         # Endereço do arquivo
#         arquivo_csv = end

#         # Lista para armazenar linhas atualizadas
#         linhas_atualizadas = []

#         with open(arquivo_csv, mode='r', newline='') as file:
#             reader = csv.DictReader(file)

#             # Adiciona cabeçalho ao início da lista
#             linhas_atualizadas.append(reader.fieldnames)

#             # Itera sobre as linhas e atualiza aquelas que atendem a todas as condições
#             for linha in reader:
#                 atende_todas_condicoes = all(
#                     coluna_valor(linha[col], operador, valor) for col, operador, valor in condicoes
#                 )
#                 if atende_todas_condicoes:
#                     # Atualiza a linha com os novos dados
#                     linha[novos_dados[0]] = novos_dados[2]
#                 linhas_atualizadas.append(linha)

#         # Escreve as linhas atualizadas de volta ao arquivo CSV
#         with open(arquivo_csv, mode='w', newline='') as file:
#             writer = csv.DictWriter(file, fieldnames=linhas_atualizadas[0])
#             writer.writeheader()
#             writer.writerows(linhas_atualizadas[1:])
#         retorno = f'Dados atualizados com base nas condições: {condicoes}'
#     except:
#         retorno = f'Ocorreu um erro na condição!'
#     finally:
#         return retorno

# # Exemplo de uso
# condicoes = {'emp_no': ('==', '10001')}
# novos_dados = {'dept_no': '01'}
# end = r"E:\Nova pasta\Faculdade\BancoDeDados\trab\dados_salvos\employees\dept_emp.csv"
# atualizar_dados(end, condicoes, novos_dados)


def selecionar_dados(end, or_condition, condicoes=None, colunas=None, inner = None, order = None):
    try:
        
        # Endereço do arquivo
        arquivo_csv = end

        # Lista para armazenar linhas selecionadas
        linhas_selecionadas = []
        # print(arquivo_csv)
        with open(arquivo_csv, mode='r', newline='') as file:
            reader = csv.DictReader(file)

            # Adiciona cabeçalho ao início da lista
            #if coluna == '*'
            if inner:
                caminho_parts = os.path.split(end)
                # Obtém todas as partes exceto a última
                end_table = os.path.join(*caminho_parts[:-1])
                end_table += "/" + inner[0] + ".csv" 
                print(innerjoip(end, end_table, inner[1], inner[3]))
                linhas_selecionadas = innerjoip(end, end_table, inner[1], inner[3])
    
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
        retorno = []
        for linha_selecionada in linhas_selecionadas[1:]:
             retorno.append(linha_selecionada)
       
        if order:
            if order[1].lower() == 'asc':
                print("############", order[0])
                lista_ordenada = sorted(retorno, key=lambda x: x[order[0]], reverse=True)         
            elif order[1].lower() == 'desc':
                lista_ordenada = sorted(retorno, key=lambda x: x[order[0]])
            retorno = lista_ordenada
    except:
        retorno = "Ocorreu um erro!"
    finally:
        # print(f"RETORNO::::{retorno}")
        return retorno
    # for linha_selecionada in linhas_selecionadas[1:]:
    #     print(linha_selecionada)




# end = r"E:\Nova pasta\Faculdade\BancoDeDados\trab\dados_salvos\employees\dept_emp.csv"

# # Exemplo de uso sem condições específicas
# # selecionar_dados(end)

# # Exemplo de uso com condições e colunas específicas
# condicoes = {'to_date':('==', "9999-01-01"), 'emp_no':('==', "55") }
# # colunas_selecionadas = ['emp_no', 'from_date']
# selecionar_dados(end, condicoes)


    
def add_columns(tabela, new_columns_list):
    if len(tabela) == len(new_columns_list):
        for i in range(len(tabela)):
            tabela[i].extend(new_columns_list[i])


def innerJoin(table_1, table_2, p_1, p_2):
    # Check if the common column exists in both tables



    if p_1 not in table_1[0] or p_2 not in table_2[0]:
        return False
    
    common_index_1 = p_1
    common_index_2 = p_2

    
    tam_1 = len(table_1)
    tam_2 = len(table_2)
    
    #caso o tamanho da tabela 1 seja maior q o da tabela 2, os valores da tabela 2 são copiados para a tabela 1
    if tam_1 > tam_2:
        new_values = []
        new_values.append(table_2[0].keys())
        print('table2',table_2[0].keys())
        for i in range(1,tam_1):
            for j in range(1,tam_2):
                if table_1[i][common_index_1] == table_2[j][common_index_2]:
                    #print("primeiro: " + table_1[i][common_index_1],"segundo: " +table_2[j][common_index_2])
                    #print( "table_1[i][common_index_1]: " + str(table_1[i][common_index_1]) + " table_2[j]" + str(table_2[j]))
                    new_values.append(table_2[j])
                    break
        add_columns(table_1, new_values)
        # print(table_1)
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
    print("AAAAAAAAAAAAAAAAA")
    print('TABLE 1: ', table_1)

    print('TABLE 2: ', table_2)

    print('NEW VALUE: ', new_values)
        #write_to_csv('./dados_salvos/universidade/teste_inner_join_2.csv', table_2)

def innerjoip(tabela1, tabela2, chave_primaria_tabela1, chave_primaria_tabela2):
    # Lê os dados das tabelas CSV
    with open(tabela1, 'r') as arquivo1, open(tabela2, 'r') as arquivo2:
        leitor1 = csv.DictReader(arquivo1)
        leitor2 = csv.DictReader(arquivo2)

        # Cria índice para a tabela2 usando a chave primária
        indice_tabela2 = {linha[chave_primaria_tabela2]: linha for linha in leitor2}

        # Realiza o INNER JOIN
        resultado = []
        for linha_tabela1 in leitor1:
            chave = linha_tabela1[chave_primaria_tabela1]
            if chave in indice_tabela2:
                linha_tabela2 = indice_tabela2[chave]
                linha_resultado = {**linha_tabela1, **linha_tabela2}
                resultado.append(linha_resultado)

    return resultado

