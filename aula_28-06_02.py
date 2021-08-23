#Crie uma classe chamada Conta para simular as operações de uma conta corrente. Sua classe deverá ter os atributos Titular e Saldo, e os métodos Sacar e Depositar. Crie um objeto da classe Conta e teste os atributos e métodos implementados.​ Adicione uma regra no método Sacar, onde o usuário só poderá sacar se o Saldo for maior que zero, caso contrário mostre a mensagem na tela: "Você não tem saldo suficiente para essa operação."


# ABSTRAÇÃO


class Conta:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo


    def sacar(self, dinheiro):
        if self.saldo <= 0:
            print('Você não tem saldo suficiente para essa operação')
        else:
            self.saldo -= dinheiro


    def depositar(self, dinheiro):
        self.saldo += dinheiro


    def mostrarConta(self):
        return f'''
            Titular = {self.titular}
            Saldo = {self.saldo}
        '''

pessoa = input('Digite o nome do titular da conta: ')
saldo = float(input('Qual o seu saldo? '))

pessoa1 = Conta(pessoa, saldo)

print(pessoa1.mostrarConta())

pessoa1.sacar(10)
