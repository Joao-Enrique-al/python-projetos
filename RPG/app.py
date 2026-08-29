import time
import random


# Status do jogador
jogador = {
    "nome": "",
    "vida": 100,
    "ouro": 50,
    "itens": []
}


# Locais do jogo
locais = {
    "cidade": {
        "descricao": "Uma cidade movimentada, com lojas e pessoas amigáveis.",
        "opcoes": ["loja", "floresta", "descansar"]
    },
    "floresta": {
        "descricao": "Uma floresta escura com sons estranhos e tesouros escondidos.",
        "opcoes": ["explorar", "voltar para a cidade", "acampamento"]
    },
    "loja": {
        "descricao": "Uma pequena loja com vários itens à venda.",
        "opcoes": [
            "comprar poção de vida (20 ouro)",
            "comprar espada (50 ouro)",
            "voltar para a cidade"
        ]
    }
}


# Itens e seus efeitos
itens = {
    "poção de vida": {
        "vida": 30,
        "preco": 20
    },
    "espada": {
        "dano": 10,
        "preco": 50
    }
}


# Inimigos que podem ser encontrados
inimigos = [
    {
        "nome": "Goblin",
        "vida": 30,
        "dano": 5,
        "ouro": 15
    },
    {
        "nome": "Lobo",
        "vida": 20,
        "dano": 7,
        "ouro": 10
    },
    {
        "nome": "Bandido",
        "vida": 40,
        "dano": 8,
        "ouro": 25
    }
]


def escrever_lentamente(texto):
    for caractere in texto:
        print(caractere, end="", flush=True)
        time.sleep(0.02)

    print()


def mostrar_status():
    print("\n" + "=" * 40)

    print(
        f"👤 Nome: {jogador['nome']} | "
        f"❤️ Vida: {jogador['vida']} | "
        f"💰 Ouro: {jogador['ouro']}"
    )

    if jogador["itens"]:
        print(f"🎒 Itens: {', '.join(jogador['itens'])}")

    print("=" * 40)


def cidade():
    escrever_lentamente("\n🏠 Você está na cidade.")
    escrever_lentamente(locais["cidade"]["descricao"])

    while True:
        mostrar_status()

        print("\nO que você gostaria de fazer?")
        print("1. 🛒 Ir para a loja")
        print("2. 🌲 Entrar na floresta")
        print("3. 🛏️ Descansar na hospedaria (recupera a vida por 10 de ouro)")
        print("4. 👋 Sair do jogo")

        escolha = input("> ").lower()

        if escolha == "1" or "loja" in escolha:
            loja()

        elif escolha == "2" or "floresta" in escolha:
            floresta()

        elif escolha == "3" or "descansar" in escolha:
            descansar()

        elif escolha == "4" or "sair" in escolha:
            escrever_lentamente("\n👋 Obrigado por jogar! Até logo.")
            exit()

        else:
            print("Não entendi essa opção. Tente novamente!")


def loja():
    escrever_lentamente(
        "\n🛒 Você entra na loja. "
        "O vendedor cumprimenta você."
    )

    escrever_lentamente(locais["loja"]["descricao"])

    while True:
        mostrar_status()

        print("\nO que você gostaria de fazer?")
        print("1. 🧪 Comprar poção de vida (20 de ouro)")
        print("2. ⚔️ Comprar espada (50 de ouro)")
        print("3. 🚶 Voltar para a cidade")

        escolha = input("> ").lower()

        if escolha == "1" or "vida" in escolha or "poção" in escolha:
            comprar_item("poção de vida")

        elif escolha == "2" or "espada" in escolha:
            comprar_item("espada")

        elif (
            escolha == "3"
            or "voltar" in escolha
            or "cidade" in escolha
        ):
            escrever_lentamente(
                "\n🚶 Você sai da loja e volta para a cidade."
            )
            return

        else:
            print("❓ Não entendi. Tente novamente.")


