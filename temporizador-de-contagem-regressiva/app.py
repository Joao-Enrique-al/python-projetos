import time

print("\n=== ⏱️ TEMPORIZADOR DE CONTAGEM REGRESSIVA ⏱️ ===")
print("✨ Faça uma contagem regressiva a partir dos segundos escolhidos! ✨")

while True:
    try:
        segundos = int(input("\n🤔 Digite os segundos para iniciar a contagem: "))

        # validar entrada
        if segundos <= 0:
            print("❌ Digite um número positivo.")
            continue

        print(f"⏳ Iniciando contagem regressiva a partir de {segundos} segundos!")

        for i in range(segundos, 0, -1):
            print(f"⏰ {i} segundos restantes...")
            time.sleep(1)

        print("\n🎉 CONTAGEM REGRESSIVA CONCLUÍDA! 🎉")

        novamente = input(
            "\n🔄 Iniciar outra contagem regressiva? (sim/não): "
        ).lower()

        if not novamente.startswith("s"):
            print("Até logo! 👋")
            break

    except ValueError:
        print("❌ Digite um número válido.")