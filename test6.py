# Imagine que você tem um tabuleiro de xadrez e coloca um único grão de arroz em um quadrado.
# No segundo quadrado, você coloca 2 grãos de arroz, já que isso é o dobro da quantidade de arroz
# no quadrado anterior. No terceiro quadrado, você coloca 4 grãos. No quarto quadrado, 
# você coloca 8 grãos, e no quinto quadrado, você coloca 16 grãos, e assim por diante.

# Escreva a função em python que calcula em qual quadrado do tabuleiro você precisará colocar 
# uma determinada quantidade de grãos de arroz. Por exemplo, para 16 grãos, a função retornará 5,
# já que você colocará os 16 grãos no quinto quadrado.

def encontrar_quadrado_para_graos(alvo):
    quadrado = 1
    graos = 1  # Inicia com 1 grão no primeiro quadrado

    while graos < alvo:
        quadrado += 1
        graos *= 2  # Dobra o num de grãos para o proximo quadrado

    return quadrado

# Exemplo de uso
print(encontrar_quadrado_para_graos(16))  # Deve retornar 5

# O(log N)