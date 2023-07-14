
menu = f"""
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
"""
saldo = 0
extrato = ""
LIMITE_DIARIO_SAQUES = 3
valor_maximo_saque = 500
quantidade_saques = 0

while True:
    print("Seja bem-vindo ao nosso Banco. \n Informe a opção desejada:\n ")

    opção = input(menu)

    if opção == "d":
        valor = float(input("Insira o valor a ser depositado: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito R$ {valor:.2f}\n"
            print(f'Depósito efetuado com sucesso.\n Valor depositado R$ {valor:.2f}.')
        else:
            print("O valor inserido é inválido, verifique e tente novamente.")
    
    elif opção == "s":
        valor = float(input("Insira o valor do saque: "))

        saldo_insuficiente = valor > saldo
        valor_saque_excedido = valor > valor_maximo_saque
        limite_saque_alcancado = quantidade_saques >= LIMITE_DIARIO_SAQUES

        if saldo_insuficiente:
            print("Operação não realizada.\n Saldo Insuficiente.")

        elif valor_saque_excedido:
            print( "Operação não realizada.\n O valor de saque excede o limite.")
        elif limite_saque_alcancado:
            print( "Operação não realizada.\n Quantidade de saques diário excedida.")
        elif valor > 0:
            saldo -= valor
            quantidade_saques += 1
            extrato += f'Saque R$ {valor:.2f}\n'
            print(f'Saque efetuado com sucesso. \n Saldo em conta R$ {saldo:.2f}')
        else:
            print("Operação falhou. O valor informado é inválido.")
    elif opção == "e":
        print('"""""""""""""""EXTRATO"""""""""""""""')
        print("Não foram realizadas movimentações."if not extrato else extrato)
        print(f'Saldo: R${saldo:.2f}')
        print('""""""""""""""""""""""""""""""""""""""')
    elif opção == "q":
        break 
    else:
        print("Opção inválida. Tente novamente.")
        print("   \n     ")




            
        
        


    


    




