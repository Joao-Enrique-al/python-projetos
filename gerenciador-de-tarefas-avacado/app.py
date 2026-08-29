import tkinter as tk
from tkinter import messagebox
import json


def adicionar_tarefa():
    tarefa = entrada_tarefa.get()

    if tarefa:
        lista_tarefas.insert(tk.END, tarefa)
        entrada_tarefa.delete(0, tk.END)

        salvar_tarefas()
    else:
        messagebox.showwarning(
            "Aviso",
            "Digite uma tarefa!"
        )


def excluir_tarefa():
    try:
        indice_tarefa_selecionada = lista_tarefas.curselection()[0]

        lista_tarefas.delete(indice_tarefa_selecionada)

        salvar_tarefas()

    except IndexError:
        messagebox.showwarning(
            "Aviso",
            "Selecione uma tarefa para excluir!"
        )


def marcar_concluida():
    try:
        indice_tarefa_selecionada = lista_tarefas.curselection()[0]

        tarefa = lista_tarefas.get(indice_tarefa_selecionada)

        if tarefa.startswith("✓ "):
            tarefa = tarefa[2:]
        else:
            tarefa = "✓ " + tarefa

        lista_tarefas.delete(indice_tarefa_selecionada)
        lista_tarefas.insert(
            indice_tarefa_selecionada,
            tarefa
        )

        salvar_tarefas()

    except IndexError:
        messagebox.showwarning(
            "Aviso",
            "Selecione uma tarefa para marcar como concluída!"
        )


def salvar_tarefas():
    tarefas = lista_tarefas.get(0, tk.END)

    with open("tarefas.json", "w") as arquivo:
        json.dump(list(tarefas), arquivo)


def carregar_tarefas():
    try:
        with open("tarefas.json", "r") as arquivo:
            tarefas = json.load(arquivo)

        for tarefa in tarefas:
            lista_tarefas.insert(tk.END, tarefa)

    except FileNotFoundError:
        pass


# Criar a janela principal
janela = tk.Tk()
janela.title("Aplicativo Gerenciador de Tarefas")
janela.geometry("400x450")
janela.resizable(False, False)


# Título
rotulo_titulo = tk.Label(
    janela,
    text="Lista de Tarefas",
    font=("Arial", 18, "bold")
)
rotulo_titulo.pack(pady=10)


# Área de entrada
quadro_entrada = tk.Frame(janela)
quadro_entrada.pack(pady=10)

entrada_tarefa = tk.Entry(
    quadro_entrada,
    width=30,
    font=("Arial", 12)
)
entrada_tarefa.pack(
    side=tk.LEFT,
    padx=5
)


botao_adicionar = tk.Button(
    quadro_entrada,
    text="Adicionar Tarefa",
    command=adicionar_tarefa
)
botao_adicionar.pack(side=tk.LEFT)


# Área da lista
quadro_lista = tk.Frame(janela)
quadro_lista.pack(
    pady=10,
    fill=tk.BOTH,
    expand=True
)


# Barra de rolagem
barra_rolagem = tk.Scrollbar(quadro_lista)
barra_rolagem.pack(
    side=tk.RIGHT,
    fill=tk.Y
)


# Lista de tarefas
lista_tarefas = tk.Listbox(
    quadro_lista,
    width=45,
    height=12,
    font=("Arial", 12),
    selectmode=tk.SINGLE,
    yscrollcommand=barra_rolagem.set
)

lista_tarefas.pack(
    side=tk.LEFT,
    fill=tk.BOTH,
    expand=True
)


barra_rolagem.config(
    command=lista_tarefas.yview
)


# Botões
quadro_botoes = tk.Frame(janela)
quadro_botoes.pack(pady=10)


botao_concluir = tk.Button(
    quadro_botoes,
    text="Marcar como Concluída",
    command=marcar_concluida
)
botao_concluir.pack(
    side=tk.LEFT,
    padx=5
)


botao_excluir = tk.Button(
    quadro_botoes,
    text="Excluir Tarefa",
    command=excluir_tarefa
)
botao_excluir.pack(
    side=tk.LEFT,
    padx=5
)


# Carregar tarefas salvas
carregar_tarefas()


# Iniciar aplicação
janela.mainloop()