import tkinter as tk
import interpreter
import execute_cmd as ec
import os

def manager_func(bd, comando):
    # Insira em dept_emp (emp_no,dept_no,from_date,to_date) valores ('10005','d005','1986-06-26','9999-01-01')
    diretorio_atual = os.getcwd()  # Obtém o caminho do diretório atual
    subdiretorio = 'dados_salvos'
    variavel = 'bd'
    caminho_banco = os.path.join(diretorio_atual, subdiretorio, bd)

    if comando['func'] == 'DELETE':
        caminho_tabela = os.path.join(caminho_banco, f"{comando['tabela']}.csv")
        ec.deletar_dados(caminho_tabela, comando['condition'])
    if comando['func'] == 'INSERT':
        caminho_tabela = os.path.join(caminho_banco, f"{comando['tabela']}.csv")
        ec.inserir_dados(caminho_tabela,comando['values'] )
    if comando['func'] == 'UPDATE':
        # Atualize dept_emp defina emp_no = 7000 onde dept_no = '1'
        caminho_tabela = os.path.join(caminho_banco, f"{comando['tabela']}.csv")
        ec.atualizar_dados(caminho_tabela, comando['condition'], comando['set'])


# cmd = {'func':'INSERT', 'tabela':table, 'colunas': columns, 'values': values}
        



def window():

    def preencher(bd, cmd):
        result = interpreter.parse_query(cmd)
        print((result))
        manager_func(bd, result)

    janela = tk.Tk()
    janela.title("Central")
    janela.geometry("400x400")

    label_bd = tk.Label(janela, text="Insira o Banco de Dados")
    entry_bd = tk.Entry(janela)
    button_bd = tk.Button(janela, text="Enivar", command=lambda:entry_bd.config(state="readonly"))
    label_comando = tk.Label(janela, text = "Insira o comando:")
    entry_comando = tk.Entry(janela, width=20)
    button_enviar = tk.Button(janela, width=15, text = "Enviar", command=lambda:preencher(entry_bd.get(), entry_comando.get()))


    label_bd.grid(column=0, row=0)
    entry_bd.grid(column=1, row=0)
    button_bd.grid(column=2, row=0)
    label_comando.grid(column=0, row=1)
    entry_comando.grid(column=1, row=1)
    button_enviar.grid(column=2, row=1)



    janela.mainloop()

window()



