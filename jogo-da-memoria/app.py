import random
import time
import os


def limpar_tela():
    """Limpa a tela do terminal."""
    os.system("cls" if os.name == "nt" else "clear")


print("\n=== 🧠 JOGO DA SEQUÊNCIA DE MEMÓRIA 🧠 ===")
print("✨ Memorize a sequência e digite-a novamente! ✨")
print("\nRegras:")
print("- Observe os números aparecerem um por um")
print("- Depois que a sequência for mostrada, digite-a na ordem correta")
print("- A cada rodada, um novo número é adicionado à sequência")
print("- Até onde você consegue chegar? 🏆\n")

input("Pressione Enter para começar...")

sequencia = []
rodada_atual = 1
fim_de_jogo = False

while not fim_de_jogo:
    sequencia.append(random.randint(1, 9))

    limpar_tela()
    print(f"\n=== Rodada {rodada_atual} ===")
    print(f"Memorize esta sequência de {len(sequencia)} números:")

    for numero in sequencia:
        time.sleep(0.7)
        print(f"\n{numero}")
        time.sleep(0.7)
        limpar_tela()

    print(
        "\nAgora repita a sequência digitando cada número, "
        "separado por espaços:"
    )

    resposta_jogador = input("> ")

    # "3 6 1" => ["3", "6", "1"] => [3, 6, 1]

    try:
        sequencia_jogador = [
            int(numero) for numero in resposta_jogador.split()
        ]

    except ValueError:
        print("❌ Digite apenas números!")
        fim_de_jogo = True
        continue

    if sequencia_jogador == sequencia:
        print(
            f"🎉 Parabéns! Você memorizou todos os "
            f"{len(sequencia)} números!"
        )

        rodada_atual += 1
        time.sleep(2)

    else:
        print(
            f"😭 Fim de jogo! Você chegou até a rodada "
            f"{rodada_atual - 1}!"
        )

        print(
            f"A sequência correta era: "
            f"{' '.join(str(numero) for numero in sequencia)}"
        )

        fim_de_jogo = True

    if fim_de_jogo:
        jogar_novamente = input(
            "\nJogar novamente? (sim/não): "
        ).lower()

        if jogar_novamente.startswith("s"):
            sequencia = []
            rodada_atual = 1
            fim_de_jogo = False

        else:
            print("Obrigado por jogar! 👋")