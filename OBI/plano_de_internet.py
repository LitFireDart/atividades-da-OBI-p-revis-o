x = int(input())
n = int(input())

for i in range(n):
    consumo = int(input())
    x = x - consumo + x

print(x)