# Utilizando os conceitos de Orientação a Objetos (OO) vistos na aula
# anterior, crie um lançador de dados e moedas em que o usuário deve
# escolher o objeto a ser lançado. Não esqueça que os lançamentos são
# feitos de forma randômica

# from random import randint









#01 - Crie um programa que gerencie o aproveitamento de um jogador de futebol. 
# O programa vai ler o nome do jogador e 
# quantas partidas ele jogou. 
# Depois vai ler a quantidade de gols feitos em cada partida.
#  No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

dados = {}
jogador = []
partidas = []


while True:
    jogador = input('Nome do jogador: ')
    partidas = int(input('Quantas partidas jogou? '))

    for c in range(0, partidas):
        c = int(input(f'Fez quantos gols na {c+1}° partida? '))

    

