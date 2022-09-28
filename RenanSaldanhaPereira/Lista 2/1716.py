#https://www.beecrowd.com.br/judge/pt/custom-problems/fullscreen/1716

plano = (input(""))
n1 = float(input(""))

porcA = (1 + 10/100) * n1
porcB = (1 + 15/100) * n1
porcC = (1 + 20/100) * n1

if plano == "A":
    print("Novo salário: R$%.2f" % porcA)

elif plano == "B":
    print("Novo salário : R$%.2f" % porcB)

else:
    print("Novo salário: R$%.2F" % porcC)
