def shellSort(array):
    # Obtiene la longitud del array
    n = len(array)
    
    # Inicializa el gap (intervalo) para el algoritmo ShellSort
    gap = n // 2

    # Continúa reduciendo el gap hasta que sea 0
    while gap > 0:
        # Itera sobre los elementos desde el gap hasta el final del array
        for i in range(gap, n):
            # Guarda el valor actual en una variable temporal
            temp = array[i]

            # Inicializa la variable j para comparar y mover elementos
            j = i

            # Mueve los elementos del array que están en el intervalo de gap y son mayores que temp
            while j >= gap and array[j - gap] > temp:
                # Desplaza el elemento hacia adelante
                array[j] = array[j - gap]
                # Reduce j en el valor de gap
                j -= gap
            
            # Coloca temp en su posición correcta
            array[j] = temp
        
        # Reduce el gap a la mitad para la siguiente iteración
        gap //= 2

# Pide al usuario el número total de elementos a ordenar
arrayLength = int(input('Ingresa el total de números a ordenar: '))

# Inicializa una lista vacía para almacenar los elementos del array
array = []

# Pide al usuario que ingrese los elementos del array
print('Ingresa los elementos del array:')
for _ in range(arrayLength):
    # Lee cada elemento ingresado por el usuario y lo añade a la lista
    elemento = int(input())
    array.append(elemento)

# Muestra el array original antes de ordenar
print("Array original:", array)

# Llama a la función shellSort para ordenar el array (se pasa como parametro array, una vez lleno)
shellSort(array)

# Muestra el array ordenado después de aplicar ShellSort
print("Array ordenado:", array)