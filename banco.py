saldo = 0
saques_realizados = 0
max_saque_dia = 3
limite_saque = 500
op = 0

while True:
    print('#'*10, 'MENU', '#'*10)
    print('\n'
      '[1] Depósito\n'
      '[2] Saque\n'
      '[3] Extrato\n'
      '[4] sair\n')
    print('#'*26)
    
    op = int(input('Qual a sua opção? '))
    
    if op == 1:
        vl_d = float(input('Quanto deseja depositar? R$ '))
        saldo += vl_d
    elif op == 2:
        if saques_realizados < max_saque_dia:
            valor_saque = float(input("Digite o valor do saque: "))
            if valor_saque <= saldo and valor_saque <= limite_saque:
                saldo -= valor_saque
                saques_realizados += 1
                print("Saque realizado com sucesso!")
            else:
                print("Valor de saque inválido! Acima do limite diário ou saldo insuficiente.")
        else:
            print("Limite de saques diários atingido!")
    elif op == 3:
        print(f'Seu saldo é de R$ {saldo:.2f}')
    elif op == 4:
        print("Encerrando o programa...")
        break
    else:
        print("Opção inválida! Por favor, escolha uma opção válida.")