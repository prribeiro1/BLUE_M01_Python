import random
from time import sleep

print('-='*17)
print('Sejam bem-vindos ao jogo: JOKENPÔ')
print('-='*17)
sleep(2)

print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")
sleep(2)
print("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")
sleep(2)
print("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
sleep(2)

while True:
    quant = int(input('Digite quantas rodadas serão: '))
    vitoria_eu = vitoria_ia = 0
        
    for c in range(0, quant):
        eu = str(input('Eu escolho: '))
        ia = ['pedra', 'papel', 'tesoura']
        comp = random.choice(ia)
        sleep(1)
        print('O computador escolheu..')
        sleep(2)
        print(comp)
        sleep(1)
        print()
        if eu == 'pedra' and comp == 'tesoura' or eu == 'papel' and comp == 'pedra' or eu == 'tesoura' and comp == 'papel':
            print('Você venceu!!')
            vitoria_eu += 1
        if eu == comp:
            print('Vocês empataram')
        if comp == 'pedra' and eu == 'tesoura' or comp == 'papel' and eu == 'pedra' or comp == 'tesoura' and eu == 'papel':
            print('O computador venceu!')
            vitoria_ia += 1
        print()
    if vitoria_eu > vitoria_ia:
         print('Você é o grande vencedor!')
    if vitoria_eu == vitoria_ia:
         print('Porque não tentem de novo para desempatarem?')     
    if vitoria_ia > vitoria_eu:
         print('O computador é o grande vencedor!')
    print(f'Você venceu {vitoria_eu} rodada(s) e o computador venceu {vitoria_ia} rodada(s)')
    print()
    print()    
    resp = input('Quer jogar novamente? [S/N] ').strip().upper()[0]
    if resp == 'N':
      break
      print('Jogo finalizado')
