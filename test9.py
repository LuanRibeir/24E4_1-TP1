# Escreva uma função em Python que implemente o algoritmo
# Bubble Sort para ordenar uma lista de números em ordem crescente.
# Em seguida, teste a função com diferentes listas de números e 
# verifique se ela está ordenando corretamente.

def bubbleSort(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:  
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                

testes = [
    [1, 2, 3, 4, 5], 
    [64, 55, 25, 12, 23, 17, 90],
    [5, 92, 465, 2, 8],
    [5, 4, 3, 2, 1],  
    [55]            
]

for lista in testes:
    print("Lista:", lista)
    bubbleSort(lista)
    print(f"Lista ordenada: {lista} \n")    