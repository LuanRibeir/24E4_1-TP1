# A seguinte função aceita um array de strings e retorna um novo array 
# que contém apenas as strings que começam com o caractere "a". 
# Use a Notação Big O para descrever a complexidade de tempo da função:

def selectAStrings(array):
    newArray = []

    for i in range(len(array)):
        if array[i].startswith("a"):
            newArray.append(array[i])
    
    return newArray

# O(N)