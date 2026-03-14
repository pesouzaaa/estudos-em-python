contatos = {"marcelo@gmmail.com":{"nome":"Mercelo", "telefone": "333-2121"}}
print(contatos)

#ele remove a chave
resultado = contatos.pop("marcelo@gmmail.com") 
print(resultado)

resultado = contatos.pop("marcelo@gmmail.com", {}) 
print(resultado)