#https://www.beecrowd.com.br/judge/pt/custom-problems/fullscreen/1734

numero = int(input(""))
soma = numero
fatorial  = 1

while soma > 0:
    fatorial = fatorial * soma
    soma = soma - 1

print("%i! = %i" %(numero,fatorial))