#https://www.beecrowd.com.br/judge/pt/custom-problems/fullscreen/1737

soma = 0
cont = 0
quantidade = int(input(""))

if quantidade <= 0:
    print("Informe uma quantidade > 0!")
else:
    while cont < quantidade:
        numero = float(input(""))
        soma = soma + numero
        cont = cont + 1

    print("Soma dos números informados: %.2f"% soma)