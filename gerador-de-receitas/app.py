import random

print("👩‍🍳 GERADOR DE RECEITAS ALEATÓRIAS 👩‍🍳")

proteinas = ["frango", "carne bovina", "tofu", "peixe", "ovos"]
vegetais = ["brócolis", "cenoura", "espinafre", "pimentão", "cogumelos"]
carboidratos = ["arroz", "macarrão", "batatas", "quinoa", "pão"]
metodos = ["assado", "grelhado", "refogado", "tostado", "salteado"]
sabores = ["alho", "limão", "picante", "ervas", "agridoce"]


while True:
    proteina = random.choice(proteinas)
    vegetal = random.choice(vegetais)
    carboidrato = random.choice(carboidratos)
    metodo = random.choice(metodos)
    sabor = random.choice(sabores)

    print(
        f"\nSua receita aleatória: {proteina} {metodo} com {vegetal}, "
        f"{carboidrato} e sabor de {sabor}"
    )

    if not input("\nGerar outra receita? (s/n): ").lower().startswith("s"):
        print("👋 Até logo!")
        break