def comprar_item(nome_item):
    item = itens[nome_item]

    # O jogador não pode comprar outra espada,
    # mas pode comprar várias poções de vida.
    if nome_item in jogador["itens"] and nome_item != "poção de vida":
        escrever_lentamente(
            f"\nVocê já possui uma {nome_item}."
        )
        return

    if jogador["ouro"] >= item["preco"]:
        jogador["ouro"] -= item["preco"]

        if nome_item not in jogador["itens"]:
            jogador["itens"].append(nome_item)

        if "vida" in item:
            escrever_lentamente(
                f"\n🧪 Você comprou uma poção de vida! "
                f"Ela pode restaurar {item['vida']} de vida."
            )

        elif "dano" in item:
            escrever_lentamente(
                f"\n✅ Você comprou uma {nome_item}! "
                "Ela ajudará você a derrotar inimigos mais rapidamente."
            )

    else:
        escrever_lentamente(
            "\n❌ Você não tem ouro suficiente para comprar esse item!"
        )


def floresta():
    escrever_lentamente("\n🌲 Você entra na floresta escura...")
    escrever_lentamente(locais["floresta"]["descricao"])

    while True:
        mostrar_status()

        print("\nO que você gostaria de fazer?")
        print("1. 🔍 Explorar mais profundamente (chance de encontrar tesouros ou inimigos)")
        print("2. 🏠 Voltar para a cidade")
        print("3. ⛺ Montar acampamento (recupera 10 de vida)")

        escolha = input("> ").lower()

        if escolha == "1" or "explorar" in escolha:
            explorar()

        elif (
            escolha == "2"
            or "voltar" in escolha
            or "cidade" in escolha
        ):
            escrever_lentamente(
                "\n🚶 Você deixa a floresta e volta para a cidade."
            )
            return

        elif escolha == "3" or "acampamento" in escolha:
            escrever_lentamente(
                "\n⛺ Você monta um acampamento para descansar rapidamente."
            )

            jogador["vida"] = min(jogador["vida"] + 10, 100)

            escrever_lentamente(
                "😌 Você se sente um pouco melhor. (+10 de vida)"
            )

        else:
            print(
                "Não entendi essa opção! "
                "Tente novamente."
            )


def explorar():
    escrever_lentamente(
        "\n🔍 Você avança cada vez mais para dentro da floresta..."
    )

    time.sleep(1)

    # Encontro aleatório:
    # 60% inimigo
    # 30% tesouro
    # 10% nada
    encontro = random.choices(
        ["inimigo", "tesouro", "nada"],
        [60, 30, 10]
    )[0]

    if encontro == "inimigo":
        encontro_inimigo()

    elif encontro == "tesouro":
        encontro_tesouro()

    else:
        escrever_lentamente(
            "🤷 Você explora por algum tempo, "
            "mas não encontra nada interessante."
        )


def encontro_inimigo():
    inimigo = random.choice(inimigos)
    vida_inimigo = inimigo["vida"]

    escrever_lentamente(
        f"\n⚠️ Você encontrou um {inimigo['nome']}!"
    )

    while vida_inimigo > 0 and jogador["vida"] > 0:

        mostrar_status()

        print(
            f"\n👹 Vida do {inimigo['nome']}: "
            f"{vida_inimigo}"
        )

        print("\nO que você fará?")
        print("1. ⚔️ Atacar")
        print("2. 🧪 Usar poção de vida")
        print("3. 🏃 Fugir")

        escolha = input("> ").lower()

        if escolha == "1" or "atacar" in escolha:

            dano_jogador = 5

            if "espada" in jogador["itens"]:
                dano_jogador += itens["espada"]["dano"]

            vida_inimigo -= dano_jogador

            escrever_lentamente(
                f"💥 Você atacou o {inimigo['nome']} "
                f"causando {dano_jogador} de dano!"
            )

            if vida_inimigo <= 0:
                escrever_lentamente(
                    f"🎉 Você derrotou o {inimigo['nome']}!"
                )

                jogador["ouro"] += inimigo["ouro"]

                escrever_lentamente(
                    f"💰 Você encontrou "
                    f"{inimigo['ouro']} de ouro!"
                )

                return

            jogador["vida"] -= inimigo["dano"]

            escrever_lentamente(
                f"😱 O {inimigo['nome']} atacou você "
                f"causando {inimigo['dano']} de dano!"
            )

            if jogador["vida"] <= 0:
                fim_de_jogo()


        elif escolha == "2" or "poção" in escolha:

            if "poção de vida" in jogador["itens"]:

                jogador["itens"].remove("poção de vida")

                jogador["vida"] = min(
                    jogador["vida"]
                    + itens["poção de vida"]["vida"],
                    100
                )

                escrever_lentamente(
                    f"🧪 Você usou uma poção de vida "
                    f"e recuperou "
                    f"{itens['poção de vida']['vida']} de vida!"
                )

            else:
                escrever_lentamente(
                    "❌ Você não possui nenhuma poção de vida!"
                )

                continue

            jogador["vida"] -= inimigo["dano"]

            escrever_lentamente(
                f"😱 O {inimigo['nome']} atacou você "
                f"causando {inimigo['dano']} de dano!"
            )

            if jogador["vida"] <= 0:
                fim_de_jogo()


        elif escolha == "3" or "fugir" in escolha:

            # 50% de chance de escapar
            if random.random() > 0.5:

                escrever_lentamente(
                    "🏃 Você conseguiu escapar!"
                )

                return

            else:

                escrever_lentamente(
                    "😨 Você não conseguiu escapar!"
                )

                jogador["vida"] -= inimigo["dano"]

                escrever_lentamente(
                    f"😱 O {inimigo['nome']} atacou você "
                    f"causando {inimigo['dano']} de dano!"
                )

                if jogador["vida"] <= 0:
                    fim_de_jogo()

        else:
            print("❓ Não entendi. Tente novamente.")


