print("🔄 GERADOR DE NOME AO CONTRÁRIO 🔄")

while True:
    nome = input("\nDigite um nome: ")

    if not nome:
        break

    nome_invertido = nome[::-1]

    print(f"Seu nome ao contrário é: {nome_invertido}")
    print(f"Em um universo paralelo, te chamam de {nome_invertido.title()}")

    resposta = input("\nTentar outro nome? (s/n): ")

    if resposta != "s":
        break