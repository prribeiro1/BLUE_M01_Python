# A 1° Função precisa ser chamada autoriza_voto() ela vai receber como parâmetro o
# ano de nascimento de uma pessoa que será digitado pelo usuário, retornando um
# valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e
# OBRIGATÓRIO nas eleições.

# A 2° Função será a votacao(), ela vai receber dois parâmetros, autorização (que virá
# da função autoriza_voto()) e o voto que é o número que a pessoa votou.

# Se ela não puder votar, a 2° função terá que retornar “Você não pode votar”, caso o
# contrário a 2° função deve validar o número que a pessoa escolheu, ela pode
# escolher de 1 a 5 (crie 3 candidatos para a votação):

# ● 1, 2 ou 3 - Votos para os respectivos candidatos
# ● 4- Voto Nulo
# ● 5 - Voto em Branco

# Sua função votacao() tem que calcular e mostrar:
# ● O total de votos para cada candidato;
# ● O total de votos nulos;
# ● O total de votos em branco;
# ● Qual candidato venceu a votação


from datetime import datetime # função para representar uma data
from os import system # função para limpar o terminal

def autoriza_voto(nascimento): # função para validar se o usuário está ou não apto para votar, através da sua idade
    idade = hoje - nascimento
    if idade < 16:
        autorizacao = 'NEGADO'
    elif 18 <= idade < 70:
        autorizacao = 'OBRIGATÓRIO'
    else:
        autorizacao = 'OPCIONAL'
    return autorizacao

def votacao(autorizacao, voto): # função que irá pegar a validação da função anterior e, se for liberado, contabilizar o voto do usuário
    if autorizacao == 'NEGADO':
        print('--> Você não tem idade para votar <---')
    else:
        lista[voto-1] += 1 # como o voto começa por 1 e o índice da lista por 0, dessa forma conseguimos igualá-las para computar corretamente o voto
    print(f'''
    RESULTADO PARCIAL:

    Primeiraldo:    {lista[0]}\n
    Segundavio:     {lista[1]}\n
    Terceirinho:    {lista[2]}\n
    Votos Nulos:    {lista[3]}\n
    Votos Brancos:  {lista[4]}
    ''')

lista = [0, 0, 0, 0, 0]

hoje = datetime.now().year

system('cls')

while True: # laço de repetição  para que o usuário digite seu ano de nascimento e, se liberado, prosseguir votando
    nascimento = int(input('Digite seu ano de nascimento: '))
    print('[1] - Primeiraldo  |  [2] - Segundavio  |  [3] - Terceirinho  |  [4] - NUlo  |  [5] - Branco')
    print()
    voto = int(input('Digite o seu voto: '))
    while voto not in range(1, 6): # while para confirmar se o número digitado se refere à alguma opção 
        voto = int(input('Tente novamente: '))

    votacao(autoriza_voto(nascimento), voto)

    resp = input('\nTem mais algum eleitor? [S/N] ').strip().upper()[0] # continuar ou não com a votação
    while resp not in 'SN':
        resp = input('Tente novamente.')

    system('cls')
    if resp == 'N':
        break

 
print(f'''
    RESULTADO FINAL:

    Primeiraldo:    {lista[0]}\n
    Segundavio:     {lista[1]}\n
    Terceirinho:    {lista[2]}\n
    Votos Nulos:    {lista[3]}\n
    Votos Brancos:  {lista[4]}
''')