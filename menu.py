import tkinter as tk
import connection_database as cdb
import importacao
import comandos
def menu():
    janela = tk.Tk()
    janela.title("Menu")
    janela.geometry("200x200")
    button_import = tk.Button(text="Importação",command=lambda:importacao.window())
    button_parser = tk.Button(text="Comandos",command=lambda:comandos.window())
    

    button_import.pack(pady=10)
    button_parser.pack(pady=10)

    janela.mainloop()

menu()