linguagens = ["Python", "Java", "C++", "C"]

sorted(linguagens, key=lambda x: len(x))
print(linguagens)

sorted(linguagens, key=lambda x: len(x), reverse=True)
print(linguagens)