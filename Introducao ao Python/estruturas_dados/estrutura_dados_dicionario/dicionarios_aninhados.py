#assim que declara um dicionario aninhado
contatos = {
    "pedro@gmmail.com":{"nome": "Pedro", "telefone": "3333-2121"},
    "marcos@gmmail.com":{"nome":"Marcos", "telefone": "333-2121"},
    "vinicius@gmmail.com":{"nome":"Vinicius", "telefone": "333-2121"},
    "leandro@gmmail.com":{"nome":"Leandro", "telefone": "333-2121"},
    "marcelo@gmmail.com":{"nome":"Mercelo", "telefone": "333-2121"},
}
#assim chama os dados - O primeiro colchete chama o dicionario
contatos["leandro@gmmail.com"]["telefone"] #o primeiro colchete chama o dicionario, o segundo o dados
print(contatos["leandro@gmmail.com"]["telefone"])
