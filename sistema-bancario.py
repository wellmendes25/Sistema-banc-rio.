menu = """
[0] Depositar
[1] Sacar
[2] Extrato
[3] Sair

"""



saldo = 0
limite = 500
extrato = ""  # Inicializado como string vazia PARA RECEBER OS DADOS
numero_saques = 1
LIMITE_SAQUES = 3

while True:
    
    opcao = input(menu)
    
    if opcao == "0":
        valor_deposito = float(input("Qual o valor do depósito: "))
        if valor_deposito > 0:
            saldo += valor_deposito
            extrato += f"Depósito: R$ {valor_deposito:.2f}\n" # o EXTRATO SEMPRE RECEBE UM VALOR QUANDO FOR DEPOSITADO
            print(f"Você depositou R$ {valor_deposito:.2f}")
        else:
            print("Valor inválido.")
    
    elif opcao == "1":
        valor_saque = float(input("Qual o valor que você deseja sacar: "))
        
        excedeu_saldo = valor_saque > saldo
        excedeu_limite = valor_saque > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        # Mensagens de depuração adicionadas
        print(f"Tentativa de saque: {valor_saque}, Saldo atualizado: {saldo-valor_saque}, Limite diário: {limite}, Saques realizados: {numero_saques}")

        if excedeu_saldo:
            print("Saldo insuficiente.")
        elif excedeu_limite:
            print(f"Limite de saque é de R$ {limite:.2f}.")
        elif excedeu_saques:
            print("Número máximo de saques atingido.")
        else:
            saldo -= valor_saque
            extrato += f"Saque: R$ {valor_saque:.2f}\n"
            numero_saques += 1
            print(f"Você sacou R$ {valor_saque:.2f}")
    
    elif opcao == "2":
        print("\nExtrato")
        print("-----------")
        if extrato:
            print(extrato)
        else:
            print("Nenhuma transação realizada.")
        print(f"Saldo atual: R$ {saldo:.2f}")
        print("-----------")
    
    elif opcao == "3":
        print("Volte sempre, foi bom lhe atender.")
        break
    
    else:
        print("Opção inválida.")
