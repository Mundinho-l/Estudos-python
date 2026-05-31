notaA=float(input("Nota A: "))
notaB=float(input("Nota B: "))

mediafinal=(notaA+notaB)/2

if mediafinal>=7:
    print("A Média: %.1f - Aprovado"%mediafinal)
else:
    print("A Média: %.1f - Reprovado"%mediafinal)