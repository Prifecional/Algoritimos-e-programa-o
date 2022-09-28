#https://www.beecrowd.com.br/judge/pt/custom-problems/fullscreen/1714

n1 = float(input(""))
porc1 = (45/100) * n1 + n1
porc2 = (30/100) * n1 + n1

if n1 < 20.00:
    print( "Valor de venda: R$%.2f"%(porc1))
else:
    print( "Valor de venda: R$%.2f"%(porc2))