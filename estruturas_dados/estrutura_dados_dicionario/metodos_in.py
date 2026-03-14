contatos = {
    "pedro@gmmail.com":{"nome": "Pedro", "telefone": "3333-2121"},
    "marcos@gmmail.com":{"nome":"Marcos", "telefone": "333-2121"},
    "vinicius@gmmail.com":{"nome":"Vinicius", "telefone": "333-2121"},
    "leandro@gmmail.com":{"nome":"Leandro", "telefone": "333-2121"},
    "marcelo@gmmail.com":{"nome":"Mercelo", "telefone": "333-2121"},
}

#retorna se um valor esta presente no dicionario
resultado = "leandro@gmmail.com" in contatos #True
print(resultado)

resultado = "barbara@gmmail.com" in contatos #False
print(resultado)

resultado = "idade" in contatos["leandro@gmmail.com"] #False
print(resultado)

resultado = "telefone" in contatos["pedro@gmmail.com"] #True
print(resultado)

