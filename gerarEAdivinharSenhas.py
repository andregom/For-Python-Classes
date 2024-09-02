import random
import string

def gerar_senha(n, onlyNumbers=True):
    # Define os caracteres possíveis com base na opção onlyNumbers
    if onlyNumbers:
        caracteres = string.digits  # Utiliza string.digits para números
    else:
        caracteres = string.ascii_letters + string.digits  # Utiliza letras e números
    
    # Gera uma senha de n caracteres usando os caracteres definidos
    senha = ''.join(random.choices(caracteres, k=n))
    return senha

def adivinhar_senha(senha):
    tentativa = ''
    while tentativa != senha:
        tentativa = input("Tente adivinhar a senha: ")
        if tentativa == senha:
            print("Parabéns! Você adivinhou a senha!")
        else:
            print("Senha incorreta. Tente novamente.")

def main():
    n = int(input("Digite o número de dígitos para a senha: "))
    onlyNumbers = input("A senha deve conter apenas números? (s/n): ").lower() == 's'
    
    senha = gerar_senha(n, onlyNumbers)
    print("Uma senha foi gerada!")
    adivinhar_senha(senha)

if __name__ == "__main__":
    main()
