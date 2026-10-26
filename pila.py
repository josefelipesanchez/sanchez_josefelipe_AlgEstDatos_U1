"""pila.py - Pila (stack) implementada con nodos enlazados. Principio LIFO."""


class NodoPila:
    """Nodo de la pila: guarda un dato y la referencia al nodo de abajo."""

    def __init__(self, dato, siguiente=None):
        self.dato = dato
        self.siguiente = siguiente


class Pila:
    """Pila con referencia solo al tope.

    Se usa para el historial de acciones del operador. LIFO es adecuado
    porque la acción que se deshace siempre es la más reciente.
    """

    def __init__(self):
        self.tope = None
        self.tamano = 0

    def esta_vacia(self):       # esta_vacia: O(1)
        return self.tope is None

    def push(self, dato):       # push: O(1) -> solo se modifica el tope
        self.tope = NodoPila(dato, self.tope)
        self.tamano += 1

    def pop(self):              # pop: O(1) -> solo se retira el tope
        if self.esta_vacia():
            return None
        dato = self.tope.dato
        self.tope = self.tope.siguiente
        self.tamano -= 1
        return dato

    def peek(self):             # peek: O(1)
        return None if self.esta_vacia() else self.tope.dato

    def recorrer(self):         # recorrer: O(n) -> visita todos los nodos
        """Devuelve los datos del más reciente al más antiguo."""
        datos, actual = [], self.tope
        while actual is not None:
            datos.append(actual.dato)
            actual = actual.siguiente
        return datos


def prueba_pila():
    """Caso de prueba: el último en entrar es el primero en salir."""
    p = Pila()
    assert p.esta_vacia() and p.pop() is None
    p.push("A"); p.push("B"); p.push("C")
    assert p.peek() == "C" and p.tamano == 3
    assert p.pop() == "C" and p.pop() == "B" and p.pop() == "A"
    assert p.esta_vacia()
    print("[OK] Prueba de PILA (LIFO)")


if __name__ == "__main__":
    prueba_pila()
