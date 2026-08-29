import requests


def principal():
    print("\n✨ CONVERSOR DE MOEDAS ✨")

    print("🔄 Obtendo taxas de câmbio...")

    try:
        resposta = requests.get(
            "https://open.er-api.com/v6/latest/USD"
        )

        taxas = resposta.json()["rates"]

        print("✅ Taxas obtidas com sucesso!")

    except:
        print("❌ Erro: Não foi possível conectar à API de taxas de câmbio.")
        return

    print("\n💼 Populares: USD EUR GBP JPY CAD AUD CNY INR")

    while True:
        print("\n💸 Digite os dados:")

        moeda_origem = input(
            "Código da moeda de origem (ex: USD): "
        ).upper()

        if moeda_origem not in taxas:
            print(f"❌ Código inválido: {moeda_origem}")
            continue

        moeda_destino = input(
            "Código da moeda de destino (ex: EUR): "
        ).upper()

        if moeda_destino not in taxas:
            print(f"❌ Código inválido: {moeda_destino}")
            continue

        try:
            valor = float(
                input(f"Valor em {moeda_origem}: ")
            )

        except:
            print("❌ Digite um número válido.")
            continue

        valor_em_usd = valor / taxas[moeda_origem]

        resultado = valor_em_usd * taxas[moeda_destino]

        print(
            f"\n💰 Resultado: {valor} {moeda_origem} = "
            f"{resultado:.2f} {moeda_destino}"
        )

        print(
            f"Taxa: 1 {moeda_origem} = "
            f"{taxas[moeda_destino] / taxas[moeda_origem]:.4f} "
            f"{moeda_destino}"
        )

        if not input(
            "\nConverter novamente? (s/n): "
        ).lower().startswith("s"):

            print("👋 Obrigado por usar o conversor!")
            break


principal()