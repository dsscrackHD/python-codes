# 5- Almacenar en un vector 5 números (generar dichos números de forma
#aleatoria en el rango de 1 a 30), por cada número que se encuentre en el
#vector imprimir una serie de *.

vector = [i for i in range(1, 6)]

for num in vector:
    asteriscos = ''
    for _ in range(num):
        asteriscos += '*'
    print(asteriscos)