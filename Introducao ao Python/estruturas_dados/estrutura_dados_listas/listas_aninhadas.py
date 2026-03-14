#listas aninhadas
matriz = [
    [1, "a", 2],
    ["b", 3, 4],
    [6, 5, "c"]
]
print(matriz[0]) #seleciona a linha da matriz -> [1, "a", 2]
print(matriz[0][0]) #seleciona a linha e o elemento da matriz -> [1]
print(matriz[0][-1]) #seleciona a linha normal e o elemento em indice negativo-> [2]
print(matriz[-1][-1]) #seleciona a linha e o elemento em indice negativo-> [c]
