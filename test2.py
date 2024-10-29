# Pegue um baralho de cartas: retire as 13 cartas de espadas,
# reserve o resto e embaralhe as cartas de espadas. 
# Elabore um algoritmo para ordená-las por número sob as seguintes restrições:

# Todas as cartas devem ser seguradas em uma mão. Esta é a "primeira" mão.

# Inicialmente, as cartas embaralhadas estão todas empilhadas com as faces em uma direção, de modo que apenas uma carta seja visível.

# Inicialmente, todas as cartas são seguradas entre o polegar e o indicador da primeira mão.

# A carta visível na pilha pode ser retirada usando a outra mão e colocada entre quaisquer 
# dedos da primeira mão. Ela só pode ser colocada na frente ou atrás das cartas na pilha de cartas entre esses dedos.

# A outra mão pode segurar apenas uma carta por vez e deve colocá-la em algum lugar 
# na primeira mão antes de pegar outra carta visível de uma das pilhas.

# O algoritmo termina quando todas as cartas estão ordenadas em uma única pilha na mão.

import random

def orderCartas():
    # Pilha com 13 cartas de espadas embaralhadas
    espadas = list(range(1, 14))
    random.shuffle(espadas)
    
    # Outra mão (Cartas Ordenadas)
    mao = []
    
    while espadas:
        # Pegar a carta visivel
        cartaVisivel = espadas.pop(0)
                
        # 3, 9  -> 8
        # lenght mao = 2
        # i1: pos = 0 < 2? true and 3 < 8? true -> pos++
        # i2: pos = 1 < 2? true and 9 < 8? false -> insert to pos 1
        
        # Enquanto a posição não for maior que o o numero de cartas na mão
        # E se a carta em mão não for maior a carta visivel
        posicao = 0
        while posicao < len(mao) and mao[posicao] < cartaVisivel:
            posicao += 1
    
        mao.insert(posicao, cartaVisivel)
        print(f"Mão: {mao}")
    
    return mao

orderCartas()