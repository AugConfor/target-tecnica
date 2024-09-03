faturamento_estado = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}
def calcular_percentual(faturamento):
    # Calcula o faturamento total
    resultados=[]
    total = sum(faturamento.values())
    for estado,valor in faturamento.items():
        percentual = (float(valor) / total) * 100
        resultados.append(f"{estado}: {percentual:.2f}%")  
    return resultados 
print(calcular_percentual(faturamento_estado))
