#sort -> Ele ordena por ordem alfabetica
linguagens = ["Python", "Java", "C++", "C"] 
linguagens.sort()
print(linguagens)

#reverse -> Ele ordena por ordem alfabetica espelho
linguagens = ["Python", "Java", "C++", "C"]
linguagens.sort(reverse=True)
print(linguagens)

#key -> Ele ordena por ordem de tamanho
linguagens = ["Python", "Java", "C++", "C"]
linguagens.sort(key=lambda x: len(x))
print(linguagens)

#Ele ordena por ordem tamnho espelho
inguagens = ["Python", "Java", "C++", "C"]
linguagens.sort(key=lambda x: len(x), reverse=True)
print(linguagens)