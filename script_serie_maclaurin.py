# Importação da biblioteca math e da função "funcao_cosseno_maclaurin":
import math
from funcao_cosseno_maclaurin import funcao_cosseno_maclaurin


# Complete o código a seguir com o valor do penúltimo algarismo do seu RA:
penultimo = 4
# Complete o código a seguir com o valor do último algarismo do seu RA:
ultimo = 1


# A seguir, o script define o valor da precisão a ser utilizada, com base na 
# Tabela fornecida nas instruções.
if penultimo == 0 or penultimo == 9:
    precisao_desejada = 1e-9    
elif penultimo == 1 or penultimo == 8:
    precisao_desejada = 1e-8
elif penultimo == 2 or penultimo == 7:
    precisao_desejada = 1e-7
elif penultimo == 3 or penultimo == 6:
    precisao_desejada = 1e-6
else:
    precisao_desejada = 1e-5
print(precisao_desejada)

# Definição do valor de x:
x = (ultimo+1)/10



# O script chama a função "funcao_cosseno_maclaurin" e recupera os valores das
# suas saídas f e k.
f,k = funcao_cosseno_maclaurin(x,
                               precisao_desejada)


# O script calcula o valor real da diferença entre cos(x) e a aproximação 
# obtida pelo polinômio:
diferenca = math.cos(x) - f

# Impressão dos resultados em tela:
print("Valor da função: ", f)
print("Numero de termos:", k)
print("Diferença entre o valor calculado e o real: ", diferenca)