#dicionario no python
pessoa = {"nome": "Pedro", "idade":20} #sem usar o dict
print(pessoa)

pessoa = dict (nome="Pedro", idade=20) #usando o dict 
print (pessoa)

#acesso aos dados
pessoa["nome"] #assim voce chama o dado
print(pessoa["nome"]) 

pessoa["telefone"] = "3333-1234" #para adicionar mais informacoes 
print(pessoa)