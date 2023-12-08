import tkinter as tk
from tkinter import ttk
import interpreter
import execute_cmd as ec
import os


def criar_treeview(dados, tree):
    if not dados or not isinstance(dados[0], dict):
        return

    # Obter as chaves esperadas (cabeçalhos) na ordem inserida
    chaves_esperadas = list(dados[0].keys())

    # Limpar as colunas existentes, se houver
    for coluna in tree["columns"]:
        tree.delete(coluna)

    # Criar colunas com base nas chaves do primeiro dicionário
    chaves = chaves_esperadas
    tree["columns"] = chaves
    for coluna in chaves:
        tree.heading(coluna, text=coluna)
        tree.column(coluna, anchor=tk.CENTER)

    # Adicionar dados à TreeView apenas se for um dicionário e todas as chaves estiverem presentes
    for dado in dados:
        if isinstance(dado, dict) and set(dado.keys()) == set(chaves_esperadas):
            valores = [dado[chave] for chave in chaves]
            tree.insert("", tk.END, values=valores)

def window():

    def preencher(bd, cmd):
        result = interpreter.parse_query(bd,cmd)
        global tree
        tree.destroy()


        tree = ttk.Treeview(janela)  

        if isinstance(result, list):
            criar_treeview(result, tree)
            tree.pack(pady=10)
        else:
            label_result.config(text=f"{result}")

    def ativar_funcs():
        entry_bd.config(state="readonly")
        entry_comando.config(state="normal")
    janela = tk.Tk()
    janela.title("Comandos")
    janela.geometry("1000x1000")

    label_bd = tk.Label(janela, text="Insira o Banco de Dados")
    entry_bd = tk.Entry(janela)
    button_bd = tk.Button(janela, text="Enviar", command=lambda:ativar_funcs())
    label_comando = tk.Label(janela, text = "Insira o comando:")
    entry_comando = tk.Entry(janela, width=20, state='disabled')
    button_enviar = tk.Button(janela, width=15, text = "Enviar", command=lambda:preencher(entry_bd.get(), entry_comando.get()))
    # text_bd = "employees"
    # text_comand = "selecione da dept_emp ordene em from_date asc"
    # button_enviar = tk.Button(janela, width=15, text = "Enviar", command=lambda:preencher(text_bd, text_comand))
    label_result = tk.Label(janela)
    global tree 
    tree = ttk.Treeview(janela)
    tree["show"] = "headings"

    label_bd.pack(pady=10)
    entry_bd.pack(pady=10)
    button_bd.pack(pady=10)
    label_comando.pack(pady=10)
    entry_comando.pack(pady=10)
    button_enviar.pack(pady=10)
    label_result.pack(pady=10)

    janela.mainloop()

# window()
# selecione emp_no da dept_emp junte com tabela em emp_no = emp_no onde emp_no == 10001


#INSERT TUDO FUNCIONANDO
# Insira em dept_emp (emp_no,dept_no,from_date,to_date) valores (19999,1,1986-06-26,9999-01-01)
#UPDATE TUDO FUNCIONANDO
# Atualize dept_emp defina emp_no = 7000 onde emp_no == 19999
#DELETE TUDO FUNCIONANDO
# Exclua de dept_emp onde emp_no == 69 ou emp_no == 99