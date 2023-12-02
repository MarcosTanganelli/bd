import execute_cmd
def parse_query(query):
    semantica = query.lower().split()
    query_type = semantica[0].lower()
    if query_type in ["selecione", "insira", "atualize", "exclua"]:
        return parse_manager(semantica)
    else:
        raise ValueError("Comando não suportado")
    
def parse_manager(semantica):
    if semantica[0] == "selecione":
        return parse_select(semantica)
    elif semantica[0] == "insira":
        return parse_insert(semantica)
    elif semantica[0] == "atualize":
        return parse_update(semantica)
    elif semantica[0] == "exclua":
        return parse_delete(semantica)
    
def parse_select(semantica):
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

    x = f"SELECT {' '.join(columns)} FROM {''.join(table) if(table[1]) else table}"
    join_table = None
    if inner_join_index is not None:
        join_table_index = semantica.index("com")
        join_table = semantica[join_table_index+1 :where_index]
        join_table.remove("em")


    cmd = {'func':'SELECT', 'tabela':table, 'colunas': columns,'condition':condition,
            'inner join':join_table,  'order by':order_by_columns }

    return cmd
   
          
def parse_insert(semantica):
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
    if columns
        columns = columns[0].replace('(', '').replace(')', '').split(',')

    if columns:
        resultado = {f" {columns[i]} : {values[i]}" for i in range(len(columns))}
    else:
        resultado = values
    cmd = {'func':'INSERT', 'tabela':table, 'values': resultado}
    # # novos_dados = {'emp_no': '10005', 'dept_no': 'd005', 'from_date':'1986-06-26','to_date':'9999-01-01'}
    # novos_dados = ['10006', 'd005', '1986-06-26', '9999-01-01']
    return cmd

def parse_update(semantica):
    if "atualize" not in semantica or "defina" not in semantica or "onde" not in semantica:
        raise ValueError("Comando UPDATE incompleto")
    
    table = semantica[semantica.index("atualize") + 1]
    set_index = semantica.index("defina") + 1
    where_index = semantica.index("onde")

    set_clause = semantica[set_index:where_index]
    condition = semantica[where_index + 1:]
    dicionario_condicao = {condition[0]: (condition[1], condition[2])}
    cmd = {'func':'UPDATE', 'tabela':table, 'set': set_clause, 'condition': dicionario_condicao}
    return cmd

def parse_delete(semantica):
    if "de" not in semantica or "onde" not in semantica:
        raise ValueError("Comando DELETE incompleto")
    
    from_index = semantica.index("de")
    table = semantica[from_index + 1]
    where_index = semantica.index("onde") if "onde" in semantica else None
    condition = semantica[where_index + 1:] if where_index is not None else None
    if condition:
        dicionario_condicao = {condition[0]: (condition[1], condition[2])}
    cmd = {'func':'DELETE', 'tabela':table, 'condition': dicionario_condicao}
    return cmd
