class Cachorro:
    def __del__(self):
        print("Destruindo a instancia")

c = Cachorro()
del c
        