class NodoArbol {
    char caracter;  // Carácter almacenado en la hoja (si es nodo hoja).
    int frecuencia;  // Frecuencia de aparición del carácter o suma de las frecuencias (nodo interno).
    NodoArbol izquierdo;  // Referencia al nodo hijo izquierdo.
    NodoArbol derecho;  // Referencia al nodo hijo derecho.

    // Constructor para nodos
    public NodoArbol(char caracter, int frecuencia, NodoArbol izquierdo, NodoArbol derecho) {
        this.caracter = caracter;
        this.frecuencia = frecuencia;
        this.izquierdo = izquierdo;
        this.derecho = derecho;
    }

    // Constructor para nodo hoja
    public NodoArbol(char caracter, int frecuencia) {
        this(caracter, frecuencia, null, null);
    }

    // Sobrescribimos toString para representar en forma de cadena el nodo, útil para mostrar el árbol.
    @Override
    public String toString() {
        return (caracter != '\0' ? caracter : "Null") + "," + frecuencia;
    }
}