menu = '''
[d] Depositar
[s] Sacar
[e] Ver Extrato
[x] Sair do Sistema
'''

saldo = 0
LIMITE_VALOR_SAQUE_DIARIO = 500
extrato = ''
saques_feitos = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == 'd':
        print('Fazer Depósito')

    elif opcao == 's':
        print('Efetuar Saque')

    elif opcao == 'e':
        print('Exibir Extrato')

    elif opcao == 'x':
        print('Saindo do Sistema...')
        break

    else:
        print('Operação inválida! Por favor, selecione novamente a operação desejada.')
