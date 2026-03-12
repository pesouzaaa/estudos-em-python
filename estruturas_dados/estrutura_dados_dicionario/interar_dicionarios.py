contatos = {
    "pedro@gmmail.com":{"nome": "Pedro", "telefone": "3333-2121"},
    "marcos@gmmail.com":{"nome":"Marcos", "telefone": "333-2121"},
    "vinicius@gmmail.com":{"nome":"Vinicius", "telefone": "333-2121"},
    "leandro@gmmail.com":{"nome":"Leandro", "telefone": "333-2121"},
    "marcelo@gmmail.com":{"nome":"Mercelo", "telefone": "333-2121"},
}

#forma menos usual
for chave in contatos:
   print(chave, contatos[chave])

#mais usal - mesmos resultados da interior
for chave, valor, in contatos.items():
    print(chave, valor)