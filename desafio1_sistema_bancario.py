menu = '''
=================================================================
                     Que bom ter você aqui!                       
  O Banco ROSAMM está sempre pronto a ajudar com usas finanças.
=================================================================

Por favor, digite a opção desejada:

[D] Depositar   -   [E] Ver Extrato

[S] Sacar       -   [X] Sair do Sistema\n
'''

saldo = 0
LIMITE_VALOR_SAQUE_DIARIO = 500
extrato = ''
saques_feitos = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == 'd':
        print('Fazer Depósito (aceitamos apenas notas):\n')
        valor_deposito = input('Por favor, informe o valor que será depositado? => ')
        if valor_deposito < 2:
            print('Infelizmente não aceitamos moedas.\n Favor, informe novamente valor a ser depositado.\n')

    elif opcao == 's':
        print('Efetuar Saque')

    elif opcao == 'e':
        print('Exibir Extrato')

    elif opcao == 'x':
        print('\nSaindo do Sistema...\n')
        break

    else:
        print('\nOperação inválida! Por favor, selecione novamente a operação desejada.\n')
