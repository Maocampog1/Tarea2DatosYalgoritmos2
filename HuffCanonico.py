# Clase NodoArbol: Representa un nodo en el árbol de Huffman. Cada nodo puede ser una hoja (con un carácter asociado) 
# o un nodo interno que solo tiene una frecuencia y referencias a sus nodos hijos.
class NodoArbol:
    def __init__(self, caracter=None, frecuencia=0, izquierdo=None, derecho=None):
        # Los nodos hojas tendrán un 'caracter' asociado y todos los nodos tendrán una 'frecuencia'.
        self.caracter = caracter  # Carácter almacenado en la hoja (si es nodo hoja).
        self.frecuencia = frecuencia  # Frecuencia de aparición del carácter o suma de las frecuencias (nodo interno).
        self.izquierdo = izquierdo  # Referencia al nodo hijo izquierdo.
        self.derecho = derecho  # Referencia al nodo hijo derecho.

    def __str__(self):
        # Representación en forma de cadena del nodo, útil para mostrar el árbol.
        return f'{self.caracter if self.caracter else "Null"},{self.frecuencia}'


# Función para construir el árbol de Huffman.
# Recibe una lista de frecuencias y devuelve la raíz del árbol de Huffman.
def construir_arbol(frecuencias):
    # Se crea una lista de nodos a partir de las frecuencias dadas.
    nodos = [NodoArbol(caracter, frecuencia) for caracter, frecuencia in frecuencias]
    
    # Construcción del árbol mediante combinación de nodos con menor frecuencia.
    while len(nodos) > 1:
        # Ordenamos los nodos por frecuencia (menor a mayor) para seleccionar los dos más pequeños.
        nodos = sorted(nodos, key=lambda nodo: nodo.frecuencia)
        
        # Seleccionamos los dos nodos con menor frecuencia.
        izquierdo = nodos.pop(0)
        derecho = nodos.pop(0)
        
        # Creamos un nuevo nodo que es la combinación de los dos anteriores.
        # La frecuencia del nuevo nodo es la suma de los nodos hijos.
        nuevo_nodo = NodoArbol(frecuencia=izquierdo.frecuencia + derecho.frecuencia, 
                               izquierdo=izquierdo, derecho=derecho)
        
        # Añadimos el nuevo nodo de vuelta a la lista de nodos.
        nodos.append(nuevo_nodo)
    
    # Al final, solo queda un nodo en la lista, que es la raíz del árbol.
    return nodos[0]


# Función para imprimir el árbol de Huffman de forma visual.
# Muestra la estructura del árbol, mostrando las ramas izquierda y derecha.
def imprimir_arbol_formato(nodo, nivel=0, lado="Root"):
    if nodo:
        indent = "\t" * nivel  # Usamos tabulaciones para mostrar la profundidad del nodo.
        if lado == "Root":
            print(f"{lado}-> {nodo}")  # Nodo raíz.
        else:
            print(f"{indent}{lado}-> {nodo}")  # Nodos hijos (L para izquierdo, R para derecho).
        
        # Llamada recursiva para imprimir los nodos hijos.
        if nodo.izquierdo or nodo.derecho:
            if nodo.izquierdo:
                imprimir_arbol_formato(nodo.izquierdo, nivel + 1, "L")
            if nodo.derecho:
                imprimir_arbol_formato(nodo.derecho, nivel + 1, "R")


# Función para generar los códigos Huffman para cada carácter.
# Realiza un recorrido del árbol, asignando un código binario a cada carácter.
def obtener_codigos_huffman(nodo, codigo_actual="", codigos={}):
    if nodo is None:
        return

    # Si llegamos a una hoja, almacenamos el código actual para ese carácter.
    if nodo.caracter:
        codigos[nodo.caracter] = codigo_actual

    # Llamadas recursivas para las ramas izquierda y derecha.
    # En la izquierda agregamos un '0' al código, y en la derecha un '1'.
    obtener_codigos_huffman(nodo.izquierdo, codigo_actual + "0", codigos)
    obtener_codigos_huffman(nodo.derecho, codigo_actual + "1", codigos)

    # Devolvemos el diccionario que contiene los códigos Huffman.
    return codigos


# Función para calcular las frecuencias de aparición de cada carácter en la palabra.
# Recibe la palabra y devuelve un diccionario con las frecuencias.
def calcular_frecuencias(palabra):
    frecuencias = {}
    for letra in palabra:
        # Si el carácter ya está en el diccionario, aumentamos su frecuencia.
        if letra in frecuencias:
            frecuencias[letra] += 1
        # Si no, lo agregamos con frecuencia 1.
        else:
            frecuencias[letra] = 1
    return frecuencias


