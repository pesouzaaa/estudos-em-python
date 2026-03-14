# Lê a linha de entrada e separa os produtos em uma lista
produtos = input().strip().split()

mais_frequente = None
maior_contagem = -1

for produto in produtos:
    contagem = produtos.count(produto)

    if contagem > maior_contagem:
        maior_contagem = contagem
        mais_frequente = produto
        
print(mais_frequente)