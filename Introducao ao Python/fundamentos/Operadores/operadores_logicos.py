# No "and" as duas precisam ser verdade para ser True
print(True and True) 
print(True and False)
# No "or" basta uma ser verdade para ser True
print(True or True)
print(True or False)
print (False or False)


saldo = 1500
saque = 250
limite = 200
conta_especial = True


#modo nao usual
exp = saldo >= saque and saque <= limite or conta_especial and saldo >= saque
print(exp)

#pode se utiliza, mas nao recomenda-se
exp_2 = (saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)
print (exp_2)


#Melhor forma para realizar, declarar variaveis com as comparacoes. Isso ajuda na identificacao
conta_normal_com_saldo_suficiente = saldo >= saque and saque <= limite 
conta_especial_com_saldo_suficiente = limite or conta_especial and saldo >= saque

exp_3 = conta_normal_com_saldo_suficiente or conta_especial_com_saldo_suficiente
print (exp_3)