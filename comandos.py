import tkinter as tk
import interpreter
import execute_cmd as ec
import os




def window():

    def preencher(bd, cmd):
        result = interpreter.parse_query(bd,cmd)
        if isinstance(result, dict):
            print(f"dicionario:{result}")
        elif isinstance(result, list):
            print(f"lista:{result}")
            label_result.config(text=f"{result}")
            
            # label = ""
            # for a in result[1:]:
            #     label += f"\nItem {a}"
            #     print(label)
            # label_result.config(text=label)
        else:
            label_result.config(text=f"{result}")

    def ativar_funcs():
        entry_bd.config(state="readonly")
        entry_comando.config(state="normal")
    janela = tk.Tk()
    janela.title("Central")
    janela.geometry("600x600")

    label_bd = tk.Label(janela, text="Insira o Banco de Dados")
    entry_bd = tk.Entry(janela)
    button_bd = tk.Button(janela, text="Enivar", command=lambda:ativar_funcs())
    label_comando = tk.Label(janela, text = "Insira o comando:")
    entry_comando = tk.Entry(janela, width=20, state='disabled')
    button_enviar = tk.Button(janela, width=15, text = "Enviar", command=lambda:preencher(entry_bd.get(), entry_comando.get()))
    label_result = tk.Label(janela)

    label_bd.grid(column=0, row=0)
    entry_bd.grid(column=1, row=0)
    button_bd.grid(column=2, row=0)
    label_comando.grid(column=0, row=1)
    entry_comando.grid(column=1, row=1)
    button_enviar.grid(column=2, row=1)
    label_result.grid(column=1, row=3)




    janela.mainloop()

window()



