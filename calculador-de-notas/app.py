print("📊 CALCULADORA DE NOTAS 📊")
notas = []

while True:
    nota = input("Digite uma nota (ou 'fim'): ")

    if nota.lower() == "fim":
        print("👋 Até logo!")
        break

    notas.append(float(nota))
    media = sum(notas) / len(notas)

    print(f"Média das notas: {media:.1f}")

    if media >= 90:
        print("Nota: A")

    elif media >= 80:
        print("Nota: B")

    elif media >= 70:
        print("Nota: C")

    else:
        print("Nota: D ou F")