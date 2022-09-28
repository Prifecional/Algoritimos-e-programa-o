#https://www.beecrowd.com.br/judge/pt/custom-problems/fullscreen/1759

ano = int(input(""))
salario = 1000
aumento = 1.5

if ano >= 2006:

    for c in range(2005,ano):
        salario = salario * (aumento/100 + 1)
        aumento = aumento + 1
    print("Salário atual: R$%.2f" % salario)
else:
    print("O ano informado deverá ser > 2005!")
