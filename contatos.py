import json

with open("dados.json", "r") as json_file:
    contato = json.load(json_file)

print(f"Nome: {contato['nome']}, Telefone: {contato['telefone']}, Email: {contato['email']}")