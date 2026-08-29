tarefas = []


def exibir_menu():
    print("\n=== Gerenciador de Tarefas ===")
    print("1. Adicionar tarefa")
    print("2. Ver tarefas")
    print("3. Concluir tarefa")
    print("4. Excluir tarefa")
    print("0. Sair")
    print("==============================")


def adicionar_tarefa():
    titulo = input("Digite o título da tarefa: ")

    tarefas.append({
        "titulo": titulo,
        "concluida": False
    })

    print(f"Tarefa '{titulo}' adicionada com sucesso!")


def visualizar_tarefas():
    if not tarefas:
        print("Nenhuma tarefa encontrada.")
        return

    print("\n=== Minhas tarefas ===")

    for indice, tarefa in enumerate(tarefas):
        status = "✓" if tarefa["concluida"] else " "

        print(
            f"{indice + 1}. [{status}] {tarefa['titulo']}"
        )

    print("======================\n")


def concluir_tarefa():
    visualizar_tarefas()

    if not tarefas:
        return

    try:
        numero_tarefa = int(
            input("Digite o número da tarefa para marcar como concluída: ")
        )

        if numero_tarefa < 1 or numero_tarefa > len(tarefas):
            print("Número de tarefa inválido.")
            return

        tarefa_a_concluir = tarefas[numero_tarefa - 1]
        tarefa_a_concluir["concluida"] = True

        print(
            f"Tarefa '{tarefa_a_concluir['titulo']}' "
            "marcada como concluída!"
        )

    except ValueError:
        print("Digite um número válido.")


def excluir_tarefa():
    visualizar_tarefas()

    if not tarefas:
        return

    try:
        numero_tarefa = int(
            input("Digite o número da tarefa para excluir: ")
        )

        if numero_tarefa < 1 or numero_tarefa > len(tarefas):
            print("Número de tarefa inválido.")
            return

        tarefa_excluida = tarefas.pop(numero_tarefa - 1)

        print(
            f"Tarefa '{tarefa_excluida['titulo']}' "
            "excluída com sucesso!"
        )

    except ValueError:
        print("Digite um número válido.")


def principal():
    while True:
        exibir_menu()

        escolha = input("Digite sua escolha (0-4): ")

        if escolha == "1":
            adicionar_tarefa()

        elif escolha == "2":
            visualizar_tarefas()

        elif escolha == "3":
            concluir_tarefa()

        elif escolha == "4":
            excluir_tarefa()

        elif escolha == "0":
            print("Até logo! 👋")
            break

        else:
            print("❌ Escolha inválida. Digite uma opção entre 0 e 4.")


principal()