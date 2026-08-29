import random
import time


def chatbot():
    cumprimentos = [
        "Olá! 👋",
        "Oi, amigo! ☺️",
        "Olá! Prazer em conhecer você! 🎉",
        "E aí! 😃"
    ]

    despedidas = [
        "Até logo! 👋",
        "Até mais! 🚀",
        "Tchau, tchau! 😊",
        "Até a próxima! ✨"
    ]

    piadas = [
        "Por que os cientistas não confiam nos átomos? "
        "Porque eles inventam tudo! 🤣",

        "Como se chama um macarrão falso? "
        "Um impostador! 🍝",

        "Por que o espantalho ganhou um prêmio? "
        "Porque ele era excelente em sua área! 🌾",

        "Como se chama um urso sem dentes? "
        "Um ursinho de goma! 🐻"
    ]

    curiosidades = [
        "O mel nunca estraga! Arqueólogos encontraram mel de 3.000 anos "
        "que ainda estava bom! 🍯",

        "Os polvos têm três corações! 🐙",

        "Um dia em Vênus é mais longo do que um ano em Vênus! ☀️",

        "O alfabeto havaiano possui apenas 12 letras! 🏝️"
    ]

    nome_bot = "ChatBot"

    print(f"🤖 {nome_bot} está iniciando...")
    time.sleep(1)

    print(f"""
       🤖 Bem-vindo ao {nome_bot}! 🤖

      Eu posso conversar sobre:
      🎯 'piada' - Ouvir uma piada engraçada
      🧠 'curiosidade' - Aprender algo novo
      🌈 'cor' - Minha cor favorita
      👋 'tchau' - Encerrar nossa conversa
      """)

    conversando = True

    nome_usuario = input("Qual é o seu nome? ").strip()

    print(
        f"🤖 {nome_bot}: Prazer em conhecer você, "
        f"{nome_usuario}! Como posso ajudar hoje?"
    )

    while conversando:
        entrada_usuario = input("😄 Você: ").lower().strip()

        if entrada_usuario in ["oi", "olá", "ola", "e aí", "eai"]:
            print(
                f"🤖 {nome_bot}: "
                f"{random.choice(cumprimentos)}"
            )

        elif "piada" in entrada_usuario:
            print(
                f"🤖 {nome_bot}: "
                f"{random.choice(piadas)}"
            )

        elif "curiosidade" in entrada_usuario:
            print(
                f"🤖 {nome_bot}: "
                f"{random.choice(curiosidades)}"
            )

        elif "cor" in entrada_usuario:
            print(
                f"🤖 {nome_bot}: "
                "Minha cor favorita é azul robô! 🔵 Qual é a sua?"
            )

            cor = input("😄 Você: ").strip()

            print(
                f"🤖 {nome_bot}: "
                f"{cor} é uma ótima cor! 🎨"
            )

        elif entrada_usuario in [
            "tchau",
            "adeus",
            "sair",
            "encerrar"
        ]:
            print(
                f"🤖 {nome_bot}: "
                f"{random.choice(despedidas)}"
            )

            print(
                f"🤖 {nome_bot}: "
                f"Foi divertido conversar com você, {nome_usuario}!"
            )

            conversando = False

        else:
            respostas = [
                "Isso é interessante! Conte-me mais.",
                "Não tenho certeza se entendi. Pode tentar novamente?",
                "Hmm, vamos falar sobre outra coisa. "
                "Tente pedir uma piada ou uma curiosidade!",
                "Bip bop! Meu cérebro robótico está processando isso... 🤔"
            ]

            print(
                f"🤖 {nome_bot}: "
                f"{random.choice(respostas)}"
            )

    print(
        "Obrigado por conversar comigo! "
        "Execute o programa novamente para falar comigo depois! 👋"
    )


chatbot()