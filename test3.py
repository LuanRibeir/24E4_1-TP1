# Quantos passos seriam necessários para realizar uma busca linear pelo número 8 no array ordenado, [2, 4, 6, 8, 10, 12, 13]?

numeros = [2, 4, 6, 8, 10, 12, 13]
alvo = 8
passos = 0 

for i in range(len(numeros)):
    passos += 1  
    if numeros[i] == alvo:  
        print(f"Id: {i}, Passos: {passos}")