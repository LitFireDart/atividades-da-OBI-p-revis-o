a = int(input())
b = int(input())
c = int(input())
d = int(input())

d1 = abs((a + b) - (c + d))
d2 = abs((a + c) - (b + d))
d3 = abs((a + d) - (b + c))

print(min(d1, d2, d3))