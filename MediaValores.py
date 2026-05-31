qtd=0
soma=0
media=0
valor = float(input("digite um valor: "))

while (valor > 0.0):
    soma = soma + valor
    qtd = qtd + 1
    valor = float(input("digite um valor: "))

media = soma / qtd
print("\n total da soma: ", soma)
print("\n quantidade de valores digitados: ", qtd)
print("\n média dos valores: ", media)