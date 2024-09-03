import json

with open("jsontest.json","r") as f:
    data = json.load(f)

def menor_valor(data): #calcula ignorando os dias com 0 faturamento
    menor = None 
    for item in data["faturamento_mensal"]:
        if item['valor'] == 0:
            continue
        if menor is None or item["valor"] < menor["valor"]:
            menor = item
    return menor['dia']
print(f'A data com menor faturamento foi: {menor_valor(data)}')

def maior_valor(data):
    maior=None
    for item in data["faturamento_mensal"]:
        if maior is None or item["valor"] > maior["valor"]:
            maior = item
    return maior['dia']
print(f'A data com maior faturamento foi: {maior_valor(data)}')

def dias_maior_media(data):
    #Calcular média
    media = 0 
    num_dias=0
    acima_media=0
    for item in data["faturamento_mensal"]:
        if item['valor'] != 0: 
            num_dias+=1
            media += item["valor"]
    media = media/num_dias
    
    for item in data["faturamento_mensal"]:
        if item['valor'] > media:
            acima_media+=1
    
    return acima_media 
print(f'{dias_maior_media(data)} dias com faturamento maior que a média.')