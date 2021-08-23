# #01 - Crie um programa que declare uma matriz de dimensão 3×3 e preencha com valores lidos pelo teclado.
#  No final, mostre a matriz na tela, com essa formatação:

# [  1  ][  2  ][  3  ]
# [  4  ][  5  ][  6  ]
# [  7  ][  8  ][  9  ] 

# matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# #02 - Aprimore o desafio anterior, mostrando no final:
#    A) A soma de todos os valores pares digitados.
#    B) A soma dos valores da terceira coluna. 
#    C) O maior valor da segunda linha.


lista1 = [[[int(input('digite um número: '))], [int(input('digite um número: '))], [int(input('digite um número: '))]]]
lista2 = [[int(input('digite um número: '))], [int(input('digite um número: '))], [int(input('digite um número: '))]]
lista3 = [[int(input('digite um número: '))], [int(input('digite um número: '))], [int(input('digite um número: '))]]
matriz = [lista1, lista2, lista3]









#03 - Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista, depois do dado inserido,
#  pergunte ao usuário se ele quer continuar, se ele não quiser pare o programa. No final mostre:

   # Quantas pessoas foram cadastradas
   # Mostre o maior peso
   # Mostre o menor peso


# dados = []
# menor_peso = 10000
# maior_peso = 0
# pessoas_cadastradas = 0


# while True:
#     pessoas = input('Digite seu nome: ')
#     dados.append(pessoas)
#     pessoas_cadastradas += 1
#     peso = float(input('Digite seu peso: '))
#     dados.append(peso)

#     if peso > maior_peso:
#         maior_peso = peso
#     if peso < menor_peso:
#         menor_peso = peso

#     resp = (input('Deseja continuar? [S/N] ')).strip().upper()[0]
#     if resp == 'N':
#         break

# print()
# print(f'Foram cadastradas {pessoas_cadastradas} pessoas.\nO maior peso é: {maior_peso}.\nO menor peso é {menor_peso}.')


# USAR O MAX E MIN PRO PESO