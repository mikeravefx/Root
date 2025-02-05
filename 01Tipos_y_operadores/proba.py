def piramide(altura: int) -> None:
    # Esta función imprime una pirámide de números con la altura especificada.
    # Parámetro:
    # altura (int): la altura de la pirámide, que determina cuántas filas tendrá.
    for fila in range(1, altura + 1):
        # Este bucle 'for' itera desde 1 hasta la 'altura' (inclusive).
        # Cada iteración representa una fila de la pirámide.
        print(" " * (altura - fila), end="")
        # Imprime los espacios en blanco necesarios para alinear los números correctamente.
        # La cantidad de espacios disminuye a medida que la fila aumenta.
        # 'altura - fila' determina el número de espacios antes de los números en cada fila.
        # 'end=""' evita que se inserte una nueva línea después de los espacios, permitiendo que los números se impriman en la misma línea.
        for columna in range(fila, 0, -1):
            # Este bucle 'for' itera desde el valor de 'fila' hasta 1 (inclusive) en orden decreciente.
            # Cada iteración representa un número en la fila actual de la pirámide.
            print(columna, end="")
