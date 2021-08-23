# #01 - Crie um programa onde o usuário possa digitar vários valores numéricos e
# cadastre-os em uma lista. Caso o número já esteja lá dentro, ele não será
# adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem
# crescente.

# lista = [] # lista vazia, pois será adicionada quando o usuário digitar
# while True: # while True para rodar infinito

#     num = int(input('digite um numero: ')) # variável com os números que o usuário digitar, 
#     if num not in lista:
#         lista.append(num)

#     resp = input('Quer continuar? [S/N] ').strip().upper()[0] # pergunta se quer continuar pois o while é infinito
#     if resp == 'N':
#         break

# lista.sort()
# print(lista)



# #02 - Crie um programa que vai ler vários números e colocar em uma lista. Depois
# disso, crie duas listas extras que vão conter apenas os valores pares e os valores
# ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas
# geradas.

# lista = []
# lista_par = []
# lista_impar = []
# while True:

#     num = int(input('digite um número: '))
#     lista.append(num)
#     if num % 2 == 0:
#         lista_par.append(num)
#     else:
#         lista_impar.append(num)
#     resp = input('Quer continuar? [S/N] ').strip().upper()[0]
#     if resp == 'N':
#         break

    

# print(lista)
# print(lista_par)
# print(lista_impar)


# Desafio: Faça um programa que ajude um jogador da MEGA SENA a criar
# palpites.O programa vai perguntar quantos jogos serão gerados e vai sortear 6
# números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta


from random import randint

jogos = list()
quant = int(input('quantos jogos quer que eu sorteie? '))

# Esse for vai gerar os jogos
for c in range(1, 60):
    cont = 0
    lista = list()
# esse WHILE vai gerar os números dentro dos jogos
    while True:
        num = randint(1,60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])

for i, l in enumerate(jogos):
    print(f'jogo {i+1}: {l}')

# (Nesse exercício teve um laço dentro do outro (for e while), porque precisava de uma lista dentro da outra)

    




