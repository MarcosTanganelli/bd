import tkinter as tk
import connection_database as cdb
from tkinter import ttk
from tkinter import filedialog
import os

def window():
    def enviar_button(bd):
        global conn, cursor
        conn = cdb.conectar_mysql(bd)
        if conn:
            label_status.config(text="Status: Conectado!")
            entry_banco.config(state="readonly")
            button_system.config(state="active")
            cursor = conn.cursor()
            preencher_combobox(bd)

    def gerar_csv(db, table):
        direc_selecionado = filedialog.askdirectory(
                title="Selecione um arquivo CSV para salvar no sistema"
            )
        cdb.export(db, table, direc_selecionado)


    

    def preencher_combobox(bd):
        try:
            combo_list = cdb.executar_consulta(bd, "SHOW TABLES")
            combo_tables['values'] = [item[f'Tables_in_{bd}'] for item in combo_list]
        except Exception as e:
            print(f"Erro ao preencher combobox: {e}")
        finally:
            cursor.close()

    def enviar_system(bd):
        tipos_de_arquivo = [("Arquivos CSV", "*.csv")]
        arquivo_selecionado = filedialog.askopenfile(
        title="Selecione um arquivo CSV para salvar no sistema",
        filetypes=tipos_de_arquivo
    )
        # print(f"PATH:{arquivo_selecionado.name}")
        # Verifique se o usuário selecionou algum arquivo
        if arquivo_selecionado:
            # Obtenha apenas o nome do arquivo a partir do caminho completo
            nome_do_arquivo = os.path.basename(arquivo_selecionado.name)

            # print("Nome do arquivo selecionado:", nome_do_arquivo)
        cdb.save_csv_system(arquivo_selecionado.name, nome_do_arquivo, bd)

    janela = tk.Tk()
    janela.title("Importação")
    janela.geometry("400x400")
    label_banco = tk.Label(janela, text="Insira o Banco de dados:")
    entry_banco = tk.Entry(janela)
    button_enviar = tk.Button(janela, text="Enviar", command= lambda: enviar_button(entry_banco.get()))
    label_status  = tk.Label(janela, text="Status: Desconectado!")
    label_tables = tk.Label(janela, text="Escolha uma tabela:")
    combo_tables = ttk.Combobox(janela, state="readonly")
    button_csv   = tk.Button(janela, text=".CSV",command=lambda:gerar_csv(entry_banco.get(), combo_tables.get()))
    label_system = tk.Label(janela, text="Importar CSV para o sistema:")
    button_system = tk.Button(janela, text="Enviar", command=lambda:enviar_system(entry_banco.get()), state="disable")
    




    label_banco.grid(column=0, row=0)
    entry_banco.grid(column=1, row=0)
    button_enviar.grid(column=2, row=0)
    label_status.grid(column=1, row=1)
    label_tables.grid(column=0, row=2)
    combo_tables.grid(column=1, row=2)
    button_csv.grid(column=2, row=2)
    label_system.grid(column=0, row=4)
    button_system.grid(column=1, row=4)





    janela.mainloop()


