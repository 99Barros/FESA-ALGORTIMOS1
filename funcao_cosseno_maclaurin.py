def funcao_cosseno_maclaurin(x, precisao_desejada):
    import numpy as np
    import math

    precisao_desejada_alcancada = False
    #Booleana que determina se a estimativa atual está dentro da precisão
    #desejada ou não


    k = 0
    # número de termos da série de Maclaurin considerados até o momento

    f = 0
    #Estimativa da função que queremos calcular, inicializada como 0
    y=0
    #Variável de soma na função
    while not precisao_desejada_alcancada:
        # Aqui, vocês devem implementar o cálculo da função seno a partir
        # da série de MacLaurin, bem como do resto (para verificar se a
        # precisão desejada foi alcançada)
        if k % 2 == 0:
            f += (math.pow(-1,y) / (math.factorial(2*y))) * math.pow(x, 2*y)
            y += 1
        print(f"{f}\n")
        if (1/math.factorial(k+1)) * math.pow(np.abs(x), k+1) <= precisao_desejada:
            break
        k += 1
        # Enquanto a precisão desejada não tiver sido alcançada, 
        # incrementamos o valor de k e adicionamos novos termos ao
        # polinômio.

    return [f,k]