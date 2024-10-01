from abc import ABC, abstractclassmethod, abstractmethod, abstractproperty
import textwrap
from termcolor import colored # Para dar uma dar uma corzinha à +
from datetime import datetime


def message_alert (message):
    return colored (f"{message}", "yellow") # mensagem de alerta
    
def message_erro (message):
    return colored (f"\n❌ ❌ {message} ❌ ❌\n", "red") # mensagem de erro

def message_success (message):
    return colored (f"{message}", "green") # mensagem de ok 
def message_default (message):
    return colored (f"{message}", "magenta") # mensagem de ok 
def message_esc (message):
    return colored (f"{message} 🖐", "light_blue") # mensagem de ok 



class Cliente():
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []
    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta) #invoca o registrar de transacao       

    def adicionar_transacao(self, conta):
        self.contas.append(conta) # adicionar a conta recebida como parâmetro no array de contas    

class Pessoa_fisica(Cliente):
    def __init__(self, nome, data_nascimento, cpf, endereco):
        super().__init__(endereco)
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf

class Conta():
    def __init__(self, numero, cliente):
        self.__saldo = 0
        self.__numero = numero
        self.__agencia = "0001"
        self.__cliente = cliente
        self.__historico = Historico();
    
    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero,cliente) #retorna ums instancai de conta

    @property
    def saldo(self):
        return self.__saldo

    @property
    def numero(self):
        return self.__numero
    
    @property
    def agencia(self):
        return self.__agencia
    
    @property
    def cliente(self):
        return self.__cliente
    
    @property
    def historico(self):
        return self.__historico

    def sacar(self, valor):
        saldo = self.saldo
        excedeu_saldo = valor > saldo

        if excedeu_saldo:
            print(message_erro("Operação falhou! Você não tem saldo suficiente."))

        elif valor > 0:
            self.__saldo -= valor
            print(message_success("Saque realizado com sucesso!"))
            return True
       
        else:
            print(message_erro("Operação falhou! o valor informado é inválido"))
        return False
        
    def deposito(self, valor):
        if valor > 0:
            self.__saldo += valor
            print(message_success("Depósito realizado com sucesso!"))
        else:
            print(message_erro("Operação falhou! O valor informado é inválido."))
            return False
        return True

class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saque=3):
        super().__init__(numero, cliente)
        self.limite = limite
        self.limite_saque = limite_saque
    
    def sacar(self, valor): #sobrescrita método sacar
        numero_saques = len(
            [transacao for transacao in self.historico.
             transacoes if transacao["tipo"] == Saque.__name__]
        )

        excedeu_limite = valor > self.limite
        excedeu_saques = numero_saques >= self.limite_saque
        
        if excedeu_limite:
            print(message_erro(f"Operação falhou! o valor do do saque excede o limite! limite = {self.limite}"))
        elif excedeu_saques:
            print (message_erro("Operação falhou! Número máximo de saques excedido"))

        else:
            return super().sacar(valor)
        
        return False
    
    def __str__(self):
        return f"""\
        Agência: \t{self.agencia}
        C/C:\t\t{self.numero}
        Titular:\t{self.cliente.nome} 
    """

class Historico():
    def __init__(self):
        self._transacoes = []
    
    @property
    def transacoes(self):
        return self._transacoes
    
    def adicionar_transacao(self, transacao):
        self._transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                "data": datetime.now().strftime
                ("%d-%m-%Y %H:%M:%S"),
            }
        )

  #   def historico(transacao, valor):
  #      return F"|Data: {(datetime.today()).strftime("%d/%m/%y %H:%M")}|\n\tFoi realizado um {transacao} no valor de RS {valor:.2f}\n"

class Transacao (ABC):
    @property
    @abstractproperty
    def valor(self):
        pass

    @abstractclassmethod
    def registrar(self, conta):
        pass

class Saque(Transacao):
    def __init__(self, valor):
        self.__valor = valor

    @property
    def valor(self):
        return self.__valor

    def registrar(self, conta):
        sucesso_transacao = conta.sacar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)


class Deposito(Transacao):
    def __init__(self, valor):
        self.__valor = valor

    @property
    def valor(self):
        return self.__valor

    def registrar(self, conta):
        sucesso_transacao = conta.deposito(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)


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

