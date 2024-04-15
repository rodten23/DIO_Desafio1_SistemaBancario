menu = '''
=================================================================
                     Que bom ter você aqui!                       
  O Banco ROSAMM está sempre pronto a ajudar com usas finanças.
=================================================================

Por favor, digite a opção desejada:

[D] Depositar   -   [E] Ver Extrato

[S] Sacar       -   [X] Sair do Sistema\n
'''

SALDO_INICIAL = 0
saldo = SALDO_INICIAL

saques_feitos_dia = 0
LIMITE_SAQUES = 3

valor_saques_dia = 0
LIMITE_VALOR_SAQUE_DIARIO = 500

extrato = ''

while True:

    opcao = input(menu)

    if opcao == 'd':
        print('FAZER DEPÓSITO (aceitamos apenas notas):')
        valor_deposito = float(input('\nPor favor, qual valor será depositado? => '))
        while True:
            if valor_deposito < 2:
                valor_deposito = float(input('\nInfelizmente não aceitamos moedas.\nFavor, informe novamente o valor a ser depositado => '))
            else:
                saldo += valor_deposito
                extrato += f'\nDepósito de R$ {valor_deposito:.2f}  (Saldo de R$ {saldo:.2f})'
                break

    elif opcao == 's':
        print('EFETUAR SAQUE (disponibilizamos apenas notas)\nLimites: até 3 saques diários totalizando até R$ 500,00\n')
        
        if saques_feitos_dia == LIMITE_SAQUES:
            print(f'Você atingiu o limite diário de {LIMITE_SAQUES} saques.\nNovos saques poderão ser feitos no próximo dia útil.')
            break
        elif valor_saques_dia == LIMITE_VALOR_SAQUE_DIARIO:
            print(f'Você atingiu o limite diário de R$ {LIMITE_VALOR_SAQUE_DIARIO:.2f}.\nNovos saques poderão ser feitos no próximo dia útil.')
            break
        else:
            valor_saque = float(input('\nPor favor, quanto você quer sacar? => '))
            while True:
                if valor_saque == 0:
                    break
                elif valor_saque < 2:
                    valor_saque = float(input('\nInfelizmente não disponibilizamos moedas.\nFavor, informe novamente o valor que deseja sacar ou digite 0 para voltar=> '))
                elif valor_saque > saldo:
                    valor_saque = float(input('\nVocê não tem saldo suficiente.\nFavor, informe novamente o valor que deseja sacar ou digite 0 para voltar=> '))
                else:
                    saldo -= valor_saque
                    saques_feitos_dia += 1
                    valor_saques_dia += valor_saque
                    extrato += f'\nSaque de R$ {valor_saque:.2f}  (Saldo de R$ {saldo:.2f})'
                    break

    elif opcao == 'e':
        print('EXIBIR EXTRATO')
        print(f'\nSaldo inicial => R$ {SALDO_INICIAL:.2f}')
        
        if extrato == '':
            print('\nAinda não foram feitos depósitos ou saques para esta conta.')
        else:
            print(extrato)
        input('\nPressione qualquer tecla para voltar ao menu anterior: ')
        
    elif opcao == 'x':
        print('\nSaindo do Sistema...\n')
        break

    else:
        print('\nOperação inválida! Por favor, selecione novamente a operação desejada.\n')
