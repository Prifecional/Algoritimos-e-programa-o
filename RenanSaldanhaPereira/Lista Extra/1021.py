valor = float(input(""))


moedas = [1,0.50,0.25,0.10,0.05,0.01]
notas = [100, 50, 20, 10, 5, 2]

print("NOTAS:")
for nota in notas:
    quantidade_nota = int(valor / nota)
    print("%i nota(s) de R$ %.2f" %(quantidade_nota,nota))
    valor -= quantidade_nota * nota

print("MOEDAS:")
for moeda in moedas:
    quantidade_moeda = int(valor / moeda)
    print("%i moeda(s) de R$ %.2f"%(quantidade_moeda,moeda))
    valor -= quantidade_moeda * moeda
