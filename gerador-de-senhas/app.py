import random
import string


def gerar_senha(
    tamanho,
    usar_minusculas,
    usar_maiusculas,
    usar_numeros,
    usar_especiais
):
    caracteres = ""

    if usar_minusculas:
        caracteres += string.ascii_lowercase
        # caracteres = "abcdefghijklmnopqrstuvwxyz"

    if usar_maiusculas:
        caracteres += string.ascii_uppercase
        # caracteres = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

    if usar_numeros:
        caracteres += string.digits
        # caracteres = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

    if usar_especiais:
        caracteres += string.punctuation

    if not caracteres:
        print(
            "⚠️ Ops! Nenhum tipo de caractere foi selecionado. "
            "Usando letras minúsculas por padrão!"
        )

        caracteres = string.ascii_lowercase

    senha = ""

    for _ in range(tamanho):
        senha += random.choice(caracteres)

    return senha


def verificar_forca_senha(senha):
    pontuacao = min(len(senha) / 16, 1.0)

    possui_minuscula = any(
        caractere.islower() for caractere in senha
    )

    possui_maiuscula = any(
        caractere.isupper() for caractere in senha
    )

    possui_numero = any(
        caractere.isdigit() for caractere in senha
    )

    possui_especial = any(
        caractere in string.punctuation for caractere in senha
    )

    variedade = (
        possui_minuscula
        + possui_maiuscula
        + possui_numero
        + possui_especial
    ) / 4.0

    pontuacao_final = (
        pontuacao * 0.6
    ) + (
        variedade * 0.4
    )

    if pontuacao_final >= 0.8:
        return "🔥 ULTRA FORTE 🔥"

    elif pontuacao_final >= 0.6:
        return "💪 FORTE 💪"

    elif pontuacao_final >= 0.4:
        return "👍 RAZOÁVEL 👍"

    else:
        return "😬 PRECISA MELHORAR 😬"


def obter_resposta_sim_nao(pergunta):
    while True:
        resposta = input(
            pergunta + "(s/n): "
        ).lower()

        if resposta in ["sim", "s"]:
            return True

        elif resposta in ["não", "nao", "n"]:
            return False

        else:
            print(
                "Não entendi! "
                "Digite 's' para sim ou 'n' para não."
            )


def principal():
    print("\n ==== 🔐 GERADOR DE SENHAS 🔐 ====")
    print(
        "✨ Crie senhas superfortes e seguras "
        "com facilidade! ✨"
    )

    while True:
        try:
            tamanho = int(
                input("\nDigite o tamanho da senha (8-30): ")
            )

            if 8 <= tamanho <= 30:
                break

            else:
                print(
                    "⚠️ Escolha um tamanho entre 8 e 30!"
                )

        except ValueError:
            print(
                "❌ Ops! Digite um número, "
                "como 12 ou 16."
            )

    print("\nVamos personalizar sua senha! 🛠️")

    usar_minusculas = obter_resposta_sim_nao(
        "Incluir letras minúsculas (a-z)? "
    )

    usar_maiusculas = obter_resposta_sim_nao(
        "Incluir letras maiúsculas (A-Z)? "
    )

    usar_numeros = obter_resposta_sim_nao(
        "Incluir números (0-9)? "
    )

    usar_especiais = obter_resposta_sim_nao(
        "Incluir caracteres especiais (!@$#%)? "
    )

    print(
        "\n🧚 Gerando sua senha mágica... 🧚"
    )

    senha = gerar_senha(
        tamanho,
        usar_minusculas,
        usar_maiusculas,
        usar_numeros,
        usar_especiais
    )

    print("\n==== SUA NOVA SENHA 🎉 ====")
    print(f"🔑 {senha}")

    forca = verificar_forca_senha(senha)

    print(f"💪 Força: {forca}")

    print("\n📝===== DICAS PARA SENHAS =====📝")
    print(
        "🚫 Nunca use a mesma senha em várias contas"
    )

    print(
        "🗄️ Considere usar um gerenciador de senhas"
    )

    print(
        "🔄 Altere senhas importantes periodicamente"
    )

    print(
        "🛡️ Mesmo senhas fortes precisam ser mantidas em segredo!"
    )

    if obter_resposta_sim_nao(
        "\nGostaria de criar outra senha incrível? "
    ):
        principal()

    else:
        print(
            "\n🎉 Obrigado por usar o "
            "Super Gerador de Senhas! "
            "Mantenha-se seguro! 🛡️"
        )


principal()