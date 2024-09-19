# Desafio
Fazer uma aplicação em Python que simule o funcionamento de um banco, com as seguintes caracteristicas:

### **Saque**
A função `saque` deve receber os argumentos apenas por nome (_keyword only_).  
**Sugestão de argumentos**: saldo, valor, extrato, limite, numero_saques, limites_saques.  
**Sugestão de retorno**: saldo e extrato.

---

### **Depósito**
A função `depósito` deve receber os argumentos apenas por posição (_positional only_).  
**Sugestão de argumentos**: saldo, valor, extrato.  
**Sugestão de retorno**: saldo e extrato.

---

### **Extrato**
A função `extrato` deve receber os argumentos por posição e nome (_positional only_ e _keyword only_).  
**Argumentos posicionais**: saldo.  
**Argumentos nomeados**: extrato.

---

### **Novas Funções**
Precisamos criar duas novas funções: `criar usuário` e `criar conta corrente`. Fique à vontade para adicionar mais funções, exemplo: **listar contas**.

---

### Criar usuário (cliente)
O programa deve armazenar os usuários em uma **list**#, um usuário é composto por: nome, data de nascimento, CPF e endereço. O endereço é uma string com o formato: logradouro, Nº - bairro - cidade/sigla estado. Deve ser armazenado somente os **núemros** do CPF. **Não podemos cadastrar 2 usuários com o mesmo CPF**.

---

#### **Criar usuário (cliente)**
O programa deve armazenar os usuários em uma lista (`list`).  
Um usuário é composto por: nome, data de nascimento, CPF e endereço. O endereço é uma string no formato: _logradouro, número - bairro - cidade/sigla estado_.  
Deve ser armazenado somente os **números do CPF**.  
**Não podemos cadastrar dois usuários com o mesmo CPF**.

---

#### **Criar conta corrente**
O programa deve armazenar as contas em uma lista (`list`).  
Uma conta é composta por: agência, número da conta e usuário. O número da conta é **sequencial**, iniciado em **1**.  
A agência tem um número fixo: `"0001"`.  
Um usuário pode ter **mais de uma conta**, mas uma conta pertence **somente a um usuário**.

---

### **Dicas**
Para vincular um usuário a uma conta, filtre a lista de usuários buscando o número do CPF informado para cada usuário.

---

# Adicionais

#### **Filtro case-sensitive**
Foi adicionado um filtro para que o programa ignore a diferença entre letras maiúsculas e minúsculas, garantindo que a execução do programa não seja afetada.

#### **Adições visuais**
Foram adicionados retoques visuais para melhorar a estética. As mensagens são exibidas com as seguintes cores no terminal:


* <span style="color: BlueViolet; background-color: Gainsboro;">message_default</span>. ➡ Mensagem com uma cor base bem chamativa (roxo 💜).
* <span style="color: green; background-color: Gainsboro;">message_success</span>. ➡ Mensagem com o intuito de informar que está tudo certo (verde 💚).
* <span style="color: red; background-color: Gainsboro;">message_erro</span>. ➡ Mensagem com o intuito de informar ao usuário que algo deu errado (vermelho 💔).
* <span style="color: yellow; background-color: Gainsboro;">message_alert</span>. ➡ Mensagem com o intuito de passar alguma informação importante (amarelo 💛).

----


__<span style="font-size: 12px;">Data de atualização: 19/09/24</span>__
