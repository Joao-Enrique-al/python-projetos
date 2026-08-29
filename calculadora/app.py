def adicionar(x, y):
    return x + y


def subtrair(x, y):
    return x - y


def multiplicar(x, y):
    return x * y


def dividir(x, y):
    if y == 0:
        return "Erro! Divisão por zero não é permitida."

    return x / y


def principal():
    print("\n==== 🧮 CALCULADORA SIMPLES 🧮 ====")
    print("Selecione uma operação:")
    print("1. ➕ Adição")
    print("2. ➖ Subtração")
    print("3. ✖️ Multiplicação")
    print("4. ➗ Divisão")

    while True:
        escolha = input("\nDigite sua escolha (1-4): ")

        if escolha not in ["1", "2", "3", "4"]:
            print("Entrada inválida. Digite um número entre 1 e 4.")

        else:
            break

    try:
        numero1 = float(input("Digite o primeiro número: "))
        numero2 = float(input("Digite o segundo número: "))

    except ValueError:
        print("❌ Erro! Digite números válidos!")
        return

    if escolha == "1":
        print(f"\n{numero1} + {numero2} = {adicionar(numero1, numero2)}")

    elif escolha == "2":
        print(f"\n{numero1} - {numero2} = {subtrair(numero1, numero2)}")

    elif escolha == "3":
        print(f"\n{numero1} x {numero2} = {multiplicar(numero1, numero2)}")

    elif escolha == "4":
        print(f"\n{numero1} / {numero2} = {dividir(numero1, numero2)}")

    novamente = input(
        "\nDeseja realizar outro cálculo? (sim/não): "
    ).lower()

    if not novamente.startswith("s"):
        print("Até logo!")
        return

    else:
        principal()


principal()