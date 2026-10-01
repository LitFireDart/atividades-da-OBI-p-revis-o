número = int(input())

aprovados = []

for i in range(número):
    estado, alcool, gasolina = input().split()

    alcool = float(alcool)
    gasolina = float(gasolina)

    if alcool <= gasolina * 0.7:
        aprovados.append(estado)

if aprovados:
    print(*aprovados)
else:
    print("*")