"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""
cpf = '74682489070'
cpf2 = '74642489070'
nove_digitos = cpf[:9]
contador_regressivo = 10
resultado = 0

print(nove_digitos)
for digito in nove_digitos:
    resultado += int(digito) * contador_regressivo
    contador_regressivo -= 1
print(resultado)

resultado10 = resultado * 10
print(f'resultado x 10:',resultado10)

restoresultado = resultado10 % 11
print(f'resultado da divisão por 11:',restoresultado)
if restoresultado > 11:
    resultado0 = 0
    print(f'se o numero anterior for maior que 9 = 0:',resultado0)
else:
    print(f'se o numero anterior for maior que 9 = 0:',restoresultado)

numero = 0
print('________ _________ __________')
for numero in cpf:
    contador = int(numero) + 1
    pdigito = cpf[contador] == cpf2[contador]
    print(f'cpf1:',cpf[contador],'| cpf2',cpf2[contador],' | é igual?:',pdigito)    
print('________ _________ __________')