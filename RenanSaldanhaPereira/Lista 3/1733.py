#https://www.beecrowd.com.br/judge/pt/custom-problems/fullscreen/1733

nome = input("")
horas_extras = float(input(""))
salario_extra = horas_extras * 10.00
salario_bruto = 3 * 1192.40 + salario_extra
salario_liquido = salario_bruto

if salario_bruto > 2000.00:
      salario_liquido = salario_liquido - (salario_bruto * 0.12)

else:
      salario_liquido = salario_liquido - (salario_bruto * 0.5)

if salario_bruto > 2500:
        salario_liquido = salario_liquido - (salario_bruto * 0.20)
else:
    salario_liquido = salario_liquido * 0


print("Nome: %s" %(nome))
print("Salário bruto: R$%.2f"% salario_bruto)
print("Salário líquido: R$%.2f"% salario_liquido)