import tkinter as tk


def calcular_soma():
    try:
        numero1 = float(primeiro_numero.get())
        numero2 = float(segundo_numero.get())

        resultado = numero1 + numero2

        rotulo_resultado.config(text=f"Resultado: {resultado}")

    except ValueError:
        rotulo_resultado.config(
            text="Digite números válidos!"
        )


# Criar a janela principal
janela = tk.Tk()
janela.title("Calculadora Simples")
janela.geometry("300x250")


rotulo_titulo = tk.Label(
    janela,
    text="Calculadora Simples",
    font=("Arial", 16)
)
rotulo_titulo.pack(pady=10)


quadro1 = tk.Frame(janela)
quadro1.pack(pady=5)

rotulo_numero1 = tk.Label(
    quadro1,
    text="Primeiro número:"
)
rotulo_numero1.pack(side=tk.LEFT)

primeiro_numero = tk.Entry(
    quadro1,
    width=10
)
primeiro_numero.pack()


quadro2 = tk.Frame(janela)
quadro2.pack(pady=5)

rotulo_numero2 = tk.Label(
    quadro2,
    text="Segundo número:"
)
rotulo_numero2.pack(side=tk.LEFT)

segundo_numero = tk.Entry(
    quadro2,
    width=10
)
segundo_numero.pack()


botao_calcular = tk.Button(
    janela,
    text="Somar números",
    command=calcular_soma
)
botao_calcular.pack(pady=10)


rotulo_resultado = tk.Label(
    janela,
    text="Resultado: ",
    font=("Arial", 12)
)
rotulo_resultado.pack(pady=10)


def limpar_campos():
    primeiro_numero.delete(0, tk.END)
    segundo_numero.delete(0, tk.END)

    rotulo_resultado.config(
        text="Resultado: "
    )


botao_limpar = tk.Button(
    janela,
    text="Limpar",
    command=limpar_campos
)
botao_limpar.pack(pady=5)


janela.mainloop()