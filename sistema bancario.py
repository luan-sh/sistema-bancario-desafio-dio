import datetime

menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo           = 0
limite          = 500
extrato         = []
numero_saques   = 0
documento       = 1
LIMITE_SAQUES   = 3

while True:
    opcao = input(menu)

    if opcao == "d":
        valor = float( input("Informe o valor do depósito: ") )
        
        if valor > 0:
            saldo += valor
            extrato.append({
                "documento": documento,
                "operacao": f"Depósito: R$ {valor:.2f}\n",
                "data": datetime.datetime.now()
            })

            documento += 1

            print(f"Depósito realizado com sucesso no valor de {valor:.2f}")
        else:
            print("Operação falhou!\nO valor informado é inválido.")

    elif opcao == "s":

        valor           = float(input("Informe o valor do saque: "))

        excedeu_saldo   = valor > saldo
        excedeu_limite  = valor > limite
        excedeu_saques  = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou!\nVocê não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação falhou!\nO valor do saque excede o limite.")

        elif excedeu_saques:
            print("Operação falhou!\nNúmero máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato.append({
                    "documento": documento,
                    "operacao": f"Saque: R$ {valor:.2f}\n",
                    "data": datetime.datetime.now()
            })

            documento       += 1
            numero_saques   += 1

            print(f"Saque realizado com sucesso no valor de R$ {valor:.2f}")

        else:
            print("Operação falhou!\nO valor informado é inválido.")

    elif opcao == "e":

        if len(extrato) > 0:
            print("\n============================= EXTRATO =============================")
            print("Documento " + ( " "*( len(str(extrato[-1]["documento"]))-10) )  + "| Data       | Hora     | Operação\n")

            for i in range(len(extrato)):
                print(
                        str(extrato[i]["documento"]) + " "*(10-len(str(extrato[i]["documento"]))) + "| " 
                        + extrato[i]["data"].strftime("%d/%m/%Y") + " | " 
                        + extrato[i]["data"].strftime("%X") + " | " 
                        + extrato[i]["operacao"]
                    )
            
            print(f"\nSaldo: R$ {saldo:.2f}")
            print("===================================================================")
        else:
            print("Não foram realizadas movimentações.")

    elif opcao == "q":
        print("Volte sempre!")
        break
    else:
        print("Operação inválida!\nPor favor, selecione novamente a operação desejada.")
