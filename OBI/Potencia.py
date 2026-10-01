n = int(input())

soma = 0

for i in range(n):
    t = int(input())

    expoente = t % 10
    base = t // 10

    soma += base ** expoente

print(soma)