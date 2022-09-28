#https://www.beecrowd.com.br/judge/pt/custom-problems/fullscreen/1761

valor = 1
total = 0
while valor > 0:
    valor = float(input(""))
    total = total + valor
pago = float(input(""))
troco = pago - total

print("Total da compra: R$%.2f "% total)
print("Valor pago: R$%.2f "% pago)
print("Troco: R$%.2f" %troco)