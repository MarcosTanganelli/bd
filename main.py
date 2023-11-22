import tkinter as tk
import interpreter
import connection_database


def main():

    def preencher(cmd):
        result = interpreter.parse_query(cmd)
        print(connection_database.executar_consulta(result))

    janela = tk.Tk()
    janela.title("Central")
    janela.geometry("300x300")


    label_comando = tk.Label(text = "Insira o comando:")
    entry_comando = tk.Entry(width=20)
    button_enviar = tk.Button(janela, width=15, text = "Enviar", command=lambda:preencher(entry_comando.get()))


    label_comando.pack(pady = 10)
    entry_comando.pack(pady = 10)
    button_enviar.pack(pady = 10)



    janela.mainloop()

if __name__ == "__main__":
    main()