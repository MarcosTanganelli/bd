class QueryParser:
    def __init__(self):
        self.queries = []

    def parse_query(self, query):
        tokens = query.lower().split()

        query_type = tokens[0].lower()
        if query_type in ["selecione", "insira", "atualize", "exclua"]:
            return self.parse_select_insert_update_delete(tokens)
        else:
            raise ValueError("Comando não suportado")

    def parse_select_insert_update_delete(self, tokens):
        if tokens[0] == "selecione":
            return self.parse_select(tokens)
        elif tokens[0] == "insira":
            return self.parse_insert(tokens)
        elif tokens[0] == "atualize":
            return self.parse_update(tokens)
        elif tokens[0] == "exclua":
            return self.parse_delete(tokens)

    def parse_select(self, tokens):
        if "da" not in tokens:
            raise ValueError("Comando SELECT incompleto")

        select_index = tokens.index("selecione")
        from_index = tokens.index("da")

        columns = tokens[select_index + 1:from_index]
        table = tokens[from_index + 1]

        where_index = tokens.index("onde") if "onde" in tokens else None
        condition = tokens[where_index + 1:] if where_index is not None else None

        return {"tipo": "select", "colunas": columns, "tabela": table, "condicao": condition}

    def parse_insert(self, tokens):
        if "em" not in tokens:
            raise ValueError("Comando INSERT incompleto")

        insert_index = tokens.index("insira")
        into_index = tokens.index("em")

        table = tokens[into_index + 1]
        values_start_index = tokens.index("valores") + 1
        values = tokens[values_start_index:]

        return {"tipo": "insert", "tabela": table, "valores": values}

    def parse_update(self, tokens):
        if "em" not in tokens or "definido" not in tokens:
            raise ValueError("Comando UPDATE incompleto")

        update_index = tokens.index("atualize")
        table = tokens[tokens.index("em") + 1]
        set_index = tokens.index("definido") + 1
        set_clause = tokens[set_index:]

        return {"tipo": "update", "tabela": table, "definido": set_clause}

    def parse_delete(self, tokens):
        if "de" not in tokens:
            raise ValueError("Comando DELETE incompleto")

        delete_index = tokens.index("exclua")
        from_index = tokens.index("de")

        table = tokens[from_index + 1]
        where_index = tokens.index("onde") if "onde" in tokens else None
        condition = tokens[where_index + 1:] if where_index is not None else None

        return {"tipo": "delete", "tabela": table, "condition": condition}


if __name__ == "__main__":
    query_parser = QueryParser()

    query1 = "Selecione nome, idade da Funcionarios onde idade > 25 e salario > 5000"
    parsed_query1 = query_parser.parse_query(query1)
    print(parsed_query1)

    query2 = "Insira em Funcionarios valores ('João', 30, 6000)"
    parsed_query2 = query_parser.parse_query(query2)
    print(parsed_query2)

    # query3 = "Atualize Funcionarios definido salario = 7000 onde nome = 'João'"
    # parsed_query3 = query_parser.parse_query(query3)
    # print(parsed_query3)

    query4 = "Exclua de Funcionarios onde idade > 25"
    parsed_query4 = query_parser.parse_query(query4)
    print(parsed_query4)