# Función para imprimir los códigos Huffman en el orden en que aparecen en la palabra.
# Útil para mostrar los códigos en un formato más comprensible.
def imprimir_codigos_ordenados(codigos_huffman, palabra):
    # Obtenemos los caracteres en el orden en que aparecen por primera vez en la palabra.
    orden_deseado = ''.join(sorted(set(palabra), key=lambda x: palabra.index(x)))
    
    print("\nTabla de códigos Huffman:")
    for caracter in orden_deseado:
        if caracter in codigos_huffman:
            print(f"{caracter} = {codigos_huffman[caracter]}")


# Función para imprimir la tabla de la longitud de los códigos Huffman.
# Muestra la longitud del código asociado a cada carácter.
def imprimir_tabla_longitud_codigos(codigos_huffman, palabra):
    print("\nPALABRA | LONGITUD EN HUFFMAN")
    for caracter in palabra:
        if caracter in codigos_huffman:
            longitud = len(codigos_huffman[caracter])
            print(f"{caracter}       {longitud}")


# Función para imprimir una tabla extendida que incluye detalles adicionales.
# Muestra la letra, longitud del código, y una ID asociada a cada carácter.
def imprimir_tabla_extendida(codigos_huffman, palabra):
    print("\n| LETRA   | LONGITUD EN HUFFMAN | N_ID   |")
    print("+---------+---------------------+---------")
    # Obtenemos los caracteres en el orden en que aparecen en la palabra.
    orden_deseado = ''.join(sorted(set(palabra), key=lambda x: palabra.index(x)))
    
    # Imprimimos la tabla con detalles.
    for i, caracter in enumerate(orden_deseado):
        longitud = len(codigos_huffman[caracter])
        print(f"|   {caracter}     |         {longitud}           |   {i+1}    |")
        print("+---------+---------------------+---------")

    # Mostramos la relación entre 'List Number' y 'First Code'.
    print("\n LIST NUMBER | FIRST CODE | ")
    print("+------------+------------+")
    for i, caracter in enumerate(orden_deseado):
        longitud = len(codigos_huffman[caracter])
        print(f" ({i+1}) -> ({longitud})  |      {codigos_huffman[caracter]}   |")
        print("+------------+------------+")

    # Finalmente, ordenamos las letras de forma lexicográfica y mostramos sus códigos Huffman.
    print("\nOrdenar letras lexicográficamente")
    print("---------------------------------------------->")
    for caracter in sorted(codigos_huffman.keys()):
        print(f"{caracter} = {codigos_huffman[caracter]}")


# Función principal que ejecuta el programa.
def main():
    # Solicitamos al usuario que ingrese una palabra y la convertimos a mayúsculas.
    palabra = input("Por favor ingrese la palabra que desea comprimir (en mayúsculas): ").upper()

    # Calculamos las frecuencias de los caracteres.
    frecuencias = calcular_frecuencias(palabra)

    # Ordenamos las frecuencias de menor a mayor para construir el árbol.
    lista = sorted(frecuencias.items(), key=lambda item: item[1])

    # Mostramos la lista enlazada ordenada por frecuencias.
    print("Lista enlazada ordenada por frecuencia:")
    for caracter, frecuencia in lista:
        print(f"|__{caracter},{frecuencia}__| -> ", end="")
    print("None")

    # Construimos el árbol de Huffman a partir de las frecuencias.
    raiz_arbol_huffman = construir_arbol(lista)

    # Mostramos una representación visual del árbol de Huffman.
    print("\nVisualización del árbol de Huffman:")
    imprimir_arbol_formato(raiz_arbol_huffman)

    # Obtenemos los códigos Huffman para cada carácter.
    codigos_huffman = obtener_codigos_huffman(raiz_arbol_huffman)

    # Imprimimos los códigos Huffman en el orden en que aparecen en la palabra.
    imprimir_codigos_ordenados(codigos_huffman, palabra)

    # Imprimimos la longitud de los códigos Huffman para cada carácter.
    imprimir_tabla_longitud_codigos(codigos_huffman, palabra)

    # Imprimimos una tabla extendida con detalles adicionales.
    imprimir_tabla_extendida(codigos_huffman, palabra)


# Verificamos si el script se está ejecutando directamente y ejecutamos la función principal.
if __name__ == "__main__":
    main()

