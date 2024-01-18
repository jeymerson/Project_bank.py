menu = """
=================Bem vindo ao Banco-X ======================

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

============================================================
Por favor, escolha uma das opções acima => """

saldo = 1000
limite = 500
extrato = ""
numeros_saques = 0
LIMITE_SAQUES = 3
numero_de_operacoes = 0
#as opções podem ser tanto em maiusculo ou minusculo
while True:

    opcao = input (menu)

    if (opcao == "s") or (opcao =="S"):
        print("Opção escolhida => SAQUE")
        if numeros_saques < LIMITE_SAQUES:   #caso o limite de saques seja atinjidos, não pergunta se vai sacar mais algum valor        
            print(f'Quantidade de saques disponives para o dia é {LIMITE_SAQUES-numeros_saques}')
            valor = float(input(f'informe o valor do saque, R$: '))
            if valor > saldo:
                print("valor acima do saldo")
            elif valor ==0:
                print("Não aceitamos valores nulos")
            elif valor > limite:
                print("valor acima do limite máximo (RS 500,00)")
            elif valor < 0:
                print("Não aceitamos valores negativos, somente pósitivos!")
            else:
                saldo -= valor
                numeros_saques += 1
                numero_de_operacoes +=1

                print(f'valor sacado de R${valor:.2f}, saldo de R${saldo:.2f}')
                extrato += f'{numero_de_operacoes} - valor sacado de R${valor:.2f} \n'
        else:
            print("Limites de saque alcançado!")

    elif (opcao == "d") or (opcao =="D"):
        print("Opção escolhida =>  DEPOSITAR")
        valor = float(input(f'informe o valor para depósito R$: '))
        if valor < 0:
            print ("Não aceitamos valores negativos, somente pósitivos!")
        else:
            saldo += valor
            numero_de_operacoes +=1
            print(f'valor depositado de R${valor:.2f}, saldo de R${saldo:.2f}')
            extrato += f'{numero_de_operacoes} - valor depositado de R${valor:.2f}\n'

    elif (opcao == "e") or (opcao =="E"):
        print("Opção escolhida =>  EXTRATO")
        top_line = "EXTRATO"
        print(top_line.center(60,'-'))
        print(extrato)
        print(f'Saldo atual de R$: {saldo:.2f}')
        final_line = "-"
        print(final_line.center(60,'-'))




    elif (opcao == "q") or (opcao =="Q") or (opcao=="sair") or (opcao=="SAIR"):  #assim temos mais variedade para sair do programa
        print("Opção escolhida =>  SAIR\n")
        print("Obrigado por usar nossos serviços, volte sempre!\n")
        break

    else:
        print("Operação invalida, por favor selecione novamente a operação desejada\n")
    
