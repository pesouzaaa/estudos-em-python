#FIltro VS1
numeros = [1,30, 21, 2, 0 ,65, 34]
pares = []

for numero in numeros:
    if numero % 2==0:
        pares.append(numero)

#FIltro VS2 -> Compreensao
numerosI = [5 , 50, 100, 80, 40, 99, 21, 23]
paresI = [numero for numero in numerosI if numero % 2==0] 