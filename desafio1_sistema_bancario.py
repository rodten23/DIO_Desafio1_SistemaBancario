menu = '''
=================================================================
                     Que bom ter você aqui!                       
  O Banco ROSAMM está sempre pronto a ajudar com usas finanças.
=================================================================

Por favor, digite a opção desejada:

[d] Depositar   -   [e] Ver Extrato
[s] Sacar       -   [x] Sair do Sistema\n
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
        print('\nSaindo do Sistema...\n')
        break

    else:
        print('Operação inválida! Por favor, selecione novamente a operação desejada.')
