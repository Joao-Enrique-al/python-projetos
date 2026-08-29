import tkinter as tk


def dizer_ola():
    nome = entrada_nome.get()

    if nome:
        rotulo_saudacao.config(text=f"Olá, {nome}!")
    else:
        rotulo_saudacao.config(text="Olá, mundo!")


janela = tk.Tk()
janela.title("Meu Primeiro Aplicativo Tkinter")
janela.geometry("300x200")

janela.resizable(False, False)

rotulo_titulo = tk.Label(
    janela,
    text="Bem-vindo ao Tkinter!",
    font=("Arial", 16)
)
rotulo_titulo.pack(pady=10)

entrada_nome = tk.Entry(janela, width=20)
entrada_nome.pack(pady=10)

botao_ola = tk.Button(
    janela,
    text="Dizer Olá",
    command=dizer_ola
)
botao_ola.pack(pady=10)

rotulo_saudacao = tk.Label(
    janela,
    text="",
    font=("Arial", 12)
)
rotulo_saudacao.pack(pady=10)

janela.mainloop()