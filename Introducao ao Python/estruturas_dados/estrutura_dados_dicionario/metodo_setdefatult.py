contatos = {"nome":"Mercelo", "telefone": "333-2121"}
print(contatos)

contatos.setdefault("nome", "Marcos") #nao altera pois ja existe
print(contatos)

contatos.setdefault("idade", 20) #altera pois nao existe ainda
print(contatos)