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


def deletar_dados(end, condicoes, or_condition):
    try:
        arquivo_csv = end

        linhas_mantidas = []

        with open(arquivo_csv, mode='r', newline='') as file:
            reader = csv.DictReader(file)

            linhas_mantidas.append(reader.fieldnames)

            for linha in reader:
                if not or_condition:
                    atende_todas_condicoes = all(
                        coluna_valor(linha[col], operador, valor) for col, operador, valor in condicoes
                    )
                    if not atende_todas_condicoes:
                        linhas_mantidas.append(linha)
                else:
                    atende_uma_das_condicoes = any(
                        coluna_valor(linha[col], operador, valor) for col, operador, valor in condicoes
                    )
                    if not atende_uma_das_condicoes:
                        linhas_mantidas.append(linha)

        with open(arquivo_csv, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=linhas_mantidas[0])
            writer.writeheader()
            writer.writerows(linhas_mantidas[1:])
        retorno = f'Dados excluídos com base nas condições: {condicoes}'
    except:
        retorno = f'Houve um erro!, condição incorreta!'
    finally:
        return retorno





def inserir_dados(end, novos_dados):    

    with open(end, mode='a', newline='') as file:
        if isinstance(novos_dados, dict):
            writer = csv.DictWriter(file, fieldnames=novos_dados.keys())
            writer.writerow(novos_dados)
        elif isinstance(novos_dados, list):
            writer = csv.writer(file)
            writer.writerow(novos_dados)

    return f'Dados inseridos com sucesso: {novos_dados}'



def atualizar_dados(end, condicoes, or_condition, novos_dados):
    try:
        arquivo_csv = end


        linhas_atualizadas = [] 

        with open(arquivo_csv, mode='r', newline='') as file:
            reader = csv.DictReader(file)

            linhas_atualizadas.append(reader.fieldnames)

            for linha in reader:
                if not or_condition:
                    atende_todas_condicoes = all(
                        coluna_valor(linha[col], operador, valor) for col, operador, valor in condicoes
                    )
                    if atende_todas_condicoes:
                        linha[novos_dados[0]] = novos_dados[2]
                else:
                    atende_uma_das_condicoes = any(
                        coluna_valor(linha[col], operador, valor) for col, operador, valor in condicoes
                    )
                    if atende_uma_das_condicoes:
                        linha[novos_dados[0]] = novos_dados[2]
                linhas_atualizadas.append(linha)

        with open(arquivo_csv, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=linhas_atualizadas[0])
            writer.writeheader()
            writer.writerows(linhas_atualizadas[1:])
        retorno = f'Dados atualizados com base nas condições: {condicoes}'
    except:
        retorno = f'Ocorreu um erro na condição!'
    finally:
        return retorno





def selecionar_dados(end, colunas=None,  condicoes=None, or_condition=None, inner = None, order = None):
    try:
        
        arquivo_csv = end

        linhas_selecionadas = []
        with open(arquivo_csv, mode='r', newline='') as file:
            reader = csv.DictReader(file)


            if inner:
                caminho_parts = os.path.split(end)

                end_table = os.path.join(*caminho_parts[:-1])
                end_table += "/" + inner[0] + ".csv" 
                reader = innerjoin(end, end_table, inner[1], inner[3])



            if condicoes == None:
                for linha in reader:
                    if colunas == None:
                        linhas_selecionadas.append(linha)
                    else:
                        linha_selecionada = {col: linha[col] for col in colunas}
                        linhas_selecionadas.append(linha_selecionada)
            else:
                if not or_condition:
                    for linha in reader:
                        atende_todas_condicoes = condicoes is None or all(
                            coluna_valor(linha[col], operador, valor) for col, operador, valor in condicoes
                        )
                        if atende_todas_condicoes:
                            if colunas == None:
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
                            if colunas == None:
                                linhas_selecionadas.append(linha)
                            else:
                                linha_selecionada = {col: linha[col] for col in colunas}
                                linhas_selecionadas.append(linha_selecionada)
        print(f'Dados selecionados com base nas condições: {condicoes}')
        retorno = []
        for linha_selecionada in linhas_selecionadas:
             retorno.append(linha_selecionada)
       
        if order:
            try:
                if order[1].lower() == 'asc':
                    lista_ordenada = sorted(retorno, key=lambda x: int(x[order[0]]))
                elif order[1].lower() == 'desc':
                    lista_ordenada = sorted(retorno, key=lambda x: int(x[order[0]]), reverse=True)
            except Exception as e:
                print(e)
                if order[1].lower() == 'asc':
                    lista_ordenada = sorted(retorno, key=lambda x: x[order[0]])
                elif order[1].lower() == 'desc':
                    lista_ordenada = sorted(retorno, key=lambda x: x[order[0]], reverse=True)
            retorno = lista_ordenada
    except Exception as e:
        retorno = "Ocorreu um erro!", e
    finally:
        return retorno




def innerjoin(tabela1, tabela2, chave_primaria_tabela1, chave_primaria_tabela2):
    with open(tabela1, 'r') as arquivo1, open(tabela2, 'r') as arquivo2:
        leitor1 = csv.DictReader(arquivo1)
        leitor2 = csv.DictReader(arquivo2)

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

