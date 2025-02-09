# Exercícios
# Crie funções que duplicam, triplicam e quadruplicam
# o número recebido como parâmetro.
import os
opcao = int(input("""
[1] - Duplicar,
[2] - Triplicar,
[3] - Quadruplicar
[4] - Sair
Digite a opcão desejada:"""))
#Blocos de codigos
def duplicar(numero):
    return numero * 2
    
def triplicar(numero):
    return numero * 3
    
def quadruplicar(numero):
    return numero * 4
#Multiplicação dos numeros    
if opcao <= 4:
    if opcao == 4:
        print('Você saiu do programa.')
        exit()
    numero = int(input('digite um numero a ser multiplicado: '))
    if opcao == 1:
        print(numero,f"* 2 é igual:",duplicar(numero))
    elif opcao == 2:
        print(numero,f"* 3 é igual:",triplicar(numero))
    elif opcao == 3:
        print(numero,f"* 4 é igual:",quadruplicar(numero))
else:
    os.system('cls')
    print("opção errada")
    
                 