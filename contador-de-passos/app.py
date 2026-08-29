print("🏃 CONTADOR DE PASSOS 🏃")

meta_diaria = int(input("🤷‍♂️ Qual é sua meta diária de passos? "))

passos_atuais = int(input("✨ Quantos passos você deu hoje? "))

restantes = meta_diaria - passos_atuais

if restantes > 0:

    print(f"💪 Você precisa dar mais {restantes} passos para alcançar sua meta!")

else:

    print(
        f"🎉 Parabéns! Você ultrapassou sua meta em {-restantes} passos!"
    )