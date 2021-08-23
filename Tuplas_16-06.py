# TUPLAS

# from random import randint


# tupla = (randint(1,50), randint(1,50), randint(1,50), randint(1,50), randint(1,50))
# print(sorted(tupla))

# print(f'O maior número foi: {max(tupla)}')
# print(f'O menor número foi: {min(tupla)}')



# tupla = (int(input('digite um numero: ')), int(input('digite um numero: ')), int(input('digite um numero: ')), int(input('digite um numero: ')))
# print(tupla)

# print(tupla.count(9))
# print(tupla.index(3))







# LISTAS

# 01 - Dada a lista l = [5, 7, 2, 9, 4, 1, 3], escreva um programa que imprima as seguintes informações:
# a) tamanho da lista.
# b) maior valor da lista.
# c) menor valor da lista.
# d) soma de todos os elementos da lista.
# e) lista em ordem crescente.
# f) lista em ordem decrescente.

l = [5, 7, 2, 9, 4, 1, 3]

print(l)
print(f'a lista tem {len(l)} números\nO maior valor é: {max(l)}\nO menor valor é: {min(l)}\nA soma é: {sum(l)}')
l.sort()
print(l)
l.reverse()
print(l)



