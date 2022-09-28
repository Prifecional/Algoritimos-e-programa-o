#https://www.beecrowd.com.br/judge/pt/custom-problems/fullscreen/1715

n2 = int(input(""))
n1 = float(input(""))

porc1 = (1 - 13/100) * n1
porc2 = (1 - 7/100) * n1


if n2 == 2:
    print( "Valor total a ser pago: R$%.2f"%(porc1))

elif n2 == 3:
    print("Valor total a ser pago: R$%.2f"%(porc2))

elif n2 == 1:
    print("Valor total a ser pago: R$%.2F"%(n1))

else:
    print("OPÇÃO INVÁLIDA!")
