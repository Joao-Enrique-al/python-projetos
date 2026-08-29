import time
import os
import platform


def limpar_tela():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")


def formatar_tempo(segundos):
    # formatar(30) => 00:30
    # formatar(75) => 01:15
    # formatar(0) => 00:00

    minutos = segundos // 60
    segundos_restantes = segundos % 60

    return f"{minutos:02d}:{segundos_restantes:02d}"


def contagem_regressiva(segundos, titulo):
    for restante in range(segundos, 0, -1):
        limpar_tela()

        print(f"\n⏰ {titulo} ⏰")
        print(
            f"\n⏳ Tempo restante: "
            f"{formatar_tempo(restante)}"
        )

        if titulo == "Sessão de Trabalho":
            print("\n🧠 Concentre-se na sua tarefa! 💪")

        elif "Pausa" in titulo:
            print("\n☕ Respire um pouco... 😉")

        time.sleep(1)

    limpar_tela()

    print(f"\n✅ {titulo} concluído!")

    if platform.system() == "Windows":
        import winsound

        # frequência em hertz, duração em milissegundos
        winsound.Beep(1000, 500)

    else:
        print("🔔")


def cronometro_pomodoro():
    try:
        limpar_tela()

        print("\n==== 🍅 CRONÔMETRO POMODORO 🍅 ====")

        # Configurações padrão
        minutos_trabalho = 25
        minutos_pausa_curta = 5
        minutos_pausa_longa = 15
        ciclos = 4

        personalizar = input(
            "\nUsar configurações padrão "
            "(25 min trabalho, 5 min pausa curta, "
            "15 min pausa longa)? (sim/não): "
        ).lower()

        if personalizar.startswith("n"):
            try:
                minutos_trabalho = int(
                    input(
                        "\nDigite a duração da sessão de trabalho "
                        "(minutos): "
                    )
                )

                minutos_pausa_curta = int(
                    input(
                        "Digite a duração da pausa curta "
                        "(minutos): "
                    )
                )

                minutos_pausa_longa = int(
                    input(
                        "Digite a duração da pausa longa "
                        "(minutos): "
                    )
                )

                ciclos = int(
                    input(
                        "Digite o número de ciclos antes "
                        "de uma pausa longa: "
                    )
                )

            except ValueError:
                print(
                    "\n❌ Entrada inválida! "
                    "Usando as configurações padrão."
                )

                time.sleep(2)

        limpar_tela()

        print("\n🚀 Iniciando o Cronômetro Pomodoro com:")

        print(
            f"• {minutos_trabalho} minutos de sessões de trabalho"
        )

        print(
            f"• {minutos_pausa_curta} minutos de pausas curtas"
        )

        print(
            f"• {minutos_pausa_longa} minutos de pausa longa "
            f"após {ciclos} ciclos"
        )

        print(
            "• Pressione Ctrl+C a qualquer momento para sair"
        )

        input("\nPressione Enter para começar...")

        # Converter minutos para segundos
        segundos_trabalho = minutos_trabalho * 60
        segundos_pausa_curta = minutos_pausa_curta * 60
        segundos_pausa_longa = minutos_pausa_longa * 60

        ciclos_concluidos = 0

        while True:
            contagem_regressiva(
                segundos_trabalho,
                "Sessão de Trabalho"
            )

            ciclos_concluidos += 1

            if ciclos_concluidos % ciclos == 0:
                input(
                    "\nHora de fazer uma pausa longa! "
                    "Pressione Enter para começar..."
                )

                contagem_regressiva(
                    segundos_pausa_longa,
                    "Pausa Longa"
                )

                input(
                    "\nPausa longa concluída! "
                    "Pressione Enter para iniciar "
                    "a próxima sessão de trabalho..."
                )

            else:
                input(
                    "\nHora de fazer uma pausa curta! "
                    "Pressione Enter para começar..."
                )

                contagem_regressiva(
                    segundos_pausa_curta,
                    "Pausa Curta"
                )

                input(
                    "\nPausa curta concluída! "
                    "Pressione Enter para iniciar "
                    "a próxima sessão de trabalho..."
                )

    except KeyboardInterrupt:
        limpar_tela()
        print("Até logo! 👋")


cronometro_pomodoro()