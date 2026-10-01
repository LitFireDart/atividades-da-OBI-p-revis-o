import json

json_data = {"nome": "nome", "telefone": "telefone", "email": "email"}

with open("dados.json", "w") as json_file:
    json.dump(json_data, json_file)

print("dado salvo com sucesso no arquivo dados.json")