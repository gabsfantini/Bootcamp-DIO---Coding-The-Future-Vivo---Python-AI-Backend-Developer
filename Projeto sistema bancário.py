limite = 1000
saldo = 0
extrato = ''
numero_saque = 0
LIMITE_SAQUE = 3

from datetime import datetime

menu = '''\n
      \033[0;33m------MENU--------\033[m

      \033[1;35m(0) DEPÓSITO
      
      (1) SAQUE
      
      (2) EXTRATO
      
      (3) SAIR \033[m
      
      \033[0;33m------------------\033[m
'''

while True:

    opcao = input('\nEscolha uma opção  {}'.format(menu))

    if opcao == '0':
        valor = float(input('\033[1;36mQual valor deseja depositar R$ \033[m'))

        if valor > 0:
            saldo += valor
            data_hora_atual = datetime.now()
            data_hora_formatada = data_hora_atual.strftime("%d/%m/%Y %H:%M:%S")
            extrato += f'\n\033[1;32mDepósito R$ {valor:.2f} \033[m - {data_hora_formatada}\n'
            print('+ R$ {:.2f} depositado com sucesso!'.format(valor))

        else:
            print ('\033[1;31mValor inválido, tente novamente.\033[m')

    elif opcao == '1':
        valor = float(input('Qual valor deseja sacar R$ '))

        excedeu_limite = valor > limite

        excedeu_saldo = valor > saldo

        excedeu_saque = numero_saque >= LIMITE_SAQUE

        if excedeu_limite:
            print('\033[1;31mAtenção, o seu limite para saques é de R$ 1000,00\033[m')
            
        elif excedeu_saldo:
                print('\033[1;31mVocê não tem saldo sulficiente para realizar essa operação !\033[m')
                print('O seu saldo atual é de R$ {:.2f}'.format(saldo))

        elif excedeu_saque:
                print('\033[1;31mAtenção! Você excedeu o limite de saques diários para sua conta.\033[m')

        elif valor > 0:
             saldo -= valor
             data_hora_atual = datetime.now()
             data_hora_formatada = data_hora_atual.strftime("%d/%m/%Y %H:%M:%S")
             extrato += f'\033[31mSaque R$ {valor:.2f}\033[m - {data_hora_formatada}\n'
             numero_saque += 1
        
        else:
             print('\033[1;31mValor inválido, tente novamente.\033[m')

    elif opcao == '2':
         print('-'*50)
         print('\nEXTRATO BANCÁRIO - BANCO DIO -')
         print('\nNão foram realizadas movimentações nessa conta.'if not extrato else extrato)
         print('\nSaldo: R$ {:.2f}'.format(saldo))
         
         print('-'*50)

    elif opcao == '3':
         break
    
    else:
         print('Opção inválida, tente uma opção válida.')
         
    



        
    


      
        

                  


                    
        



                    


                     


                









            
