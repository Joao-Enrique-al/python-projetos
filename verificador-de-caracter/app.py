print("📝 VERIFICADOR DE TIPO DE CARACTERE 📝")

caractere = input("Digite um único caractere: ")

if caractere.isalpha():

    print("Isso é uma letra.")

elif caractere.isdigit():

    print("Isso é um número.")

else:

    print("Isso é um caractere especial.")