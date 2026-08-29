print("🎨 MISTURADOR DE CORES 🎨")

misturas_de_cores = {
    ("vermelho", "azul"): "roxo",
    ("vermelho", "amarelo"): "laranja",
    ("azul", "amarelo"): "verde",
    ("azul", "verde"): "verde-azulado",
    ("branco", "vermelho"): "rosa",
    ("vermelho", "verde"): "marrom",
}


while True:
    cor1 = input("\nDigite a primeira cor: ").lower().strip()
    cor2 = input("Digite a segunda cor: ").lower().strip()  # "vermelho   " => "vermelho"

    mistura = None

    if (cor1, cor2) in misturas_de_cores:
        mistura = misturas_de_cores[(cor1, cor2)]

    elif (cor2, cor1) in misturas_de_cores:
        mistura = misturas_de_cores[(cor2, cor1)]

    if mistura:
        print(f"Quando você mistura {cor1} e {cor2}, obtém {mistura}!")

    else:
        print("Não sei qual cor essas duas cores formam quando misturadas.")

    if not input("\nMisturar mais cores? (s/n)").lower().startswith("s"):
        print("Até logo! 👋")
        break