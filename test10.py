# Modifique a função bubbleSort() para que ela ordene uma lista de strings
# em ordem alfabética. Em seguida, teste a função com diferentes
# listas de strings e verifique se ela está ordenando corretamente.

def bubbleSort(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

testes = [
    ["a", "m", "l", "u", "a"],
    ["z", "c", "e", "a", "g"],
    ["m", "b", "c", "d", "f"],
    ["a", "d", "c", "b", "e"],  
]

for lista in testes:
    print("Lista:", lista)
    bubbleSort(lista)
    print(f"Lista ordenada: {lista} \n")  