nome = "Pedro"
idade = "20"
profissao = "Programador"
linguagem = "Python"
saldo = 45.525

#old style (parece JAVA)
print("Nome: %s , Idade: %s" % (nome, idade))

#metodo format
print("Nome: {}, Idade: {}, profissao: {}, linguagem de programacao: {}". format(nome, idade, profissao, linguagem)) #parece o oldstyle
print("Nome: {0}, Idade: {1}, profissao: {2}, linguagem de programacao: {3}". format(nome, idade, profissao, linguagem)) #mais usual, ja que eu posso apenas colocar chaves e a posicao dela
print("Nome: {nome} , Idade: {idade}" . format(nome=nome, idade=idade)) #ao inves de numero pode so nomear eles

#f-string - pega a variavel em si
print(f"Nome: {nome} , Idade: {idade}, Saldo: {saldo:10.2f}")