def encontro_tesouro():
    ouro_encontrado = random.randint(10, 30)

    jogador["ouro"] += ouro_encontrado

    # 20% de chance de encontrar uma poção
    if (
        random.random() < 0.2
        and "poção de vida" not in jogador["itens"]
    ):

        jogador["itens"].append("poção de vida")

        escrever_lentamente(
            "\n✨ Você encontrou um baú de tesouro escondido!"
        )

        escrever_lentamente(
            f"🎁 Dentro havia {ouro_encontrado} de ouro "
            "e uma poção de vida!"
        )

    else:

        escrever_lentamente(
            "\n💰 Você encontrou uma pequena bolsa "
            "com algumas moedas!"
        )

        escrever_lentamente(
            f"✨ Você ganhou {ouro_encontrado} de ouro!"
        )


def descansar():

    if jogador["ouro"] >= 10:

        jogador["ouro"] -= 10
        jogador["vida"] = 100

        escrever_lentamente(
            "\n🛏️ Você descansa na hospedaria "
            "e recupera completamente sua vida."
        )

        escrever_lentamente(
            "😊 Custou 10 de ouro, "
            "mas você está completamente recuperado!"
        )

    else:

        escrever_lentamente(
            "\n❌ Você não tem ouro suficiente "
            "para descansar na hospedaria!"
        )


def fim_de_jogo():

    escrever_lentamente(
        "\n💔 Sua vida chegou a 0!"
    )

    escrever_lentamente(
        "☠️ FIM DE JOGO!"
    )

    print(
        f"\n📊 Estatísticas finais: "
        f"{jogador['ouro']} de ouro coletado"
    )

    jogar_novamente = input(
        "\n🔄 Você gostaria de jogar novamente? (sim/não): "
    ).lower()

    if jogar_novamente.startswith("s"):
        iniciar_jogo()

    else:
        escrever_lentamente(
            "\n👋 Obrigado por jogar! Até logo."
        )

        exit()


def iniciar_jogo():

    jogador["vida"] = 100
    jogador["ouro"] = 50
    jogador["itens"] = []

    escrever_lentamente("\n" + "=" * 60)
    escrever_lentamente("🏆 AVENTURA NA FLORESTA 🏆")
    escrever_lentamente("=" * 60)

    escrever_lentamente(
        "🎮 Bem-vindo a um simples jogo de aventura em texto!"
    )

    jogador["nome"] = input(
        "\nQual é o seu nome, aventureiro? "
    )

    escrever_lentamente(
        f"\n🎉 Bem-vindo, {jogador['nome']}! "
        "Sua aventura começa em uma pequena cidade."
    )

    cidade()


iniciar_jogo()