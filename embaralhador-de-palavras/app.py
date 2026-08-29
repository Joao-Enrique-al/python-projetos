import random

print("🔤 EMBARALHADOR DE PALAVRAS 🔤")

while True:
    palavra = input("\nDigite uma palavra para embaralhar (ou 'sair'): ")

    if palavra.lower() == "sair":
        print("👋 Até logo!")
        break

    # "everyone" => ["e", "v", "e", "r", "y", "o", "n", "e"]
    # shuffle => ["y", "v", "e", "r", "e", "o", "n", "e"]
    # join => "yvereone"

    letras = list(palavra)
    random.shuffle(letras)

    print(f"Embaralhado: {''.join(letras)}")