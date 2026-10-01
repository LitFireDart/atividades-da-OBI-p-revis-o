número = int(input())

frase1 = input()
frase2 = input()

frase1 = frase1.replace(" ", "").replace(",", "").replace(".", "")
frase2 = frase2.replace(" ", "").replace(",", "").replace(".", "")

if sorted(frase1) == sorted(frase2):
    print("S")
else:
    print("N")