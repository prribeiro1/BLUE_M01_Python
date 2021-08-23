# Faça um programa, com uma função que necessite de três argumentos, e que forneça a
# soma desses três argumentos.

# def numeros(n1, n2, n3):
#     soma = n1 + n2 + n3
#     return soma

# n1 = int(input('1 Numero: '))
# n2 = int(input('2 Numero: '))
# n3 = int(input('3 Numero: '))

# print('Soma = ', numeros(n1, n2, n3))




# Faça um programa, com uma função que necessite de um argumento. A função retorna
# o valor de caractere ‘P’, se seu argumento for positivo, ‘N’, se seu argumento for
# negativo e ‘0’ se for 0

# def valor(num):
#     if num > 0:
#         return 'POSITIVO'
#     elif num < 0:
#         return 'NEGATIVO'
#     else:
#         return '0'

# n1 = int(input('Numero: '))
# print(valor(n1))




# Faça um programa com uma função chamada somaImposto. A função possui dois
# parâmetros formais: taxaImposto, que é a quantia de imposto sobre vendas expressa em
# porcentagem e custo, que é o custo de um item antes do imposto. A função “altera” o
# valor de custo para incluir o imposto sobre vendas.

# def somaImposto(taxaImposto, custo):
#     #cálculo do imposto.
#     resultado_imposto = custo + (custo * taxaImposto / 100)
#     #retorno do resultado do imposto
#     return resultado_imposto
    

# taxa = int(input('valor do imposto: '))
# valor = float(input('preço do produto: '))
# print(somaImposto(taxa, valor))



# Faça um programa que calcule o salário de um colaborador na empresa XYZ. O salário
# é pago conforme a quantidade de horas trabalhadas. Quando um funcionário trabalha
# mais de 40 horas ele recebe um adicional de 1.5 nas horas extras trabalhadas

# def colabXYZ(salario, extra):
#     salario_final = salario + extra
#     return salario_final


# salario = float(input('Seu salario: '))
# extra = 0
# hora_extra = int(input('Horas extra trabalhadas: '))
# for c in range(0, hora_extra):
#     extra += 1.5

# print(f'Você recebe R$ {salario} mas com as suas {c+1} horas extras, que dá um valor de R$ {extra}, receberá R$ {colabXYZ(salario, extra)} esse mês') 



# Faça um programa que calcule através de uma função o IMC de uma pessoa que tenha 
# 1,68 e pese 75kg


# def imc(peso, altura):
#     result = peso / (altura * altura)
#     return result

# peso = float(input('Digite seu peso: '))
# altura = float(input('Digite sua altura: '))

# print(imc(peso, altura))




# Escreva uma função que, dado um número nota representando a nota de um estudante, 
# converte o valor de nota para um conceito (A, B, C, D, E e F)


# def estudante(nota):
#     if nota >= 9:
#         return 'A'
#     elif nota >= 8:
#         return 'B'
#     elif nota >= 7:
#         return 'C'
#     elif nota := 6:
#         return 'D'
#     elif nota >= 5:
#         return 'E'
#     else:
#         return 'F'


# nota = float(input('Digite sua nota: '))

# print(estudante(nota))




# Escreva uma função que recebe dois parâmetros e imprime o menor dos dois. Se eles 
# forem iguais, imprima que eles são iguais.


# def result(m, n):
#     if m > n:
#         return f'o menor é o {n}'
#     elif m < n:
#         return f'o menor é o {m}'
#     else:
#         return 'São iguais'


# n1 = int(input('Numero 1: '))
# n2 = int(input('Numero 2: '))

# print(result(n1, n2))




# DESAFIO - Data com mês por extenso. Construa uma função que receba uma data no 
# formato DD/MM/AAAA e devolva uma string no formato D de mesPorExtenso de AAAA. 
# Opcionalmente, valide a data e retorne NULL caso a data seja inválida. Considere que 
# Fevereiro tem 28 dias e que a cada 4 anos temos ano bisexto, sendo que nesses casos Fevereiro 
# terá 29 dias.