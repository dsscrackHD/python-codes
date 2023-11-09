#7-Generar 3 vectores de 20 posiciones cada una, en el primer vector
#almacenar 20 números (generar dichos números de forma aleatoria en el
#rango de 10 a 250), en los otros dos (2) vectores, en el primero almacenar
#los numeros pares del primer vector, los impares en el tercer vector.

vector1 = [i for i in range(10, 30)]

vector2 = []
vector3 = []

for num in vector1:
    if num % 2 == 0:
        vector2.append(num)
    else:
        vector3.append(num)

print("Vector 1:", vector1)
print("Vector 2 (pares):", vector2)
print("Vector 3 (impares):", vector3)