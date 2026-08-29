import tkinter as tk
from tkinter import colorchooser


current_x, current_y = 0, 0
cor = "black"
tamanho_pincel = 5


def iniciar_posicao(event):
    global current_x, current_y

    current_x, current_y = event.x, event.y


def desenhar_linha(event):
    global current_x, current_y

    tela_desenho.create_line(
        current_x,
        current_y,
        event.x,
        event.y,
        fill=cor,
        width=tamanho_pincel,
        capstyle=tk.ROUND,
        smooth=True
    )

    current_x, current_y = event.x, event.y


def alterar_cor():
    global cor

    nova_cor = colorchooser.askcolor()[1]

    if nova_cor:
        cor = nova_cor
        botao_cor.config(bg=cor)


def limpar_tela():
    tela_desenho.delete("all")


def alterar_tamanho_pincel(novo_tamanho):
    global tamanho_pincel

    tamanho_pincel = novo_tamanho


def definir_pincel_pequeno():
    alterar_tamanho_pincel(2)


def definir_pincel_medio():
    alterar_tamanho_pincel(5)


def definir_pincel_grande():
    alterar_tamanho_pincel(10)


# Criar a janela principal
janela = tk.Tk()
janela.title("Aplicativo de Desenho Simples")
janela.geometry("800x600")


# Título
rotulo_titulo = tk.Label(
    janela,
    text="Aplicativo de Desenho Simples",
    font=("Arial", 16)
)
rotulo_titulo.pack(pady=10)


# Barra de ferramentas
barra_ferramentas = tk.Frame(janela)
barra_ferramentas.pack(
    fill=tk.X,
    pady=5
)


# Botão para escolher a cor
botao_cor = tk.Button(
    barra_ferramentas,
    text="Escolher Cor",
    command=alterar_cor,
    bg=cor
)
botao_cor.pack(
    side=tk.LEFT,
    padx=5
)


# Botão para limpar a tela
botao_limpar = tk.Button(
    barra_ferramentas,
    text="Limpar Tela",
    command=limpar_tela
)
botao_limpar.pack(
    side=tk.LEFT,
    padx=5
)


# Área para escolher o tamanho do pincel
quadro_tamanho = tk.Frame(barra_ferramentas)
quadro_tamanho.pack(
    side=tk.LEFT,
    padx=15
)


rotulo_tamanho = tk.Label(
    quadro_tamanho,
    text="Tamanho do Pincel:"
)
rotulo_tamanho.pack(side=tk.LEFT)


# Pincel pequeno
botao_pequeno = tk.Button(
    quadro_tamanho,
    text="Pequeno",
    command=definir_pincel_pequeno
)
botao_pequeno.pack(
    side=tk.LEFT,
    padx=2
)


# Pincel médio
botao_medio = tk.Button(
    quadro_tamanho,
    text="Médio",
    command=definir_pincel_medio
)
botao_medio.pack(
    side=tk.LEFT,
    padx=2
)


# Pincel grande
botao_grande = tk.Button(
    quadro_tamanho,
    text="Grande",
    command=definir_pincel_grande
)
botao_grande.pack(
    side=tk.LEFT,
    padx=2
)


# Área de desenho
tela_desenho = tk.Canvas(
    janela,
    bg="white"
)

tela_desenho.pack(
    fill=tk.BOTH,
    expand=True,
    padx=10,
    pady=10
)


# Eventos do mouse
# Registra a posição inicial quando o botão esquerdo é pressionado
tela_desenho.bind(
    "<Button-1>",
    iniciar_posicao
)

# Acompanha o movimento do mouse enquanto o botão esquerdo está pressionado
tela_desenho.bind(
    "<B1-Motion>",
    desenhar_linha
)


# Instrução
rotulo_instrucao = tk.Label(
    janela,
    text="Clique e arraste para desenhar",
    font=("Arial", 10)
)
rotulo_instrucao.pack(pady=5)


# Iniciar aplicação
janela.mainloop()