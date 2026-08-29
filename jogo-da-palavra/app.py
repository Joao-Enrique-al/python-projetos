import random

print("\n=== 🔤 ADIVINHE A PALAVRA! 🔤 ===")
print("✨ Desembaralhe as letras para descobrir a palavra! ✨")

palavras = ["python", "programação", "jogo", "computador", "diversão", "aprender"]

while True:
    palavra_original = random.choice(palavras)

    # "jogo" => ["j","o","g","o"] => ["o","j","g","o"] => "ojgo"
    letras = list(palavra_original)
    random.shuffle(letras)
    embaralhada = "".join(letras)

    print(f"\n Palavra embaralhada: {embaralhada}")

    palpite = input("🤔 Qual é a palavra?: ").lower()

    if palpite == palavra_original:
        print("🎉 Parabéns! Você ganhou!")

    else:
        print(f"😢 Você errou! A palavra era: {palavra_original}")

    novamente = input("Jogar novamente? (s/n): ").lower()

    if not novamente.startswith("s"):
        print("Até logo! 👋")
        break