# Faça um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições:

# def voto(ano):
#     from datetime import date
#     atual = date.today().year
#     idade = atual - ano
#     if idade < 16:
#         return f'com {idade} anos o voto é NEGADO'
#     elif 16 <= idade < idade or idade > 70:
#         return f'com {idade} anos o voto é OPCIONAL'
#     else:
#         return f'com {idade} anos o voto é OBRIGATÓRIO'

# nasc = int(input('digite o ano de nascimento: '))
# print(voto(nasc))


# Faça um programa, com uma função que necessite de um parametro. A função retorna o valor de caractere ‘P’, se seu argumento for positivo, e ‘N’, se seu argumento for zero ou negativo.


# def argumento(n):
#     if n > 0:
#         return 'P'
#     else:
#         return 'N'

# n1 = int(input('digite um numero: '))
# print(argumento(n1))



# Faça um programa em Python com uma função que necessite de três parametros, e que forneça:
# A soma desses três parametros através de uma função.
# Seu script também deve fornecer a média dos três números,  através de uma segunda função que chama a primeira.


# def soma(n1, n2, n3):
#     res = n1 + n2 + n3
#     return res

# def media(soma):
#     med = soma / 3
#     return f'A média é {med:.2f}'

# def menu():
#     nota1 = float(input('Nota 1: '))
#     nota2 = float(input('Nota 2: '))
#     nota3 = float(input('Nota 3: '))
#     somar = soma(nota1, nota2, nota3)
#     print(media(somar))

# menu()


# OU


# def soma(n1, n2, n3):
#     res = n1 + n2 + n3
#     return res

# def media_func():
#     media = soma(float(input('Nota 1: ')), int(input('Nota 2: ')), int(input('Nota 3: ')))/3
#     return media

# print(f'A média é {media_func():.2f}')




