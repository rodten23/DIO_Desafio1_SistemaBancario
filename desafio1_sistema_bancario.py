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
extrato = 'R$ 0.00'
saques_feitos = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == 'd':
        print('Fazer Depósito (aceitamos apenas notas):')
        valor_deposito = float(input('\nPor favor, qual valor que será depositado? => '))
        while True:
            if valor_deposito < 2:
                valor_deposito = float(input('\nInfelizmente não aceitamos moedas.\nFavor, informe novamente valor a ser depositado => '))
            else:
                saldo += valor_deposito
                extrato += f'\nDepósito de R$ {valor_deposito:.2f}  (Saldo de R$ {saldo:.2f})'
                break

    elif opcao == 's':
        print('Efetuar Saque')

    elif opcao == 'e':
        print('Exibir Extrato')

    elif opcao == 'x':
        print('\nSaindo do Sistema...\n')
        break

    else:
        print('\nOperação inválida! Por favor, selecione novamente a operação desejada.\n')
