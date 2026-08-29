import random
import time


def exibir_boas_vindas():
    print("\n==== PEDRA, PAPEL E TESOURA ====")
    print("🪨  📄  ✂️")
    print("\nRegras:")
    print("- Pedra quebra a Tesoura")
    print("- Tesoura corta o Papel")
    print("- Papel cobre a Pedra")
    print("- O primeiro a vencer 3 rodadas é o campeão!")
    print("\n----------------------------")


def obter_escolha_jogador():
    while True:
        print("\nFaça sua escolha:")
        print("1. Pedra 🪨")
        print("2. Papel 📄")
        print("3. Tesoura ✂️")

        try:
            escolha = int(input("Digite sua escolha (1-3): "))

            if 1 <= escolha <= 3:
                return escolha
            else:
                print("Digite um número entre 1 e 3.")

        except ValueError:
            print("Digite um número válido.")


def obter_escolha_computador():
    return random.randint(1, 3)


def converter_escolha_para_texto(escolha):
    opcoes = {
        1: "Pedra 🪨",
        2: "Papel 📄",
        3: "Tesoura ✂️"
    }

    return opcoes[escolha]


def determinar_vencedor(escolha_jogador, escolha_computador):
    # Empate
    if escolha_jogador == escolha_computador:
        return "empate"

    # Casos em que o jogador vence:
    elif (
        (escolha_jogador == 1 and escolha_computador == 3) or
        (escolha_jogador == 3 and escolha_computador == 2) or
        (escolha_jogador == 2 and escolha_computador == 1)
    ):
        return "jogador"

    else:
        return "computador"


def exibir_resultado_rodada(
    escolha_jogador,
    escolha_computador,
    resultado
):
    texto_jogador = converter_escolha_para_texto(escolha_jogador)
    texto_computador = converter_escolha_para_texto(escolha_computador)

    print(f"\nVocê escolheu: {texto_jogador}")

    print("Computador está escolhendo", end="")

    for _ in range(3):
        print(".", end="", flush=True)
        time.sleep(0.5)

    print(f"\nComputador escolheu: {texto_computador}")

    if resultado == "empate":
        print("Empate! 🤝")

    elif resultado == "jogador":
        print("Você venceu esta rodada! 🎉")

    else:
        print("O computador venceu esta rodada! 💻")


def jogar():
    """Função principal do jogo."""
    exibir_boas_vindas()

    pontuacao_jogador = 0
    pontuacao_computador = 0
    pontuacao_alvo = 3
    numero_rodada = 1

    while (
        pontuacao_jogador < pontuacao_alvo
        and pontuacao_computador < pontuacao_alvo
    ):
        print(f"\n=== Rodada {numero_rodada} ===")
        print(
            f"Placar: Você {pontuacao_jogador} - "
            f"{pontuacao_computador} Computador"
        )

        escolha_jogador = obter_escolha_jogador()
        escolha_computador = obter_escolha_computador()

        resultado = determinar_vencedor(
            escolha_jogador,
            escolha_computador
        )

        exibir_resultado_rodada(
            escolha_jogador,
            escolha_computador,
            resultado
        )

        if resultado == "jogador":
            pontuacao_jogador += 1

        elif resultado == "computador":
            pontuacao_computador += 1

        numero_rodada += 1

    print("\n==== FIM DE JOGO ====")
    print(
        f"Placar final: Você {pontuacao_jogador} - "
        f"{pontuacao_computador} Computador"
    )

    if pontuacao_jogador > pontuacao_computador:
        print("Parabéns! Você é o campeão! 🎉")

    else:
        print("Mais sorte na próxima! O computador venceu o jogo. 🤖")

    jogar_novamente = input(
        "\nDeseja jogar novamente? (s/n): "
    ).lower()

    if jogar_novamente.startswith("s"):
        jogar()

    else:
        print("Até logo! 👋")


jogar()