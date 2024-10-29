# No algoritmo Bubble Sort; 
# O índice interno sempre vai da esquerda para a direita, 
# encontrando o maior item e levando-o para a direita. 
# Modifique o método bubbleSort() para que ele seja bidirecional. 
# Isso significa que o índice interno primeiro levará o maior item da esquerda
# para a direita como antes, mas quando alcançar o último, ele se inverterá
# e levará o menor item da direita para a esquerda. 
# Você precisará de dois índices externos, um à direita (o antigo último)
# e outro à esquerda. 

def bubbleSort(self):                           # Ordenar comparando valores adjs.
      for last in range(self.__nItems-1, 0, -1):  # e subir
         for inner in range(last):                # o loop interno vai até o último
            if self.__a[inner] > self.__a[inner+1]:  # Se o item for menor
               self.swap(inner, inner+1)          # que o item adjacente, trocar


def bubbleSortBidirectional(self):
    left = 0
    right = self.__nItems - 1

    while left < right:
        # Movimento da esquerda para a direita
        for i in range(left, right):
            if self.__a[i] > self.__a[i + 1]:
                self.swap(i, i + 1)
        # Reduz o limite superior
        right -= 1

        # Movimento da direita para a esquerda
        for i in range(right, left, -1):
            if self.__a[i] < self.__a[i - 1]:
                self.swap(i, i - 1)
        # Aumenta o limite inferior
        left += 1
        
        
a = [5, 1, 4, 2, 8, 0, 2]
bubbleSortBidirectional(a)