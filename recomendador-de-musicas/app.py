import random

print("🎶 RECOMENDADOR DE MÚSICAS 🎶")

generos = {

    "rock": ["AC/DC", "Queen", "Led Zeppelin"],

    "pop": ["Taylor Swift", "Ed Sheeran", "Ariana Grande"],

    "hip-hop": ["Kendrick Lamar", "Drake", "J. Cole"],

}

escolha = input("Qual gênero você gosta? (rock/pop/hip-hop): ")

if escolha not in generos:

    print("😭 Desculpe, não conheço esse gênero.")

else:

    print(f"🎵 Você deveria ouvir {random.choice(generos[escolha])}")