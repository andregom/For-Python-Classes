import random

def adivinhar_numero():
    # Gera um número aleatório entre 1 e 100
    numero_secreto = random.randint(1, 100)
    tentativa = None

    print("Estou pensando em um número entre 1 e 100. Tente adivinhar!")

    # Continua pedindo ao usuário até que ele adivinhe corretamente
    while tentativa != numero_secreto:
        tentativa = int(input("Digite seu palpite: "))

        if tentativa < numero_secreto:
            print("Muito baixo. Tente novamente.")
        elif tentativa > numero_secreto:
            print("Muito alto. Tente novamente.")
        else:
            print("Parabéns! Você adivinhou o número.")

if __name__ == "__main__":
    adivinhar_numero()
