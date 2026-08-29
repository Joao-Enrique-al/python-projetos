import random

print("🎮 Bem-vindo ao Jogo de Adivinhação de Números! 🎮")
print("🤔 Estou pensando em um número entre 1 e 100. Você tem 10 tentativas. 🔢")

jogando = True

while jogando:
    numero_secreto = random.randint(1, 100)
    tentativas = 0
    max_tentativas = 10

    fim_de_jogo = False

    while tentativas < max_tentativas and not fim_de_jogo:
        try:
            palpite = int(
                input(
                    f"🎯 Tentativa {tentativas + 1}/{max_tentativas}. "
                    "Digite seu palpite: "
                )
            )

        except ValueError:
            print("❌ Digite um número válido")
            continue

        tentativas += 1

        if palpite < numero_secreto:
            print("📉 Muito baixo! Tente um número maior! ⬆️")

        elif palpite > numero_secreto:
            print("📈 Muito alto! Tente um número menor! ⬇️")

        else:
            print(
                f"🎉 Parabéns! Você acertou o número {numero_secreto} "
                f"em {tentativas} tentativas!"
            )
            fim_de_jogo = True

        if tentativas < max_tentativas and not fim_de_jogo:
            print(
                f"⏳ Você ainda tem {max_tentativas - tentativas} "
                "tentativas restantes!"
            )

    if not fim_de_jogo:
        print(f"😭 Fim de jogo! O número era {numero_secreto}")

    jogar_novamente = input(
        "🔄 Você gostaria de jogar novamente? (sim/não): "
    ).lower()

    if jogar_novamente.startswith("s"):
        print("Novo jogo começando...\n")

    else:
        print("Até logo! 👋")
        jogando = False