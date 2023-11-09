#1- Almacenar 15 números en un vector, calcular e imprimir:
#- El Número mayor.
#- El Número menor
#- Cuantos números menor al promedio hay.
#- Cuantos números positivos hay.
#- Cuantos números ceros hay.
#- Cuantos números negativos hay.
#- Cuantos números pares hay.
#- Cuantos números primos hay.

import random

vector=[random.randint(-10, 10) for _ in range(15)]

num_mayor=max(vector)
num_menor=min(vector)
promedio=sum(vector)/len(vector)

num_menor_promedio=0
num_positivos=0
num_ceros=0
num_negativos=0
num_pares=0
num_primos=0

for num in vector:
    if num <promedio:
        num_menor_promedio+=1
    if num>0:
        num_positivos+=1
    elif num==0:
        num_ceros+=1
    else:
        num_negativos+=1
    if num%2==0:
        num_pares+=1
    if num>1:
        is_prime=True
        for i in range(2,int(num**0.5) + 1):
            if num % i==0:
                is_prime=False
                break
        if is_prime:
            num_primos+=1

print("Vector:",vector)
print("Número mayor:",num_mayor)
print("Número menor:",num_menor)
print("Números menores al promedio:",num_menor_promedio)
print("Números positivos:",num_positivos)
print("Números ceros:",num_ceros)
print("Números negativos:",num_negativos)
print("Números pares:",num_pares)
print("Números primos:",num_primos)