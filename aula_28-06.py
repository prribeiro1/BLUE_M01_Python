# ABSTRAÇÃO


# class Pessoa:
#     def __init__(self, nome, idade, peso): # método construtor/inicializador de atributos
#         self.nomePessoa = nome
#         self.idadePessoa = idade
#         self.pesoPessoa = peso

#     def comer(self, calorias,):
#         self.pesoPessoa += calorias

#     def malhar(self, calorias):
#         self.pesoPessoa -= calorias

#     def mostrarDados(self):
#         return f'''
#             Nome = {self.nomePessoa}
#             Idade = {self.idadePessoa}
#             Peso = {self.pesoPessoa}
#         '''


# pessoa1 = Pessoa("Paulo", 32, 74) # Instaciancia de um novo objeto (criando uma referencia da classe através de um objeto)
# pessoa2 = Pessoa("Érica", 31, 55)

# print(pessoa1.mostrarDados()) # nao foi preciso colocar nenhum paramentro pq é o self, e o self da pessoa1

# pessoa1.comer(5)

# print(pessoa1.mostrarDados())


# Se a pessoa tiver mais de 30 anos,as calorias de coomer sao em dobro
# se tiver menos que 39, as calarias de malhar tb sao em dobro

class Pessoa:
    def __init__(self, nome, idade, peso):
        self.nomePessoa = nome
        self.idadePessoa = idade
        self.pesoPessoa = peso

    def comer(self, calorias,):
        if self.idadePessoa > 30:
            dobro = calorias * 2
            self.pesoPessoa += dobro
        else:
            self.pesoPessoa += calorias
        
    def malhar(self, calorias):
        if self.idadePessoa < 30:
            self.pesoPessoa -= calorias*2
        else:
            self.pesoPessoa -= calorias


    def mostrarDados(self):
        return f'''
            Nome = {self.nomePessoa}
            Idade = {self.idadePessoa}
            Peso = {self.pesoPessoa}
        '''

idade1 = int(input('1 Idade: '))        
idade2 = int(input('2 Idade: '))
idade3 = int(input('3 Idade: '))

peso1 = float(input('1 Peso: '))
peso2 = float(input('2 Peso: '))
peso3 = float(input('3 Peso: '))

pessoa1 = Pessoa('p1', idade1, peso1)
pessoa2 = Pessoa('p2', idade2, peso2)
pessoa3 = Pessoa('p3', idade3, peso3)

print(pessoa1.mostrarDados())
print(pessoa2.mostrarDados())
print(pessoa3.mostrarDados())

pessoa1.comer(2)
pessoa2.comer(5)
pessoa3.malhar(5)

print(pessoa1.mostrarDados())
print(pessoa2.mostrarDados())
print(pessoa3.mostrarDados())