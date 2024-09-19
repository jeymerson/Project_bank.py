import textwrap
from termcolor import colored # Para dar uma dar uma corzinha à +

def message_alert (message):
    return colored (f"{message}", "yellow") # mensagem de alerta
    
def message_erro (message):
    return colored (f"\n❌ ❌ {message} ❌ ❌\n", "red") # mensagem de erro

def message_success (message):
    return colored (f"{message}", "green") # mensagem de ok 
def message_default (message):
    return colored (f"{message}", "magenta") # mensagem de ok 

def menu():
    menu = """\n
    🟪🟪🟪🟪🟪🟪🟪 Menu 🟪🟪🟪🟪🟪🟪🟪 
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova Conta
    [lc]\tListar Contas
    [nu]\tNovo usuário
    [q]\tsair  
    ▶  """
    return input(colored(textwrap.dedent(menu),"magenta"))

def deposito(saldo, valor, extrato, /):
    #A função de depósito deve receber valores apenas por posição /!
    if valor > 0:
        saldo += valor
        extrato += message_alert(f"Depósito: \t R$ {valor:.2f}\n")
        print(message_success("\n ==== 💸 Depósito realizado com sucesso ! 💸 ===") )
    else:
        print(message_erro("Operação falhou! O valor informado é inválido!"))
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    #apenas por parametros nomeados *>

    #validações
    valor_invalido = valor <= 0
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques
    
    if excedeu_saldo:
        print( message_erro("Operação falhou! você não tem saldo suficiente"))

    elif excedeu_saques:
        print( message_erro("Operação falhou! O valor do saque excedeu o limite"))

    elif excedeu_limite:
        print( message_erro("Operação falhou! Número máximo de saques excedido"))

    elif valor_invalido:
        print( message_erro("Operação falhou! O valor deverá ser maior que 0"))
        
    elif valor > 0:
        saldo -= valor
        extrato += message_alert(f"Saque: \t\t R${valor:.2f}\n")
        numero_saques = numero_saques + 1
        print(f"---------  {numero_saques}")
        print(message_success(f"\n --- Saque de {valor} realizado com sucesso! ---"))

    else:
        print( message_erro("Operação falhou! O valor informado inválido"))

    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    #de forma nomeado *=>
    #de forma posicional <=/
    print(message_alert("\n--------------------EXTRATO---------------------"))
    #validação e exibição caso não tenha sido movimentada a conta
    print(message_alert("Não foram realizadas movimentações.") if not extrato else extrato)
    print(message_alert(f"\nSaldo: \t\tR$ {saldo:.2f}"))
    print(message_alert("\n-------------------------------------------------"))
  

def criar_usuario(usuarios):
    cpf = input(message_alert("Informe o CPF (somente números): "))
    usuario = filtrar_usuario (cpf, usuarios)

    if usuario:
        print(message_erro("\nJá existe usuário com esse CPF!"))
        #se o usuário exista irá retornar ao fluxo
        return
    nome = input(message_alert("Informe o nome completo: "))
    data_nascimento = input(message_alert("Informe a data de nascimento (dd-mm-aaaa): "))
    endereco = input(message_alert("Informe o endereço (logradouro, nro - bairo - cidade/estado): "))


    #adiciona o usuário como um dicionário
    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print(message_success("---- Usuário criado com  sucesso! ----"))


def filtrar_usuario(cpf, usuarios):
    # se tiver usuário o retornará, se não a lista ficará vazia
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    #verifica se usuarios_filtrados tem conteúdo, se vão for
    # uma lista vazia, retorna o primeiro elemento (usuario achado)
    return usuarios_filtrados[0] if usuarios_filtrados else None
    # se não encontrar retorna none

def criar_conta(agencia, numero_conta, usuarios):
    if len(usuarios) < 1:
        print(message_erro("Não existe usuários para criar conta, por favor, cadastre o usuário!"))
        return
    #pede o cpf
    cpf = input(message_alert("Informe o CPF do usuário: "))
    #verifica se já existe um usuário com este cpf
    usuario = filtrar_usuario(cpf, usuarios)

    # se não encontrou o usuário
    if usuario:
        print(message_success("\n---- Conta criada com  sucesso! ----"))
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    
    # se não tiver retorno, o padrão é None
    print(message_erro("Usuário não encontradom fluxo de criação de conta encerrado! "))

def listar_contas (contas):
    for conta in contas:
        linha = f"""\
        Agência:\t{conta['agencia']}
        C/c:\t\t{conta['numero_conta']}
        Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []
    
    while True:
            opcao = menu()
            if opcao.lower() == 'd':
                try:
                  valor = float(input(message_default("Informe o valor do dedpósito: ")))
                    #retorno - as variáveis acima tem que receber estes valores
                    # para serem mudados, refatorarei futuramente está parte
                  saldo, extrato = deposito (saldo, valor , extrato)
                 
                except ValueError:
                    print(message_erro("Porfavor, digite apenas números e com valores positivos!‼"))
                finally:
                    continue

            elif opcao.lower() == 's':
                try:
                    valor = float(input(message_alert("Informe o valor de saque: ")))
                    saldo, extrato = sacar(
                        saldo=saldo,
                        valor=valor, 
                        extrato=extrato,
                        limite=limite,
                        numero_saques=numero_saques,
                        limite_saques=LIMITE_SAQUES,
                    )
                    
                except ValueError:
                    print(message_erro("Porfavor, digite apenas números e com valores positivos!‼"))
                finally:
                    continue

            elif opcao.lower() == 'e':
                exibir_extrato(saldo, extrato=extrato)

            elif opcao.lower() == 'nu':
                criar_usuario(usuarios)

            elif opcao.lower() == 'nc':
                #Contas dos usuário é o tamanho da quantidade contas + 1 / para resolve
                # problemas de contas não usuadas, adicionar propriedade em conta, com o valor de ativa ou não
                numero_conta = len(contas) + 1
                #criando a conta
                conta = criar_conta(AGENCIA, numero_conta, usuarios)

                #se a conta foi criada, mandar conta
                if conta:
                    contas.append(conta)


            elif opcao.lower() == 'lc':
                listar_contas(contas)

            elif opcao.lower() == 'q':
                break
            else:
                print(message_erro("Operação inválida, por favor seleciona novamente a operação desejada."))



main()