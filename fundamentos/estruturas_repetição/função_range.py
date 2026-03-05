#range(stop)-> range object
#ragen (start, stop[, step]) -> range object

# list (range(0,4))

#exemplo com for:
texto = ""
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")
else: 
    print()

for numero in range(0,53,5):
    print(numero, end=" ")