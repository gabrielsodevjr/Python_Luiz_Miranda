"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

entrada = input("Digite um numero INTEIRO: ")

try:
    if int(entrada) % 2 == 0:
        print("Esse numero é par.")
    else:
        print("Esse numero é impar.")
except ValueError:
    print("Entrada invalida, Digite um numero INTEIRO.")

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

horario = input("Ola. Digite o horario atual, ex(22:34): ")
horas = int(horario[0:2])

try:
    if horas >= 0 and horas <= 11:
        print("Bom Dia")
    elif horas >= 12 and horas <= 17:
        print("Boa Tarde")
    elif horas >= 18 and horas <= 23:
        print("Boa Noite")
    else:
        print("Não conheço essa hora")
except ValueError:
    print("Por favor, digite apenas números inteiros")


"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

nome = input("Digite seu primeiro nome: ")
tamanho_nome = len(nome)

if tamanho_nome > 1:
    try:
        if tamanho_nome <= 4:
            print("Seu nome é curto")
        elif tamanho_nome >= 5 and tamanho_nome <= 6:
            print("Seu nome é normal")
        elif tamanho_nome > 6:
            print("Seu nome é muito grande")
    except:
        print("Erro. Digite seu nome usando apenas letras")
else:
    print("Você digitou algo errado, tente novamente")
