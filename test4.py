# Quantos passos a busca binária levaria para o exemplo anterior?
# número 8 no array ordenado, [2, 4, 6, 8, 10, 12, 13]

numeros = [2, 4, 6, 8, 10, 12, 13]
alvo = 8

def buscaBinaria(lista, alvo):
    passos = 0 
    i = 0
    fim = len(lista) - 1;
    
    while i <= fim:
        passos += 1
        meio = (i + fim) // 2
        
        if lista[meio] == alvo:
            return meio, passos
        elif lista[meio] > alvo:
            fim = meio - 1
        else:
            i = meio - 1
    return -1, passos

id, passos = buscaBinaria(numeros, 8)
print(f"Id: {id}, Passos: {passos}")