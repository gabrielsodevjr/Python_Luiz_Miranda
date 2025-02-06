primeiro_valor = int(input('Digite um valor: '))
segundo_valor = int(input('Digite outro valor: '))

if primeiro_valor > segundo_valor:
    print(f'"{primeiro_valor}" é maior do que o segundo valor= "{segundo_valor}"')
elif segundo_valor > primeiro_valor:
    print(f'"{segundo_valor}" é maior do que o primeiro valor= "{primeiro_valor}"')
else:
    print(f'OS primeiro numero= "{segundo_valor}" é igual ao segundo numero= "{primeiro_valor}"')
