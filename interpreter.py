
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

    cmd = f"SELECT {' '.join(columns)} FROM {''.join(table) if(table[1]) else table}"

    if inner_join_index is not None:
        join_table_index = semantica.index("com")
        join_table = semantica[join_table_index + 1]
        on_index = semantica.index("em") + 1
        on_condition = semantica[on_index:where_index]
        on_condition = [s.replace("e", "AND") if s == "e" else s for s in on_condition]
        on_condition = [s.replace("ou", "OR") if s == "ou" else s for s in on_condition]
        inner = f"\nJOIN {''.join(join_table) if(join_table[1]) else join_table} ON {' '.join(on_condition)}"
        cmd = cmd + inner

    if condition is not None:      
        condition = [s.replace("e", "AND") if s == "e" else s for s in condition]
        condition = [s.replace("ou", "OR") if s == "ou" else s for s in condition]
        where = f"\nWHERE {' '.join(condition)}"
        cmd = cmd + where

    if order_by_index is not None:
        order_by = f"\nORDER BY {''.join(order_by_columns) if(order_by_columns[1]) else order_by_columns}"
        cmd = cmd + order_by
    print(cmd)
    return cmd
   
          
def parse_insert(semantica):
    if "em" not in semantica or "valores" not in semantica:
        raise ValueError("Comando INSERT incompleto")
    
    into_index = semantica.index("em")
    table = semantica[into_index + 1]

    values_start_index = semantica.index("valores") + 1
    columns_start_index = semantica.index("em") + 2

    columns = semantica[columns_start_index:values_start_index - 1]
    values = semantica[values_start_index:]
    cmd = f"INSERT INTO {table} {''.join(columns) if(columns[1]) else columns} \nVALUES {''.join(values) if(values[1]) else values}"
    print(cmd)
    return cmd

def parse_update(semantica):
    if "atualize" not in semantica or "defina" not in semantica or "onde" not in semantica:
        raise ValueError("Comando UPDATE incompleto")
    
    table = semantica[semantica.index("atualize") + 1]
    set_index = semantica.index("defina") + 1
    where_index = semantica.index("onde")

    set_clause = semantica[set_index:where_index]
    condition = semantica[where_index + 1:]

    cmd = f"UPDATE {table} SET {''.join(set_clause) if(set_clause[1]) else set_clause} WHERE {''.join(condition) if(condition[1]) else condition}"
    return cmd

def parse_delete(semantica):
    if "de" not in semantica or "onde" not in semantica:
        raise ValueError("Comando DELETE incompleto")
    
    from_index = semantica.index("de")
    table = semantica[from_index + 1]
    where_index = semantica.index("onde") if "onde" in semantica else None
    condition = semantica[where_index + 1:] if where_index is not None else None
    cmd = f"DELETE FROM {table} \nwhere {''.join(condition) if(condition[1]) else condition}"
    return cmd
