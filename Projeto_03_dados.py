# Utilizando os conceitos aprendidos até dicionários, crie um programa onde 4 
# jogadores joguem um dado e tenham resultados aleatórios.
# O programa tem que:
# • Perguntar quantas rodadas você quer fazer; 
# • Guardar os resultados dos dados em um dicionário. 
# • Ordenar esse dicionário, sabendo que o vencedor tirou o maior número 
# no dado.
# • Mostrar no final qual jogador ganhou mais rodadas e foi o grande 
# campeão.

from random import randint # função da biblioteca random capaz de gerar números aleatórios
from time import sleep # função da biblioteca time que serve para adicionar um atraso de tempo ao seu código
from operator import itemgetter # função que serve para ordenar itens

print('-=' * 25)
print('SERÁ QUE VOCÊS ESTâO COM SORTE? JOGUEM SEUS DADOS!')
print('-=' * 25)
print()
sleep(1.5)
print("""
 _____
|     |
|  X  |
|     |
 -----""")
sleep(1.5)

print("""
 _____
|   X |
|     |
| X   |
 -----""")
sleep(1.5)

print(""" 
 _____
|   X |
|  X  |
| X   |
 -----""")
sleep(1.5)
 
print("""
 _____
|X   X|
|     |
|X   X|
 -----""")
sleep(1.5)

print(""" 
 _____
|X   X|
|  X  |
|X   X|
 -----""")
sleep(1.5)

print("""
 _____  
|X X X|
|     |
|X X X|
 ----- """)

quant = int(input('Quantas rodadas serão? ')) # variável para a quantidade de rodadas

jogador1 = input('Qual o nome do 1° jogador? ') # variáveis que irão receber os nomes dos jogadores
jogador2 = input('Qual o nome do 2° jogador? ')
jogador3 = input('Qual o nome do 3° jogador? ')
jogador4 = input('Qual o nome do 4° jogador? ')

vit_1 = vit_2 = vit_3 = vit_4 = 0 # variáveis que servirão para contar a vitória de cada jogador

jogadores = {}  # dicionário que irá receber os jogadores e os números dos dados (aleatórios)

lista = [] # lista que irá receber o dicionário

print()


for c in range(quant): # FOR usado para rodar a quantidade de vezes que o usuário pré estabeleceu
  jogadores = {jogador1: randint(1, 6), jogador2: randint(1, 6), jogador3: randint(1, 6), jogador4: randint(1, 6)}
  lista = sorted(jogadores.items(), key=itemgetter(1), reverse=True) # dicionário sendo ordenado em ordem decrescente para ser adicionado na lista

  sleep(1.5)
  for c, v in lista: # FOR usado para mostrar o nome do jogador (c) e o número do dado (v)
    print(f'{c} tirou o número {v}')
    sleep(1.5)

  # IF usado para mostrar o vencedor de cada partida e adicionar "1 ponto" a cada vitória
  if jogadores[jogador1] >= jogadores[jogador2] and jogadores[jogador1] >= jogadores[jogador3] and jogadores[jogador1] >= jogadores[jogador4]:
    print()
    print(f'O vencedor(a) dessa rodada foi: {jogador1}')
    vit_1 += 1
    sleep(1.5)
    print()
  if jogadores[jogador2] >= jogadores[jogador1] and jogadores[jogador2] >= jogadores[jogador3] and jogadores[jogador2] >= jogadores[jogador4]:
    print()
    print(f'O (A) vencedor(a) dessa rodada foi: {jogador2}')
    vit_2 += 1
    sleep(1.5)
    print()
  if jogadores[jogador3] >= jogadores[jogador1] and jogadores[jogador3] >= jogadores[jogador2] and jogadores[jogador3] >= jogadores[jogador4]:
    print()
    print(f'O (A) vencedor(a) dessa rodada foi: {jogador3}')
    vit_3 += 1
    sleep(1.5)
    print()
  if jogadores[jogador4] >= jogadores[jogador1] and jogadores[jogador4] >= jogadores[jogador2] and jogadores[jogador4] >= jogadores[jogador3]:
    print()
    print(f'O (A) vencedor(a) dessa rodada foi: {jogador4}')
    vit_4 += 1
    sleep(1.5)
    print()


print(f'{jogador1} venceu {vit_1} partida(s)\n{jogador2} venceu {vit_2} partida(s)\n{jogador3} venceu {vit_3} partida(s)\n{jogador4} venceu {vit_4} partida(s)\n') # imprime quantas rodadas cada jogador venceu
  
sleep(1.5)
# IF usado para comparar as vitórias de cada jogador para poder mostrar o(s) grande vencedor
if vit_1 >= vit_2 and vit_1 >= vit_3 and vit_1 >= vit_4:
  print('O grande vencedor é:...')
  sleep(2)
  print(f'{jogador1}! Parabéns!!!')
  print()
if vit_2 >= vit_1 and vit_2 >= vit_3 and vit_2 >= vit_4:
  print('O(A) grande vencedor(a) é:...')
  sleep(2)
  print(f'{jogador2}! Parabéns!!!')
  print()
if vit_3 >= vit_1 and vit_3 >= vit_2 and vit_3 >= vit_4:
  print('O(A) grande vencedor(a) é:...')
  sleep(2)
  print(f'{jogador3}! Parabéns!!!')
  print()
if vit_4 >= vit_1 and vit_4 >= vit_2 and vit_4 >= vit_3:
  print('O(A) grande vencedor(a) é:...')
  sleep(2)
  print(f'{jogador4}! Parabéns!!!')
