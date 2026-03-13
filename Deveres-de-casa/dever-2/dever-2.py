### INFORME O NUMERO QUE VAI SER CALCULADO O FATORIAL

#### fatorial 10: 1.7642974853515625e-05(0.000017642974853515625)

#### fatorial 100: 2.9325485229492188e-05(0.000029325485229492188)

#### fatorial de 500: 0.00014472007751464844

#### fatorial de 1000: 0.00028705596923828125


#### A complexidade do algoritimo é linear (O(N)), pois para cada nova entrada será realizado uma operação. Por exemplo:
# fatorial(4)
# fatorial(3)
# fatorial(2)
# fatorial(1)


import time
import sys

numero = 4

sys.setrecursionlimit(2000)


def fatorial(numero):
    if numero == 0:
        return 1
    num_fatorial = fatorial(numero -1)
    return num_fatorial * numero


if __name__ == '__main__':
    tempo_inicial = time.time()
    print(fatorial(numero))
    tempo_final= time.time()
    print(f"tempo que demorou para rodar o algoritimo de calcular fatorial de {numero} foi de: {tempo_final - tempo_inicial}")

