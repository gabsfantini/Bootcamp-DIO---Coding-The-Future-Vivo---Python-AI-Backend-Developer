from datetime import datetime

class Cliente:
    def __init__(self, nome, data_nascimento, cpf, endereco):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf
        self.endereco = endereco

class Conta:
    def __init__(self, numero):
        self.numero = numero
        self.saldo = 0.0
        self.extrato = []
    
    def deposito(self, valor):
        if valor > 0:
            self.saldo += valor
            self.registrar_transacao(f'Depósito R$ {valor:.2f}')
            print(f'+ R$ {valor:.2f} depositado com sucesso!')
        else:
            print('Valor inválido, tente novamente.')
    
    def saque(self, valor):
        if valor > self.saldo:
            print('Saldo insuficiente.')
        elif valor <= 0:
            print('Valor inválido, tente novamente.')
        else:
            self.saldo -= valor
            self.registrar_transacao(f'Saque R$ {valor:.2f}')
            print(f'- R$ {valor:.2f} sacado com sucesso!')
    
    def imprimir_extrato(self):
        print('-' * 50)
        print(f'\nEXTRATO BANCÁRIO - BANCO DIO - Conta: {self.numero}')
        if not self.extrato:
            print('\nNão foram realizadas movimentações nessa conta.')
        else:
            for operacao in self.extrato:
                print(operacao)
        print('\nSaldo: R$ {:.2f}'.format(self.saldo))
        print('-' * 50)
    
    def registrar_transacao(self, descricao):
        data_hora_atual = datetime.now()
        data_hora_formatada = data_hora_atual.strftime("%d/%m/%Y %H:%M:%S")
        self.extrato.append(f'{descricao} - {data_hora_formatada}')

class ContaCorrente(Conta):
    def __init__(self, numero, limite_saque):
        super().__init__(numero)
        self.limite_saque = limite_saque
        self.limite_saques_diarios = 3
        self.numero_saques = 0
    
    def saque(self, valor):
        if self.numero_saques >= self.limite_saques_diarios:
            print('Limite diário de saques excedido.')
        elif valor > self.limite_saque:
            print(f'Limite de saque excedido (R$ {self.limite_saque:.2f}).')
        else:
            super().saque(valor)
            self.numero_saques += 1

def criar_cliente():
    nome = input('Digite o nome completo do cliente: ')
    data_nascimento = input('Digite a data de nascimento (DD/MM/AAAA): ')
    cpf = input('Digite o CPF do cliente: ')
    endereco = input('Digite o endereço completo: ')

    # Verifica se já existe um cliente com o mesmo CPF
    for cliente in lista_clientes:
        if cliente.cpf == cpf:
            print('Já existe um cliente cadastrado com este CPF.')
            return None
    
    cliente = Cliente(nome, data_nascimento, cpf, endereco)
    lista_clientes.append(cliente)
    print(f'Cliente {nome} cadastrado com sucesso!')
    return cliente

def criar_conta(numero_conta, tipo_conta, cliente):
    if tipo_conta == '1':
        conta = Conta(numero_conta)
    elif tipo_conta == '2':
        limite_saque = float(input('Digite o limite de saque da conta corrente: '))
        conta = ContaCorrente(numero_conta, limite_saque)
    else:
        print('Tipo de conta inválido.')
        return None
    
    cliente_conta = {'cliente': cliente, 'conta': conta}
    lista_clientes_contas.append(cliente_conta)
    print(f'Conta criada com sucesso para o cliente {cliente.nome}.')
    return conta

def listar_contas_cliente(cpf):
    if not lista_clientes_contas:
        print('Não há contas cadastradas.')
        return
    
    cliente = next((c['cliente'] for c in lista_clientes_contas if c['cliente'].cpf == cpf), None)
    if cliente:
        print(f'Lista de contas do cliente com CPF {cpf}:')
        for cliente_conta in lista_clientes_contas:
            if cliente_conta['cliente'].cpf == cpf:
                print(f'Número da Conta: {cliente_conta["conta"].numero} - Saldo: R$ {cliente_conta["conta"].saldo:.2f}')
    else:
        print(f'Cliente com CPF {cpf} não possui contas cadastradas.')

# Listas para armazenar clientes e suas contas
lista_clientes = []
lista_clientes_contas = []

def main():
    while True:
        print('\n------MENU--------')
        print('(0) Criar Cliente')
        print('(1) Criar Conta Simples')
        print('(2) Criar Conta Corrente')
        print('(3) Realizar Depósito')
        print('(4) Realizar Saque')
        print('(5) Extrato Bancário')
        print('(6) Listar Contas de um Cliente')
        print('(7) Sair')
        print('------------------')

        opcao = input('\nEscolha uma opção: ')

        if opcao == '0':
            criar_cliente()
        elif opcao in ['1', '2']:
            cpf = input('Digite o CPF do cliente para vincular à nova conta: ')
            cliente = next((c for c in lista_clientes if c.cpf == cpf), None)
            if cliente:
                numero_conta = len(lista_clientes_contas) + 1  # número da conta é simplesmente o índice + 1
                criar_conta(numero_conta, opcao, cliente)
            else:
                print(f'Não foi encontrado um cliente com CPF {cpf}.')
        elif opcao == '3':
            numero_conta = int(input('Digite o número da conta para depósito: '))
            conta = next((c['conta'] for c in lista_clientes_contas if c['conta'].numero == numero_conta), None)
            if conta:
                valor = float(input('Qual valor deseja depositar R$ '))
                conta.deposito(valor)
            else:
                print(f'Conta com número {numero_conta} não encontrada.')
        elif opcao == '4':
            numero_conta = int(input('Digite o número da conta para saque: '))
            conta = next((c['conta'] for c in lista_clientes_contas if c['conta'].numero == numero_conta), None)
            if conta:
                valor = float(input('Qual valor deseja sacar R$ '))
                conta.saque(valor)
            else:
                print(f'Conta com número {numero_conta} não encontrada.')
        elif opcao == '5':
            numero_conta = int(input('Digite o número da conta para extrato: '))
            conta = next((c['conta'] for c in lista_clientes_contas if c['conta'].numero == numero_conta), None)
            if conta:
                conta.imprimir_extrato()
            else:
                print(f'Conta com número {numero_conta} não encontrada.')
        elif opcao == '6':
            cpf = input('Digite o CPF do cliente para listar suas contas: ')
            listar_contas_cliente(cpf)
        elif opcao == '7':
            break
        else:
            print('Opção inválida, tente uma opção válida.')

if __name__ == "__main__":
    main()