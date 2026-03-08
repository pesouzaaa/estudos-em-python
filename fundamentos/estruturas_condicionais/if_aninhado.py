conta_normal = True
conta_universitaria = False

cheque_especial = 450
saldo = 1000
saque = int(input("Qual sera o valor do saque?"))

if conta_normal:
    if saldo >= saque:
        print("Saque Realizado com sucesso!")
    elif saque <= (saldo + cheque_especial):
        print("Saque Realizado com o uso de cheque especial!")
    else:
        print("Saldo Insuficiente!")
elif conta_universitaria:
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    else:
        print("Saldo Insuficiente!")

else:
    print("Sistema nao reconheceu seu tipo de conta, entre em contato com o seu gerente")
