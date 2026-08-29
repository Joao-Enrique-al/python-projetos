import random

print("🎮 JOGO DE CARA OU COROA 🎮")
print("Adivinhe cara ou coroa ✨")

while True:
    palpite = input("\nDigite seu palpite (cara/coroa): ").lower()

    if palpite != "cara" and palpite != "coroa":
        print("❌ Digite 'cara' ou 'coroa' ❌")
        continue  # volta para o início do loop

    lancamento = random.choice(["cara", "coroa"])

    print(f"\n🪙 A moeda caiu em {lancamento}")

    if palpite == lancamento:
        print("Você ganhou! Você acertou. 🎉")
    else:
        print("😢 Você errou. Tente novamente! 🍀")

    novamente = input("\n🔄 Jogar novamente? (sim/não): ").lower()

    if not novamente.startswith("s"):
        print("Até logo!")
        break