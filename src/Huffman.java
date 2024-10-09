// Función para construir el árbol de Huffman. 
// Recibe una lista de frecuencias y devuelve la raíz del árbol de Huffman.
import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Scanner;

public class Huffman {
    public static NodoArbol construirArbol(List<NodoArbol> nodos) {
        // Construcción del árbol mediante combinación de nodos con menor frecuencia.
        while (nodos.size() > 1) {
            // Ordenamos los nodos por frecuencia (menor a mayor).
            Collections.sort(nodos, Comparator.comparingInt(n -> n.frecuencia));

            // Seleccionamos los dos nodos con menor frecuencia.
            NodoArbol izquierdo = nodos.remove(0);
            NodoArbol derecho = nodos.remove(0);

            // Creamos un nuevo nodo que es la combinación de los dos anteriores.
            NodoArbol nuevoNodo = new NodoArbol('\0', izquierdo.frecuencia + derecho.frecuencia, izquierdo, derecho);

            // Añadimos el nuevo nodo a la lista de nodos.
            nodos.add(nuevoNodo);
        }

        // Al final, solo queda un nodo en la lista, que es la raíz del árbol.
        return nodos.get(0);
    }

    // Función para imprimir el árbol de Huffman de forma visual.
    // Muestra la estructura del árbol, mostrando las ramas izquierda y derecha.
    public static void imprimirArbolFormato(NodoArbol nodo, int nivel, String lado) {
        if (nodo != null) {
            String indent = "\t".repeat(nivel);  // Usamos tabulaciones para mostrar la profundidad del nodo.
            if (lado.equals("Root")) {
                System.out.println(lado + "-> " + nodo);  // Nodo raíz.
            } else {
                System.out.println(indent + lado + "-> " + nodo);  // Nodos hijos (L para izquierdo, R para derecho).
            }

            // Llamada recursiva para imprimir los nodos hijos.
            if (nodo.izquierdo != null || nodo.derecho != null) {
                if (nodo.izquierdo != null) {
                    imprimirArbolFormato(nodo.izquierdo, nivel + 1, "L");
                }
                if (nodo.derecho != null) {
                    imprimirArbolFormato(nodo.derecho, nivel + 1, "R");
                }
            }
        }
    }

    // Función para generar los códigos Huffman para cada carácter.
    // Realiza un recorrido del árbol, asignando un código binario a cada carácter.
    public static void obtenerCodigosHuffman(NodoArbol nodo, String codigoActual, Map<Character, String> codigos) {
        if (nodo == null) return;

        // Si llegamos a una hoja, almacenamos el código actual para ese carácter.
        if (nodo.caracter != '\0') {
            codigos.put(nodo.caracter, codigoActual);
        }

        // Llamadas recursivas para las ramas izquierda y derecha.
        obtenerCodigosHuffman(nodo.izquierdo, codigoActual + "0", codigos);
        obtenerCodigosHuffman(nodo.derecho, codigoActual + "1", codigos);
    }

    // Función para calcular las frecuencias de aparición de cada carácter en la palabra.
    public static Map<Character, Integer> calcularFrecuencias(String palabra) {
        Map<Character, Integer> frecuencias = new HashMap<>();
        for (char letra : palabra.toCharArray()) {
            frecuencias.put(letra, frecuencias.getOrDefault(letra, 0) + 1);
        }
        return frecuencias;
    }

    // Función para imprimir los códigos Huffman en el orden en que aparecen en la palabra.
    public static void imprimirCodigosOrdenados(Map<Character, String> codigosHuffman, String palabra) {
        System.out.println("\nTabla de códigos Huffman:");
        palabra.chars().distinct().forEach(c -> {
            if (codigosHuffman.containsKey((char) c)) {
                System.out.println((char) c + " = " + codigosHuffman.get((char) c));
            }
        });
    }

    // Función principal que ejecuta el programa.
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // Solicitamos al usuario que ingrese una palabra y la convertimos a mayúsculas.
        System.out.print("Por favor ingrese la palabra que desea comprimir (en mayúsculas): ");
        String palabra = sc.nextLine().toUpperCase();

        // Calculamos las frecuencias de los caracteres.
        Map<Character, Integer> frecuencias = calcularFrecuencias(palabra);

        // Creamos la lista de nodos a partir de las frecuencias.
        List<NodoArbol> lista = new ArrayList<>();
        frecuencias.forEach((caracter, frecuencia) -> lista.add(new NodoArbol(caracter, frecuencia)));

        // Construimos el árbol de Huffman.
        NodoArbol raizArbolHuffman = construirArbol(lista);

        // Mostramos una representación visual del árbol de Huffman.
        System.out.println("\nVisualización del árbol de Huffman:");
        imprimirArbolFormato(raizArbolHuffman, 0, "Root");

        // Obtenemos los códigos Huffman para cada carácter.
        Map<Character, String> codigosHuffman = new HashMap<>();
        obtenerCodigosHuffman(raizArbolHuffman, "", codigosHuffman);

        // Imprimimos los códigos Huffman en el orden en que aparecen en la palabra.
        imprimirCodigosOrdenados(codigosHuffman, palabra);
    }
}