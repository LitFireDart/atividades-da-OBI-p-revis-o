frase = input().lower()

alfabeto = set("abcdefghijklmnopqrstuvxz")

if alfabeto.issubset(set(frase)):
    print("S")
else:
    print("N")