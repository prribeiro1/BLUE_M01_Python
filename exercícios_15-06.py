#01 - Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos

# menor = 1000
# maior = 0

# for c in range(1,6):
#     n = float(input('Digite seu peso: '))
#     if n > maior:
#         maior = n
#     if n < menor:
#         menor = n

# print(f'O menor peso é {menor}KG e o maior peso é {maior}KG')

# - - - - - - - - - - - - - - - - - - - - -       - - - - - - - - - - - -    - - -  - - - - - - - - - - - - 


#02 - Crie um programa que pergunte ao usuário um número inteiro e faça a tabuada desse número.

# num = int(input('Digite um numero: '))

# for n in range (11):
#     print(f'{num} x {n} = {num*n}')


# - - - - - - - - - - - - - - - - - - - - -       - - - - - - - - - - - -    - - -  - - - - - - - - - - - - 


# 03 - Crie um programa que leia o ano de nascimento de sete pessoas.
# No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

# menor_idade = 0
# maior_idade = 0
# hoje = 2021

# for c in range(1,8):
#     n = int(input('Digite seu ano de nascimento: '))
#     if (hoje - n) >= 18:
#         maior_idade += 1
#     else:
#         menor_idade += 1

# print(f'{maior_idade} pessoas já atingiram a maior idade e {menor_idade} aida não.')



# - - - - - - - - - - - - - - - - - - - - -       - - - - - - - - - - - -    - - -  - - - - - - - - - - - - 




#04 - Desenvolva um programa que leia seis números inteiros e mostre a soma
# apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.
# Mostre também quantos valores pares foram digitados.



# numero_par = 0
# soma = 0

# for c in range (1,7):
#     n = int(input('Digite um número: '))
#     if n % 2 == 0:
#         soma += n
#         numero_par += 1

# print(f'{numero_par} são números pares e a soma deles é {soma}')


# - - - - - - - - - - - - - - - - - - - - -       - - - - - - - - - - - -    - - -  - - - - - - - - - - - - 



# Execute as atividades abaixo, utilizando a estrutura de repetição WHILE:
# 01 - Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso. (utilizar while sem break)




# n1 = int(input('Digite o primeiro número: '))
# n2 = int(input('Digite o segundo número: '))
# d = 0

# while d != 5:
#     print('''[1] somar
# [2] multiplicar
# [3] maior
# [4] novos númeors
# [5] sair do programa''')
#     d = int(input('Digite: '))
#     if d == 1:
#         print(f'A soma é: {n1+n2}')
#     elif d == 2:
#         print(f'A multiplicação é: {n1*n2}')
#     elif d == 3:
#         if n1 > n2:
#             print(f'O maior é: {n1}')
#         else:
#             print('O maior é {n2}')
#     elif d == 4:
#         n1 = int(input('Digite o primeiro número: '))
#         n2 = int(input('Digite o segundo número: '))
#     elif d == 5:
#         print('Sair do programa')
# print('FIM DO PROGRAMA')


# - - - - - - - - - - - - - - - - - - - - -       - - - - - - - - - - - -    - - -  - - - - - - - - - - - - 
