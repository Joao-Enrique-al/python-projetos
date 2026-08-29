print("🔤 CONTADOR DE VOGAIS 🔤")

# Sintaxe simples
# while True:
#     texto = input("\nDigite um texto (ou 'sair'): ")

#     if texto.lower() == "sair":
#         print("👋 Até logo!")
#         break

#     contador_vogais = 0

#     for letra in texto.lower():
#         if letra in ["a", "e", "i", "o", "u"]:
#             contador_vogais += 1

#     print(f"Esse texto possui {contador_vogais} vogais!")


# Sintaxe avançada

while True:
    texto = input("\nDigite um texto (ou 'sair'): ")

    if texto.lower() == "sair":
        print("👋 Até logo!")
        break

    vogais = sum(1 for caractere in texto.lower() if caractere in "aeiou")

    print(f"Esse texto possui {vogais} vogais!")