def filtrar_cliente(cpf,clientes):
    clientes_filtrados = [cliente for cliente in clientes if cliente.cpf == cpf]
    return clientes_filtrados[0] if clientes_filtrados else None

def recuperar_conta_cliente(cliente):
    if not cliente.contas:
        print(message_erro("Cliente não possui conta! "))
        return
    #FIXME: não permite que o cliente escolha a conta
    return cliente.contas[0]

def depositar(clientes):
    cpf = input(message_default("Informe o CPF do cliente: "))
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print(message_erro("Cliente não encontrato! "))
        return
    
    valor = float(input(message_default("Informe o valor de depósito: ")))
    transacao = Deposito(valor)

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return
    
    cliente.realizar_transacao(conta, transacao)

def sacar(clientes):
    cpf = input(message_default("Informe o CPF do cliente: "))
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print(message_erro("Cliente não encontrado!"))
        return
    
    valor = float(input(message_default("Informe o valor do saque: ")))
    transacao = Saque(valor)

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return
    
    cliente.realizar_transacao(conta, transacao)


def exibir_extrato(clientes):
    cpf = input(message_default("Informe o CPF do cliente: "))
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print(message_erro("Cliente não encontrado"))
        return
    
    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return
    
    print(message_alert("\n--------------------EXTRATO---------------------"))
    transacoes = conta.historico.transacoes

    extrato = ""
    if not transacoes:
        extrato = message_alert("Não foram realizadas movimentações")
    else:
        for transacao in transacoes:
            extrato += message_alert(f"\n{transacao['tipo']} - Data:{transacao['data']}: \n \tR$ {transacao['valor']:.2f}\n")

    print(extrato)
    print(message_alert(f"\nSaldo: \n\tR$ {conta.saldo:.2f}"))
    print(message_alert("\n-------------------------------------------------"))


def criar_conta(numero_conta, clientes, contas):
    cpf = input(message_default("Informe o CPF do cliente: "))
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print(message_erro("Cliente não encontrado, fluxo de criação de conta encerrado!"))
        return
    
    conta = ContaCorrente.nova_conta(cliente=cliente,numero=numero_conta)
    contas.append(conta)
    cliente.contas.append(conta)

    print(message_success("----- Conta criada com sucesso! -----"))

def listar_contas(contas):
    for conta in contas:
        print(message_alert(" = " * 100))
        print(message_alert(textwrap.dedent(str(conta))))

def criar_cliente(clientes):
    cpf = input(message_default("Informe o CPF (somente números): "))
    cliente = filtrar_cliente(cpf, clientes)

    if cliente:
        print(message_erro("Já existe cliente com esse CPF!"))
        return
    
    nome = input(message_default("Informe o nome completo: "))
    data_nascimento = input(message_default("Informe a data de nascimento (dd-mm-aaaa): "))
    endereco = input(message_default("Informe endereço (logradouro, nro - bairro - cidade/sigla estado): "))

    cliente = Pessoa_fisica(nome=nome, data_nascimento=data_nascimento, cpf=cpf, endereco=endereco)

    clientes.append(cliente)

    print(message_success("----- Cliente cadastrado com sucesso! -----"))


def main():
    clientes = []
    contas = []

    while True:
        opcao = menu()
        if opcao.lower() == 'd':
            depositar(clientes)

        elif opcao.lower() == 's':
            sacar(clientes)

        elif opcao.lower() == 'e':
            exibir_extrato(clientes)

        elif opcao.lower() == 'nu':
            criar_cliente(clientes)

        elif opcao.lower() == 'nc':
            numero_conta = len(contas) + 1
            criar_conta(numero_conta, clientes, contas)

        elif opcao.lower() == 'lc':
            listar_contas(contas)

        elif opcao.lower() == 'q':
            print(message_esc("Obrigado por usar nosssos serviços!\nVolte Sempre! ❤"))
            break

        else:
            print(message_erro("Operação inválida, por favor seleciona novamente a operação desejada."))


#VER listar contas 13:00
main()
# class Banco:
#     usuarios = []
#     contas = []
#     def __init__(self):
#         pass






