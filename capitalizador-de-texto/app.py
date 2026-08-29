print("📢 CAPITALIZADOR DE TEXTO 📢")

texto = input("🤷‍♂️ Digite um texto: ")

print("✨ 1. LETRAS MAIÚSCULAS")

print("👀 2. letras minúsculas")

print("🎉 3. Primeira Letra De Cada Palavra")

print("🚀 4. Primeira letra da frase")

escolha = input("Escolha um formato (1-4): ")

if escolha == "1":

    print(texto.upper())

elif escolha == "2":

    print(texto.lower())

elif escolha == "3":

    print(texto.title())

elif escolha == "4":

    print(texto.capitalize())