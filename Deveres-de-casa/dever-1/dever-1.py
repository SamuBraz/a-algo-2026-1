# 1000 elementos:
# insertion sort: 0.01866745948791504
# sorted (função nativa): 5.0067901611328125e-06 (0,000005)

# 5000 elementos:
# insertion sort: 0.3977077007293701
# sorted (função nativa): 3.910064697265625e-05 (0,000039)

# 10000 elementos:
# insertion sort: 1.7140424251556396
# sorted (função nativa): 8.702278137207031e-05 (0,000087)

# 20000 elementos:
# insertion sort: 6.590724229812622
# sorted (função nativa): 0.00017404556274414062 

# 50000 elementos:
# insertion sort: 38.51888084411621 segundos
# sorted (função nativa): 0.0005898475646972656



# é possivel perceber que com 20000 a diferença ficou mais perceptiva, com 5 segundo de diferença, mas o mais notorio é com um array de 50000 que deu uma diferença de 38 segundos
import time
import random


tamanho_rray = 50000

array = [random.randint(0, 100) for _ in range(tamanho_rray)]

array_copia = array


print(len(array))

orginal = array

###insertion sort

tempo_inicial_insertion_sort = time.time()
for i in range(1, len(array), 1):
    temp = array[i]
    if array[i -1] > temp:
        for j in range(i-1, -1, -1):
            if array[j] > temp:
                array[j+1] = array[j]
                array[j] = temp
            else:
                break

tempo_final_insertion_sort= time.time()


print(f"tempo que demorou para rodar o algoritimo de insertion sort com {tamanho_rray} elementos foi de: {tempo_final_insertion_sort - tempo_inicial_insertion_sort}")



tempo_inicial_sorted = time.time()

sorted(array_copia)

tempo_final_sorted= time.time()

print(f"tempo que demorou para rodar a função nativa do python 'sorted' com {tamanho_rray} elementos foi de: {tempo_final_sorted - tempo_inicial_sorted}")