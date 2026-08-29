def contar_palavras(texto):
    palavras = texto.split()
    return len(palavras)


def contar_caracteres(texto, incluir_espacos):
    if incluir_espacos:
        return len(texto)
    else:
        return len(texto.replace(" ", ""))


def contar_frases(texto):
    # Contagem básica de frases: pontos, exclamações e interrogações
    finais_de_frase = [".", "!", "?"]
    contador = 0

    for caractere in texto:
        if caractere in finais_de_frase:
            contador += 1

    # Tratando o caso em que não há pontuação
    if contador == 0 and texto.strip():
        contador = 1

    return contador


def analisar_texto(texto):
    quantidade_palavras = contar_palavras(texto)
    caracteres_com_espacos = contar_caracteres(texto, True)
    caracteres_sem_espacos = contar_caracteres(texto, False)
    quantidade_frases = contar_frases(texto)

    if quantidade_frases > 0:
        palavras_por_frase = quantidade_palavras / quantidade_frases
    else:
        palavras_por_frase = 0

    if quantidade_palavras > 0:
        caracteres_por_palavra = (
            caracteres_com_espacos / quantidade_palavras
        )
    else:
        caracteres_por_palavra = 0

    print("\n===== 📊 RESULTADOS DA ANÁLISE DO TEXTO 📊 =====")
    print(f"• 📝 Palavras: {quantidade_palavras}")
    print(
        f"• 🔤 Caracteres (com espaços): "
        f"{caracteres_com_espacos}"
    )
    print(
        f"• 🔡 Caracteres (sem espaços): "
        f"{caracteres_sem_espacos}"
    )
    print(f"• 📃 Frases: {quantidade_frases}")
    print(
        f"• 📏 Média de palavras por frase: "
        f"{palavras_por_frase:.1f}"
    )
    print(
        f"• 📐 Média de caracteres por palavra: "
        f"{caracteres_por_palavra:.1f}"
    )

    # Velocidade média de leitura: 225 palavras por minuto
    tempo_leitura_minutos = quantidade_palavras / 225

    if tempo_leitura_minutos < 1:
        tempo_leitura_segundos = tempo_leitura_minutos * 60

        print(
            f"• ⏱️ Tempo estimado de leitura: "
            f"{tempo_leitura_segundos:.0f} segundos"
        )

    else:
        print(
            f"• ⏱️ Tempo estimado de leitura: "
            f"{tempo_leitura_minutos:.1f} minutos"
        )


def principal():
    print("\n==== 📝 CONTADOR DE PALAVRAS 📝 ====")
    print(
        "Conte palavras, caracteres e frases "
        "no seu texto ✨"
    )

    while True:
        print("\nEscolha uma opção:")
        print("1. 📄 Digitar texto para analisar")
        print("2. 🚪 Sair")

        escolha = input("\nSua escolha (1/2): ")

        if escolha == "1":
            print(
                "\nDigite ou cole seu texto abaixo "
                "(pressione Enter duas vezes para finalizar):"
            )

            linhas = []

            while True:
                linha = input()

                if not linha and linhas and not linhas[-1]:
                    break

                linhas.append(linha)

            texto = "\n".join(linhas)

            if not texto.strip():
                print(
                    "❌ Nenhum texto foi fornecido. "
                    "Tente novamente."
                )
                continue

            analisar_texto(texto)

        elif escolha == "2":
            print("Até logo! 👋")
            break

        else:
            print(
                "❌ Opção inválida. "
                "Digite 1 ou 2."
            )


principal()