"""cola.py - Cola (queue) sobre lista enlazada con head y tail. Principio FIFO."""


class NodoCola:
    """Nodo de la cola: guarda un dato y la referencia al siguiente."""

    def __init__(self, dato, siguiente=None):
        self.dato = dato
        self.siguiente = siguiente


class Cola:
    """Cola con head (frente) y tail (final).

    Mantener tail permite insertar al final sin recorrer la lista,
    por eso enqueue y dequeue son O(1).
    """

    def __init__(self):
        self.head = None
        self.tail = None
        self.tamano = 0

    def esta_vacia(self):           # esta_vacia: O(1)
        return self.head is None

    def enqueue(self, dato):        # enqueue: O(1) -> se enlaza tras tail
        nuevo = NodoCola(dato)
        if self.esta_vacia():
            self.head = self.tail = nuevo
        else:
            self.tail.siguiente = nuevo
            self.tail = nuevo
        self.tamano += 1

    def dequeue(self):              # dequeue: O(1) -> se retira head
        if self.esta_vacia():
            return None
        dato = self.head.dato
        self.head = self.head.siguiente
        if self.head is None:       # la cola quedó vacía: tail también
            self.tail = None
        self.tamano -= 1
        return dato

    def enqueue_frente(self, dato):  # enqueue_frente: O(1) -> se inserta antes de head
        """Reinserta al frente. Se usa para deshacer una atención."""
        nuevo = NodoCola(dato, self.head)
        self.head = nuevo
        if self.tail is None:
            self.tail = nuevo
        self.tamano += 1

    def quitar_ultimo(self):        # quitar_ultimo: O(n) -> hay que hallar el penúltimo
        """Elimina el último nodo. Se usa para deshacer un registro de turno.

        Es O(n) porque la lista es simplemente enlazada: no hay referencia
        'anterior' desde tail, así que se recorre desde head.
        """
        if self.esta_vacia():
            return None
        if self.head is self.tail:
            dato = self.head.dato
            self.head = self.tail = None
        else:
            actual = self.head
            while actual.siguiente is not self.tail:
                actual = actual.siguiente
            dato = self.tail.dato
            actual.siguiente = None
            self.tail = actual
        self.tamano -= 1
        return dato

    def peek(self):                 # peek: O(1)
        return None if self.esta_vacia() else self.head.dato

    def recorrer(self):             # recorrer: O(n)
        datos, actual = [], self.head
        while actual is not None:
            datos.append(actual.dato)
            actual = actual.siguiente
        return datos


def prueba_cola():
    """Caso de prueba: el primero en llegar es el primero en salir."""
    c = Cola()
    assert c.esta_vacia() and c.dequeue() is None
    c.enqueue(1); c.enqueue(2); c.enqueue(3)
    assert c.peek() == 1 and c.tamano == 3
    assert c.dequeue() == 1 and c.dequeue() == 2
    assert c.quitar_ultimo() == 3 and c.esta_vacia() and c.tail is None
    c.enqueue_frente(9)
    assert c.head is c.tail and c.peek() == 9
    print("[OK] Prueba de COLA (FIFO)")


if __name__ == "__main__":
    prueba_cola()
