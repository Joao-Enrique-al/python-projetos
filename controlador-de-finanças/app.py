import os
import datetime


ARQUIVO_DADOS = "minhas_financas.txt"


def adicionar_transacao():
    print("\n💰 ADICIONAR TRANSAÇÃO 💰")

    while True:
        tipo_transacao = input(
            "➕ Receita ou ➖ Despesa? (r/d): "
        ).lower()

        if tipo_transacao in ["r", "d"]:
            break

        print("❌ Digite 'r' para receita ou 'd' para despesa.")

    valor = input("💵 Digite o valor: R$")
    categoria = input("🏷️ Digite a categoria: ")
    descricao = input("📝 Digite a descrição: ")

    hoje = datetime.datetime.now().strftime("%Y-%m-%d")

    simbolo = "+" if tipo_transacao == "r" else "-"

    # Abre o arquivo no modo "append" ("a").
    # Isso adiciona novos dados ao final do arquivo
    # sem apagar os dados existentes.
    #
    # O "with" é uma forma segura de trabalhar com arquivos,
    # pois ele fecha o arquivo automaticamente quando termina.

    with open(ARQUIVO_DADOS, "a") as arquivo:
        arquivo.write(
            f"{hoje}|{simbolo}{valor}|{categoria}|{descricao}\n"
        )

    print("✅ Transação adicionada com sucesso!")


def visualizar_transacoes():
    if not os.path.exists(ARQUIVO_DADOS):
        print("Nenhuma transação encontrada.")
        return

    print("\n📋 TRANSAÇÕES 📋")
    print("-" * 60)

    print("DATA          VALOR       CATEGORIA       DESCRIÇÃO")
    print("-" * 60)

    with open(ARQUIVO_DADOS, "r") as arquivo:
        for linha in arquivo:
            partes = linha.strip().split("|")

            data = partes[0]
            valor = partes[1]
            categoria = partes[2]
            descricao = partes[3]

            emoji = "💰" if valor.startswith("+") else "💸"

            print(
                f"{data}    {emoji} {valor}    "
                f"{categoria}    {descricao}"
            )


def obter_resumo():
    if not os.path.exists(ARQUIVO_DADOS):
        print("\n📭 Nenhuma transação encontrada.")
        return

    total_receitas = 0
    total_despesas = 0

    with open(ARQUIVO_DADOS, "r") as arquivo:
        for linha in arquivo:
            partes = linha.strip().split("|")

            valor = partes[1]

            if valor.startswith("+"):
                total_receitas += float(valor[1:])

            else:
                total_despesas += float(valor[1:])

    saldo = total_receitas - total_despesas

    print("\n📊 RESUMO FINANCEIRO 📊")
    print(f"💰 Total de receitas:  R${total_receitas:.2f}")
    print(f"💸 Total de despesas:  R${total_despesas:.2f}")
    print(f"💵 Saldo:              R${saldo:.2f}")


def principal():
    while True:
        print("\n" + "=" * 30)
        print("💰 CONTROLE FINANCEIRO 💰")
        print("=" * 30)

        print("1. 📝 Adicionar transação")
        print("2. 📋 Ver transações")
        print("3. 📊 Resumo financeiro")
        print("4. 🚪 Sair")

        escolha = input("\n🔤 Escolha (1-4): ")

        if escolha == "1":
            adicionar_transacao()

        elif escolha == "2":
            visualizar_transacoes()

        elif escolha == "3":
            obter_resumo()

        elif escolha == "4":
            print("Até logo! 👋")
            break

        else:
            print(
                "❌ Opção inválida. "
                "Escolha uma opção entre 1 e 4."
            )


principal()