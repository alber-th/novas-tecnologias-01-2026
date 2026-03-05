# Desafio 2 - Adivinhe o Número

NUMERO_SECRETO = 42
MAX_TENTATIVAS = 5

tentativa_atual = 1
acertou = False

while tentativa_atual <= MAX_TENTATIVAS and not acertou:
    print(f"Tentativa {tentativa_atual}/{MAX_TENTATIVAS}")
    palpite = int(input("Digite seu palpite: "))

    if palpite < NUMERO_SECRETO:
        print("Muito baixo! Tente maior.\n")
    elif palpite > NUMERO_SECRETO:
        print("Muito alto! Tente menor.\n")
    else:
        print("Correto!")
        acertou = True

    tentativa_atual += 1

if not acertou:
    print(f"Suas tentativas acabaram. Você perdeu! O número era {NUMERO_SECRETO}.")
