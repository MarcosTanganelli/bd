import execute_cmd as ec


def parse_query(bd, query):
    semantica = query.split()
    query_type = semantica[0].lower()
    if query_type in ["selecione", "insira", "atualize", "exclua"]:
        return parse_manager(bd, semantica)
    else:
        raise ValueError("Comando não suportado")
    
def parse_manager(bd, semantica):
    if semantica[0].lower() == "selecione":
        return parse_select(bd, semantica)
    elif semantica[0].lower() == "insira":
        return parse_insert(bd, semantica)
    elif semantica[0].lower() == "atualize":
        return parse_update(bd, semantica)
    elif semantica[0].lower() == "exclua":
        return parse_delete(bd, semantica)
    
def parse_select(bd, semantica):
    if "da" not in semantica:
        raise ValueError("Comando SELECT incompleto")
    
    select_index = semantica.index("selecione")
    from_index = semantica.index("da")

    columns_start_index = select_index + 1
    columns_end_index = from_index

    order_by_index = semantica.index("ordene") if "ordene" in semantica else None
    inner_join_index = semantica.index("junte") if "junte" in semantica else None
    where_index = semantica.index("onde") if "onde" in semantica else None

    condition = semantica[where_index + 1:order_by_index] if where_index is not None else None
    columns = semantica[columns_start_index:columns_end_index]
    table = semantica[from_index + 1]
    order_by_columns = semantica[order_by_index + 2:] if order_by_index is not None else None
    todas_condicoes = []
    operadores_logicos = ["e", "ou"]
    condicao_atual = []

    for token in condition:
        if token.lower() in operadores_logicos:
            todas_condicoes.append(condicao_atual)
            condicao_atual = [token]
        else:
            condicao_atual.append(token)

    if condicao_atual:
        todas_condicoes.append(condicao_atual)
    # join_table = None
    # if inner_join_index is not None:
    #     join_table_index = semantica.index("com")
    #     join_table = semantica[join_table_index+1 :where_index]
    #     join_table.remove("em")
    print(todas_condicoes)
    end = "./dados_salvos/" + bd + "/" + table + ".csv"  
    ec.selecionar_dados(end, columns, todas_condicoes)
    # cmd = {'func':'SELECT', 'tabela':table, 'colunas': columns,'condition':condition,
    #         'inner join':join_table,  'order by':order_by_columns }

# bd = "employees"
# query_select = "selecione emp_no, dept_no da dept_emp onde emp_no == 10001"
# parse_query(bd, query_select)
          
def parse_insert(bd, semantica):
    print(semantica)
    if "em" not in semantica or "valores" not in semantica:
        raise ValueError("Comando INSERT incompleto")
    
    columns = None
    into_index = semantica.index("em")
    table = semantica[into_index + 1]

    values_start_index = semantica.index("valores") + 1
    columns_start_index = semantica.index("em") + 2
    
    columns = semantica[columns_start_index:values_start_index - 1]
    values = semantica[values_start_index:]

    values = values[0].replace('(', '').replace(')', '').split(',')
    values = [value.strip("'") for value in values]

    print(values)
    if columns :
        columns = columns[0].replace('(', '').replace(')', '').split(',')
        values = dict(zip(columns, values))

    print(values)        
    PATH = "./dados_salvos/" + bd + "/" + table + ".csv"  
    ec.inserir_dados(PATH,  values)

bd = "employees"
query_insert = "Insira em dept_emp (emp_no,dept_no,from_date,to_date) valores (999,'1','1986-06-26','9999-01-01')"
parse_query(bd, query_insert)


def parse_update(bd, semantica):
    if "atualize" not in semantica or "defina" not in semantica or "onde" not in semantica:
        raise ValueError("Comando UPDATE incompleto")
    
    table = semantica[semantica.index("atualize") + 1]
    set_index = semantica.index("defina") + 1
    where_index = semantica.index("onde")

    set_clause = semantica[set_index:where_index]
    condition = semantica[where_index + 1:]
    print(set_clause)
    PATH = "./dados_salvos/" + bd + "/" + table + ".csv"  
    todas_condicoes = []

    # Identificar operadores lógicos "e" e "ou"
    operadores_logicos = ["e", "ou"]
    condicao_atual = []

    for token in condition:
        if token.lower() in operadores_logicos:
            todas_condicoes.append(condicao_atual)
            condicao_atual = [token]
        else:
            condicao_atual.append(token)

    if condicao_atual:
        todas_condicoes.append(condicao_atual)
    # print(todas_condicoes)
    ec.atualizar_dados(PATH, todas_condicoes, set_clause)
    # return cmd

# bd = "employees"
# query_update = "atualize dept_emp defina emp_no = 7000 onde emp_no == 10001"
# parse_query(bd, query_update)

def parse_delete(bd, semantica):
    if "de" not in semantica or "onde" not in semantica:
        raise ValueError("Comando DELETE incompleto")
    
    from_index = semantica.index("de")
    table = semantica[from_index + 1]
    where_index = semantica.index("onde") if "onde" in semantica else None
    condition = semantica[where_index + 1:] if where_index is not None else None
    todas_condicoes = []

    # Identificar operadores lógicos "e" e "ou"
    operadores_logicos = ["e", "ou"]
    condicao_atual = []

    for token in condition:
        if token.lower() in operadores_logicos:
            todas_condicoes.append(condicao_atual)
            condicao_atual = [token]
        else:
            condicao_atual.append(token)

    if condicao_atual:
        todas_condicoes.append(condicao_atual)

    # print(condition)
    # print(todas_condicoes)

    PATH = "./dados_salvos/" + bd + "/" + table + ".csv"  
    ec.deletar_dados(PATH, todas_condicoes)

# bd = "employees"
# query_delete = "exclua de dept_emp onde emp_no == 10001"
# parse_query(bd, query_delete)