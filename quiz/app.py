import random
import time


def exibir_boas_vindas():
    print("\n" + "=" * 50)
    print(
        "🎮 BEM-VINDO AO DESAFIO DEFINITIVO DE QUIZ! 🎮".center(50)
    )
    print("=" * 50)

    print("\n📜 Instruções:")
    print("- Escolha uma categoria do quiz")
    print("- Responda às perguntas de múltipla escolha")
    print("- Cada resposta correta vale 10 pontos")
    print("- Veja sua pontuação final no final do quiz")
    print("- Divirta-se e aprenda algo novo!")


def exibir_categorias():
    print("\n🗂️ Categorias do Quiz:")
    print("1. 🌎 Conhecimentos Gerais")
    print("2. 🎬 Filmes e Séries")
    print("3. 🔬 Ciência e Natureza")
    print("4. 🎮 Jogos")
    print("5. 🎲 Mistura Aleatória (todas as categorias)")


def obter_escolha_usuario():
    while True:
        try:
            escolha = int(
                input("\nSelecione uma categoria (1-5): ")
            )

            if 1 <= escolha <= 5:
                return escolha

            else:
                print(
                    "❌ Digite um número entre 1 e 5."
                )

        except ValueError:
            print("❌ Digite um número válido.")


def carregar_perguntas():
    conhecimentos_gerais = [
        {
            "pergunta": "Qual é a capital da França?",
            "opcoes": [
                "A. Londres",
                "B. Berlim",
                "C. Paris",
                "D. Madri"
            ],
            "resposta": "C"
        },
        {
            "pergunta": "Qual planeta é conhecido como Planeta Vermelho?",
            "opcoes": [
                "A. Vênus",
                "B. Marte",
                "C. Júpiter",
                "D. Saturno"
            ],
            "resposta": "B"
        },
        {
            "pergunta": "Quantos lados possui um hexágono?",
            "opcoes": [
                "A. 5",
                "B. 6",
                "C. 7",
                "D. 8"
            ],
            "resposta": "B"
        },
        {
            "pergunta": "Qual é o maior oceano da Terra?",
            "opcoes": [
                "A. Oceano Atlântico",
                "B. Oceano Índico",
                "C. Oceano Ártico",
                "D. Oceano Pacífico"
            ],
            "resposta": "D"
        },
        {
            "pergunta": "Qual destas não é uma cor primária?",
            "opcoes": [
                "A. Vermelho",
                "B. Azul",
                "C. Verde",
                "D. Amarelo"
            ],
            "resposta": "C"
        }
    ]

    filmes_series = [
        {
            "pergunta": "Quem interpretou o Homem de Ferro no Universo Cinematográfico da Marvel?",
            "opcoes": [
                "A. Chris Evans",
                "B. Robert Downey Jr.",
                "C. Chris Hemsworth",
                "D. Mark Ruffalo"
            ],
            "resposta": "B"
        },
        {
            "pergunta": "Qual série apresenta um professor de química que se torna traficante de drogas?",
            "opcoes": [
                "A. Breaking Bad",
                "B. The Walking Dead",
                "C. Game of Thrones",
                "D. Stranger Things"
            ],
            "resposta": "A"
        },
        {
            "pergunta": "Qual foi o primeiro filme da trilogia original de Star Wars?",
            "opcoes": [
                "A. O Império Contra-Ataca",
                "B. O Retorno de Jedi",
                "C. Uma Nova Esperança",
                "D. A Ameaça Fantasma"
            ],
            "resposta": "C"
        },
        {
            "pergunta": "Qual atriz interpretou Katniss Everdeen em Jogos Vorazes?",
            "opcoes": [
                "A. Emma Watson",
                "B. Jennifer Lawrence",
                "C. Scarlett Johansson",
                "D. Emma Stone"
            ],
            "resposta": "B"
        },
        {
            "pergunta": "Qual filme de animação apresenta um boneco de neve chamado Olaf?",
            "opcoes": [
                "A. Toy Story",
                "B. Shrek",
                "C. Frozen",
                "D. Procurando Nemo"
            ],
            "resposta": "C"
        }
    ]

    ciencia_natureza = [
        {
            "pergunta": "Qual é o símbolo químico do ouro?",
            "opcoes": [
                "A. Go",
                "B. Au",
                "C. Ag",
                "D. Gd"
            ],
            "resposta": "B"
        },
        {
            "pergunta": "Qual animal pode mudar sua cor para se camuflar?",
            "opcoes": [
                "A. Camaleão",
                "B. Elefante",
                "C. Girafa",
                "D. Pinguim"
            ],
            "resposta": "A"
        },
        {
            "pergunta": "Quantos elementos existem atualmente na tabela periódica?",
            "opcoes": [
                "A. 92",
                "B. 100",
                "C. 118",
                "D. 120"
            ],
            "resposta": "C"
        },
        {
            "pergunta": "Qual é o maior órgão do corpo humano?",
            "opcoes": [
                "A. Cérebro",
                "B. Fígado",
                "C. Coração",
                "D. Pele"
            ],
            "resposta": "D"
        },
        {
            "pergunta": "Qual destes não é um tipo de nuvem?",
            "opcoes": [
                "A. Cumulus",
                "B. Stratus",
                "C. Cirrus",
                "D. Núcleo"
            ],
            "resposta": "D"
        }
    ]

    jogos = [
        {
            "pergunta": "Qual jogo apresenta um personagem chamado Mario?",
            "opcoes": [
                "A. Call of Duty",
                "B. Super Mario Bros.",
                "C. Minecraft",
                "D. Fortnite"
            ],
            "resposta": "B"
        },
        {
            "pergunta": "Qual é a cor do fantasma Inky em Pac-Man?",
            "opcoes": [
                "A. Vermelho",
                "B. Rosa",
                "C. Azul",
                "D. Laranja"
            ],
            "resposta": "C"
        },
        {
            "pergunta": "Qual jogo apresenta um personagem chamado Master Chief?",
            "opcoes": [
                "A. Halo",
                "B. God of War",
                "C. The Last of Us",
                "D. Uncharted"
            ],
            "resposta": "A"
        },
        {
            "pergunta": "No Minecraft, qual material é necessário para criar uma tocha?",
            "opcoes": [
                "A. Madeira e ferro",
                "B. Carvão e graveto",
                "C. Pedra e pederneira",
                "D. Ouro e madeira"
            ],
            "resposta": "B"
        },
        {
            "pergunta": "Qual destas não é um tipo de Pokémon?",
            "opcoes": [
                "A. Fogo",
                "B. Água",
                "C. Terra",
                "D. Elétrico"
            ],
            "resposta": "C"
        }
    ]

    return {
        1: {
            "nome": "Conhecimentos Gerais",
            "perguntas": conhecimentos_gerais
        },

        2: {
            "nome": "Filmes e Séries",
            "perguntas": filmes_series
        },

        3: {
            "nome": "Ciência e Natureza",
            "perguntas": ciencia_natureza
        },

        4: {
            "nome": "Jogos",
            "perguntas": jogos
        },

        5: {
            "nome": "Mistura Aleatória",
            "perguntas": (
                conhecimentos_gerais
                + filmes_series
                + ciencia_natureza
                + jogos
            )
        }
    }


