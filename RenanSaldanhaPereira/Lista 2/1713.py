#https://www.beecrowd.com.br/judge/pt/custom-problems/fullscreen/1713


hr = float(input(""))
nm = float(input(""))

salario = hr * nm
renda = (salario * 11/100)
inss = (salario * 8/100)
sindicato = (salario * 5/100)
liquido = salario-renda-inss-sindicato

print("Salário Bruto: R$%.2f"%(salario))
print("Imposto: R$%.2f"%(renda))
print("INSS: R$%.2f"%(inss))
print("Sindicato: R$%.2f"%(sindicato))
print("Líquido: R$%.2f"%(liquido))