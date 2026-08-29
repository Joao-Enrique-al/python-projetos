import random

primeiras_partes = ["Céu", "Estrela", "Lua", "Sol", "Fogo", "Gelo"]

ultimas_partes = [
    "cavaleiro",
    "andarilho",
    "caçador",
    "explorador",
    "dançarino",
    "guardião",
    "cantor"
]

print("✨ GERADOR DE NOMES FANTÁSTICOS ✨")

quantidade = int(input("Quantos nomes você deseja gerar? "))

for _ in range(quantidade):

    primeiro_nome = random.choice(primeiras_partes)

    ultimo_nome = random.choice(ultimas_partes)

    print(f"{primeiro_nome}{ultimo_nome}")