def executar_quiz(dados_categoria):
    nome_categoria = dados_categoria["nome"]
    perguntas = dados_categoria["perguntas"]

    random.shuffle(perguntas)

    print(
        f"\n🎯 Iniciando o quiz de {nome_categoria}! 🎯"
    )

    print(
        "Responda cada pergunta digitando a letra "
        "da sua escolha (A, B, C ou D)."
    )

    pontuacao = 0
    respostas_corretas = 0

    for indice, pergunta in enumerate(perguntas):

        print(
            f"\n-------- Pergunta "
            f"{indice + 1}/{len(perguntas)} ---------"
        )

        print(f"? {pergunta['pergunta']}")

        for opcao in pergunta["opcoes"]:
            print(opcao)

        while True:
            resposta_usuario = input(
                "\nSua resposta (A/B/C/D): "
            ).upper()

            if resposta_usuario not in [
                "A",
                "B",
                "C",
                "D"
            ]:
                print(
                    "❌ Digite A, B, C ou D."
                )

            else:
                break

        correta = (
            resposta_usuario == pergunta["resposta"]
        )

        if correta:
            pontuacao += 10
            respostas_corretas += 1

            print("✅ Correto! +10 pontos")

        else:
            print(
                f"❌ Errado! "
                f"A resposta correta é "
                f"{pergunta['resposta']}"
            )

        if indice < len(perguntas) - 1:
            print("\nPróxima pergunta chegando...")
            time.sleep(1.5)

    print("\n" + "=" * 50)
    print(
        "📊 RESULTADO DO QUIZ 📊".center(50)
    )
    print("=" * 50)

    print(f"Categoria: {nome_categoria}")

    print(
        f"Respostas corretas: "
        f"{respostas_corretas}/{len(perguntas)}"
    )

    print(
        f"Pontuação total: "
        f"{pontuacao} pontos"
    )

    porcentagem = (
        pontuacao / (len(perguntas) * 10)
    ) * 100

    if porcentagem == 100:
        print(
            "\n🏆 PONTUAÇÃO PERFEITA! "
            "Você é um mestre dos quizzes! 🏆"
        )

    elif porcentagem >= 80:
        print(
            "\n🌟 EXCELENTE! "
            "Você realmente entende do assunto!"
        )

    elif porcentagem >= 60:
        print(
            "\n😊 BOM TRABALHO! "
            "Você tem um bom conhecimento!"
        )

    elif porcentagem >= 40:
        print(
            "\n🤔 NÃO FOI MAL! "
            "Ainda há espaço para melhorar."
        )

    else:
        print(
            "\n📚 CONTINUE APRENDENDO! "
            "A prática leva à perfeição!"
        )

    return pontuacao


def principal():
    exibir_boas_vindas()

    pontuacao_total = 0
    jogar_novamente = True

    while jogar_novamente:

        exibir_categorias()

        escolha_categoria = obter_escolha_usuario()

        todas_categorias = carregar_perguntas()

        pontuacao = executar_quiz(
            todas_categorias[escolha_categoria]
        )

        pontuacao_total += pontuacao

        novamente = input(
            "\nJogar outra rodada? (sim/não): "
        ).lower()

        while not (
            novamente.startswith("s")
            or novamente.startswith("n")
        ):
            print("Digite sim ou não.")

            novamente = input(
                "Jogar outra rodada? (sim/não): "
            ).lower()

        jogar_novamente = novamente.startswith("s")

    print(
        f"\n🎉 Obrigado por jogar! "
        f"Sua pontuação total em todas as rodadas: "
        f"{pontuacao_total} pontos 🎉"
    )


principal()