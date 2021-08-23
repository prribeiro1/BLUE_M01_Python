# Exercício Treino - Crie um dicionário em que suas chaves serão os números 1, 4, 5, 6, 
# 7, e 9 (que podem ser armazenados em uma lista) e seus valores correspondentes 
# aos quadrados desses números.
# {1: 1, 4: 16, 5: 25, 6: 36, 7: 49, 9: 81} 

# lista = [1, 4, 5, 6, 7, 9]
# dicionario = {}

# for c in lista:
#     dicionario[c] = c

# for c, v in dicionario.items():
#     value = v ** 2
#     dicionario[v] = value

# print(dicionario)


#  Exercício Treino - Crie um dicionário em que suas chaves correspondem a números 
# inteiros entre [1, 10] e cada valor associado é o número ao quadrado.
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}

# lista = []
# dicionario = {}


# for c in range(1, 11): # dá pra fazer com range, pois foi dito de 1 a 10, ou da mesma forma do exercicio de cima, colocando os valores dentro da lista
#     lista.append(c)
#     dicionario[c] = c


# for c, v in dicionario.items():
#     value = v ** 2
#     dicionario[v] = value

# print(dicionario)


# Faça um programa que leia nome e média de um aluno, guardando também a situação 
# em um dicionário. No final, mostre o conteúdo da estrutura na tela. A média para 
# aprovação é 7. Se o aluno tirar entre 5 e 6.9 está de recuperação, caso contrário é 
# reprovado.

# aluno = {}

# aluno['nome'] = input('Digite o nome: ')
# aluno['media'] = float(input('Digite a média: '))


# if aluno['media'] >= 7.0:
#     aluno['situacao'] = 'Aprovado'
# elif aluno['media'] > 5.0 and aluno['media'] <= 6.9:
#     aluno['situacao'] = 'Recuperação'
# else:
#     aluno['situacao'] = 'Reprovado'


# print(f'{aluno["nome"]} está {aluno["situacao"]}')


# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastreos (com idade) em um dicionário. Se por acaso a CTPS for diferente de 0, o dicionário 
# receberá também o ano de contratação e o salário. Calcule e acrescente , além da idade 
# , com quantos anos a pessoa vai se aposentar. Considere que o trabalhador deve 
# contribuir por 35 anos para se aposentar.

# dados = {}

# dados['nome'] = input('Nome: ')
# nascimento = int(input('Ano de Nascimento: '))

# ano_atual = 2021

# dados['idade'] = ano_atual - nascimento
# dados['carteira'] = int(input('Digite a carteira de trabalho (Zero se não tiver ctps): '))

# if dados['carteira'] > 0:
#     dados['contrataçao'] = int(input('Digite ano de contratação: '))
#     dados['salário'] = float(input('Digite o salário: '))
#     dados['aposenta'] = dados['idade'] + \
#         ((dados['contrataçao'] + 35) - ano_atual)
# else:
#     print('Você precisa começar a trabalhar! :)')
# print(dados)

# print(
#     f'Nome: {dados["nome"]}\nIdade: {dados["idade"]}\nVai se aponsentar com: {dados["aposenta"]} anos.')




# DESAFIO: Crie um programa que leia nome, sexo biologico e idade de várias pessoas, 
# guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma 
# lista. No final, mostre:
# A) Quantas pessoas estão cadastradas.
# B) A média da idade.
# C) Uma lista com as mulheres.
# D) Uma lista com as idades que estão acima da média.
# OBS: O programa deve garantir que o sexo digitado seja válido, e que quando 
# perguntar ao usuário se deseja continuar a resposta seja somente sim ou não.


# pessoa = []
# mulher = []
# ano = []
# media_maior = []

# dicionario = {}


# while True:
#     dicionario['nome'] = input('Digite o nome: ')
#     dicionario['sexo bio'] = input('Digite sexo bio[F/M]: ').lower().strip()[0]
#     dicionario['idade'] = int(input('Digite a idade: '))

#     # acumulando anos lista
#     ano.append(dicionario['idade'])

#     if dicionario['sexo bio'] == 'f':
#         mulher.append(dicionario['nome'])

#     # copia dic para lista
#     pessoa.append(dicionario.copy())

#      # NÃO CONSEGUI COLOCAR OS QUE ESTÃO ACIMA DA IDADE MEDIA
#     media = sum(ano) / len(ano)
#     media_m = 0
#     if media_m > media:
#         media_maior.append(media_m)


#     resp = input('deseja continuar? [S/N] ').strip().upper()[0]
#     if resp == 'N':
#         break        


# print(f'Quantas pessoas estão cadastradas: {len(pessoa)}')
# print(f'A média da idade: {media}')
# print(f'Uma lista com as mulheres: {mulher}')
# print(f'Uma lista com as idades que estão acima da média: {media_m}')




# Desafio: Continuando o exercício 3 crie agora um boletim escolar, seu programa deve receber 5 notas de 15 alunos, assim como o nome desses alunos, o programa tem que 
# calcular a média desse aluno e mostrar a situação dele, seguindo os mesmos critérios 
# apresentados no exercício 3. No final apresente todos nomes, as 5 notas, as médias e as 
# situações dos 15 alunos de uma vez só


# alunos = []  # lista que vai receBEr a copia do dicionario

# for i in range(3):

#     info_alunos = {}  # dicionario de alunos

#     info_alunos['nome'] = input('Digite o nome: ')

#     info_alunos['notas'] = []  # lista que é colocado dict chave notas

#     media = 0  # variável recebe a média calculada dentro do for da nota

#     for n in range(15):
#         nota = float(input('Digite a nota: '))
#         # pulo do gato - criar chave nota e adicionar cada nota em  cada alunos
#         info_alunos['notas'].append(nota)

#         media += nota / 3  # envio da media para variável media acima

#     # dentro do 1º for criar e acionar no dicionario a chave media
#     info_alunos['media'] = media

#     # calculos e criação da chave "situação"
#     if info_alunos['media'] > 7:
#         # cria a chave situação dentro de dict
#         info_alunos['situação'] = 'aprovado'
#     elif 5 <= info_alunos['media'] < 7:
#         info_alunos['situação'] = 'recuperação'
#     else:
#         info_alunos['situação'] = 'reprovado'

#     # dentro do 1º for copia todo o dicionario para a lista.
#     alunos.append(info_alunos.copy())


# # mostrar a impressão
# print(f'{"nome":^15} {"media":^15} {"situação":^15}')  # cria o cabeçalho

# # acessa cada dicionario dentro da lista alunos
# for aluno in alunos:
#     notas = ','.join([str(n) for n in aluno['notas']])
#     print(
#         f'{aluno["nome"]:^15}      {aluno["media"]:.2f}      {aluno["situação"]:^15}')