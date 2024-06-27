#Neste desafio, você terá a oportunidade de otimizar o Sistema Bancário previamente desenvolvido com o uso de funções Python. O objetivo é aprimorar a estrutura e a eficiência do sistema, implementando as operações de depósito, saque e extrato em funções específicas. Você terá a chance de refatorar o código existente, dividindo-o em funções reutilizáveis, facilitando a manutenção e o entendimento do sistema como um todo. Prepare-se para aplicar conceitos avançados de programação e demonstrar sua habilidade em criar soluções mais elegantes e eficientes utilizando Python.


from datetime import datetime

class Usuario:
    def __init__(self, nome, data_nascimento, cpf, endereco):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf
        self.endereco = endereco

class ContaCorrente:
    numero_conta_atual = 0
    agencia = "0001"
    
    def __init__(self, usuario):
        ContaCorrente.numero_conta_atual += 1
        self.numero_conta = ContaCorrente.numero_conta_atual
        self.usuario = usuario
        self.saldo = 0
        self.extrato = []
        self.numero_saques = 0
        self.LIMITE_SAQUES = 3
        self.limite = 1000
    
    def deposito(self, valor):
        if valor > 0:
            self.saldo += valor
            self.registrar_transacao(f'Depósito R$ {valor:.2f}')
            print(f'+ R$ {valor:.2f} depositado com sucesso!')
        else:
            print('Valor inválido, tente novamente.')
    
    def saque(self, valor):
        if valor > self.limite:
            print('Limite de saque excedido (R$ 1000,00).')
        elif valor > self.saldo:
            print('Saldo insuficiente.')
        elif self.numero_saques >= self.LIMITE_SAQUES:
            print('Limite diário de saques excedido.')
        elif valor > 0:
            self.saldo -= valor
            self.numero_saques += 1
            self.registrar_transacao(f'Saque R$ {valor:.2f}')
            print(f'- R$ {valor:.2f} sacado com sucesso!')
        else:
            print('Valor inválido, tente novamente.')
    
    def imprimir_extrato(self):
        print('-' * 50)
        print(f'\nEXTRATO BANCÁRIO - BANCO DIO - Conta: {self.numero_conta} - Agência: {self.agencia}')
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

def criar_usuario():
    nome = input('Digite o nome completo do usuário: ')
    data_nascimento = input('Digite a data de nascimento (DD/MM/AAAA): ')
    cpf = input('Digite o CPF do usuário: ')
    endereco = input('Digite o endereço completo (logradouro, nro - bairro - cidade/estado): ')
    
    # Verifica se já existe um usuário com o mesmo CPF
    for usuario in lista_usuarios:
        if usuario.cpf == cpf:
            print('Já existe um usuário cadastrado com este CPF.')
            return None
    
    # Extrai apenas os números do CPF
    cpf_numeros = ''.join(filter(str.isdigit, cpf))
    
    usuario = Usuario(nome, data_nascimento, cpf_numeros, endereco)
    lista_usuarios.append(usuario)
    print(f'Usuário {nome} cadastrado com sucesso!')
    return usuario

def criar_conta_corrente(usuario):
    conta = ContaCorrente(usuario)
    lista_contas.append(conta)
    print(f'Conta corrente criada com sucesso para o usuário {usuario.nome}.')
    return conta

def listar_contas_usuario(cpf):
    contas_usuario = [conta for conta in lista_contas if conta.usuario.cpf == cpf]
    if contas_usuario:
        print(f'Lista de contas do usuário com CPF {cpf}:')
        for conta in contas_usuario:
            print(f'Conta {conta.numero_conta} - Saldo: R$ {conta.saldo:.2f}')
    else:
        print(f'Usuário com CPF {cpf} não possui contas cadastradas.')

# Listas para armazenar usuários e contas
lista_usuarios = []
lista_contas = []

def main():
    while True:
        print('\n------MENU--------')
        print('(0) Criar Usuário')
        print('(1) Criar Conta Corrente')
        print('(2) Realizar Depósito')
        print('(3) Realizar Saque')
        print('(4) Extrato Bancário')
        print('(5) Listar Contas de um Usuário')
        print('(6) Sair')
        print('------------------')

        opcao = input('\nEscolha uma opção: ')

        if opcao == '0':
            criar_usuario()
        elif opcao == '1':
            cpf = input('Digite o CPF do usuário para vincular à nova conta: ')
            usuario = next((u for u in lista_usuarios if u.cpf == cpf), None)
            if usuario:
                criar_conta_corrente(usuario)
            else:
                print(f'Não foi encontrado um usuário com CPF {cpf}.')
        elif opcao == '2':
            numero_conta = int(input('Digite o número da conta para depósito: '))
            conta = next((c for c in lista_contas if c.numero_conta == numero_conta), None)
            if conta:
                valor = float(input('Qual valor deseja depositar R$ '))
                conta.deposito(valor)
            else:
                print(f'Conta com número {numero_conta} não encontrada.')
        elif opcao == '3':
            numero_conta = int(input('Digite o número da conta para saque: '))
            conta = next((c for c in lista_contas if c.numero_conta == numero_conta), None)
            if conta:
                valor = float(input('Qual valor deseja sacar R$ '))
                conta.saque(valor)
            else:
                print(f'Conta com número {numero_conta} não encontrada.')
        elif opcao == '4':
            numero_conta = int(input('Digite o número da conta para extrato: '))
            conta = next((c for c in lista_contas if c.numero_conta == numero_conta), None)
            if conta:
                conta.imprimir_extrato()
            else:
                print(f'Conta com número {numero_conta} não encontrada.')
        elif opcao == '5':
            cpf = input('Digite o CPF do usuário para listar suas contas: ')
            listar_contas_usuario(cpf)
        elif opcao == '6':
            break
        else:
            print('Opção inválida, tente uma opção válida.')

if __name__ == "__main__":
    main()