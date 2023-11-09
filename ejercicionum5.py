#6- Almacenar en un vector 25 números (generar dichos números de forma
#aleatoria en el rango de 1 a 100), imprimir las posiciones donde se
#encuentre un numero par.
# Crear el vector

vector = []
for i in range(1, 26):
    vector.append(i)

print("Vector:", vector)

pares = []
for i in range(len(vector)):
    if vector[i] % 2 == 0:
        pares.append(str(i))

resultado = ",".join(pares)
print("Índices de números pares:", resultado)