while True:
    numero = int(input("Digite um número decimal: "))
    binario = format(numero, 'b')
    print("Binário:", binario)

    parar = input("Quer continuar? (s/n): ")
    if parar.lower() == 'n':
        break
