import random
import time

# pares de palavras => (palavra: palavras relacionadas)
pares_de_palavras = {
    "céu": ["azul", "nuvem", "pássaro", "voar", "sol"],
    "água": ["beber", "oceano", "nadar", "peixe", "barco"],
    "comida": ["comer", "cozinhar", "saboroso", "refeição", "restaurante"],
    "música": ["canção", "dançar", "ouvir", "banda", "ritmo"],
    "livro": ["ler", "história", "página", "autor", "biblioteca"],
    "árvore": ["folha", "verde", "floresta", "madeira", "sombra"],
    "carro": ["dirigir", "estrada", "roda", "viajar", "velocidade"],
    "cachorro": ["animal", "latir", "passear", "leal", "filhote"]
}

print("\n=== 🔄 JOGO DE ASSOCIAÇÃO DE PALAVRAS 🔄 ===")
print("✨ Responda rapidamente com uma palavra relacionada! ✨")

pontuacao = 0
rodadas = 0

while True:
    # Seleciona uma palavra aleatória
    palavra = random.choice(list(pares_de_palavras.keys()))
    palavras_relacionadas = pares_de_palavras[palavra]

    print(f"\n🔤 Palavra: {palavra.upper()}")
    print("Rápido! Digite uma palavra relacionada a esta palavra!")

    # Cronometra o tempo de resposta do jogador
    inicio = time.time()

    # Se o usuário digitar "  olá  ", será convertido para "olá"
    resposta = input("> ").lower().strip()

    tempo_resposta = time.time() - inicio

    print("Tempo de resposta:", tempo_resposta)

    # Verifica se a resposta está relacionada
    if resposta in palavras_relacionadas:
        pontos = max(1, 5 - int(tempo_resposta))
        pontuacao += pontos

        print(
            f"✅ Boa associação! +{pontos} pontos "
            f"(respondido em {tempo_resposta:.1f}s)"
        )

    else:
        print(
            f"❌ Não é uma associação comum. "
            f"Palavras relacionadas: {', '.join(palavras_relacionadas)}"
        )

    rodadas += 1

    print(f"Pontuação: {pontuacao}/{rodadas * 5} pontos possíveis")

    # Pergunta se o jogador quer continuar
    if input("\n🔄 Jogar novamente? (sim/não): ").lower().startswith("n"):
        print(
            f"Pontuação final: {pontuacao}. "
            "Obrigado por jogar! 👋"
        )
        break