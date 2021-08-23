# def area(largura, comprimento):
#     area = largura * comprimento
#     print(f'A larguraa é {largura}, o comprimento é {comprimento} e a área é {area}.')


# area(5, 4)


# def contador(inicio, fim, passo):
#     print(f'A contagem de {inicio} até {fim} com o passo de {passo}: ')

#     cont = inicio

#     while cont <= fim:
#         print(f'{cont}', end=' ')
#         cont += passo
# print('\n FIM')



# contador(1, 10, 1)




# def contador(inicio, fim, passo):
#     print(f'A contagem de {inicio} até {fim} com o passo de {passo}: ')

    
#     if inicio < fim:
#        cont = inicio
#        while cont <= fim:
#            print(f'{cont}', end=' ')
#            cont += passo
#     else:
#         cont = inicio
#         while cont >= fim:
#             print(f'{cont}', end=' ')
#             cont -= passo

#     print('\nFIM')


# contador(10, 0, 2)



def notas(*notas, situacao=False):
    dicionario = dict()
    dicionario['totalNotas'] = len(notas)
    dicionario['maiorNota'] = max(notas)
    dicionario['minNota'] = min(notas)
    dicionario['mediaTurma'] = sum(notas)/len(notas)

    if situacao:
        if dicionario['mediaTurma'] >= 7:
            dicionario['situacao'] = 'APROVADO'


    return[dicionario]