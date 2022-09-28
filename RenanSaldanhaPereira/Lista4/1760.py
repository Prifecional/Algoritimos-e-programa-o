#https://www.beecrowd.com.br/judge/pt/custom-problems/fullscreen/1760

quilo90 = 0
qtdpessoas = 0
mediaidade = 0
idade = 0

while qtdpessoas < 4:
    idade = int(input(""))
    quilo = float(input(""))
    mediaidade = mediaidade + idade

    qtdpessoas = qtdpessoas + 1
    
    if quilo >= 90:
        quilo90 += 1

media = mediaidade / 4

print("Qtd pessoas > 90kg: %i" % quilo90)
print("Idade Média: %.2f" % media)