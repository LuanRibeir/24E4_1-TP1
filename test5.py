# A seguinte função encontra o maior número único dentro de um array,
# mas tem uma eficiência de O(N²). Reescreva a função para que se torne uma eficiência O(N):

def greatesNumberExemple(array):
    for i in array:
        # Assume for now that i is the greatest:
        isIValTheGreatest = True
    
    for j in array:
        # if we find another value that is grater than i,
        # i is not the greatest:
        if j > i:
            isIValTheGreatest = False
    
        #if, by the time we checked all the other numbers, i
        #is still the gratest, it means that i is the grates number:
        if isIValTheGreatest:
            return i
            

def greatestNumber(array):
    # Armazenar a quantidade de cada num
    counts = {}

    # Contar a quantidade de cada num
    for num in array:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1

    # Encontrar o maior num unico
    greatestUnique = None
    for num in counts:
        if counts[num] == 1:  # Verifica se o num é unico
            if greatestUnique is None or num > greatestUnique:
                greatestUnique = num

    return greatestUnique

array = [4, 1, 2, 81, 81, 3, 80]
print(greatestNumber(array))
