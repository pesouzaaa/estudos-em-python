maior_idade = 18
idade_especial = 16

idade = int(input("Informe a sua idade: "))

#primeiro caso: if
if idade >= maior_idade:
    print("Maior de idade, pode tirar a CNH.")
if idade < maior_idade:
    print("menor de idade, nao pode tirar a CNH.")

#segundo caso: if/else
if idade >= maior_idade:
    print("Maior de idade, pode tirar a CNH.")
else:
    print("menor de idade, nao pode tirar a CNH.")

#terceiro caso: if/elif/else

if idade >= maior_idade:
    print("Maior de idade, pode tirar a CNH.")
elif idade >= idade_especial and idade < maior_idade:
    print("Idade especial. faz aula teorica, mas nao pode tirar a CNH.")
else:
    print("menor de idade, nao pode tirar a CNH.")



