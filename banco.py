print('#'*10, 'MENU', '#'*10)
print('\n'
      '[1] Depósito\n'
      '[2] Saque\n'
      '[3] Extrato\n'
      '[4] sair\n')
print('#'*26)

extrato = int()
cont_saq = 3

while True:
    try:
        op = int(input('Qual a sua opção? '))
    except ValueError:
        print('Opção inválida. Tente novamente...')
    
    if op == 1:
        vl_d = float(input('Quanto deseja depositar? R$ '))
        extrato += vl_d
    elif op == 2:
        vl_s = float(input('Quanto deseja sacar? R$ '))
        if vl_s > extrato:
            print('Você não tem saldo suficiente.')
        else:
            extrato -= vl_s
            cont_saq -= 1
        if cont_saq < 0:
            print('Sinto muito, mas você tem um limite diário de apenas três saques por dia e por isso não poderá efetuar mais saques hoje.')
    elif op == 3:
        print(f'Seu saldo é de R$ {extrato:.2f}')
    elif op == 4:
        break
    else:
        print(f'Opção invalida. Tente novamente...')