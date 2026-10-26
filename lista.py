"""lista.py - Lista simplemente enlazada con los clientes registrados."""


class Cliente:
    """Datos del cliente: DNI y nombre."""

    def __init__(self, dni, nombre):
        self.dni = dni
        self.nombre = nombre

    def __str__(self):
        return f"{self.nombre} (DNI {self.dni})"


class NodoLista:
    """Nodo de la lista: guarda un Cliente y la referencia al siguiente."""

    def __init__(self, cliente, siguiente=None):
        self.cliente = cliente
        self.siguiente = siguiente


class ListaClientes:
    """Lista simplemente enlazada; solo guarda la referencia a la cabeza."""

    def __init__(self):
        self.cabeza = None
        self.tamano = 0

    def agregar(self, cliente):     # agregar: O(n) -> recorre para validar DNI y llegar al final
        """Agrega al final. Devuelve False si el DNI ya existe."""
        if self.buscar_por_dni(cliente.dni) is not None:
            return False
        nuevo = NodoLista(cliente)
        if self.cabeza is None:
            self.cabeza = nuevo
        else:
            actual = self.cabeza
            while actual.siguiente is not None:
                actual = actual.siguiente
            actual.siguiente = nuevo
        self.tamano += 1
        return True

    def buscar_por_nombre(self, nombre):   # buscar_por_nombre: O(n) -> peor caso recorre toda la lista
        """Devuelve todos los clientes cuyo nombre coincide (sin mayúsculas)."""
        encontrados, actual = [], self.cabeza
        while actual is not None:
            if actual.cliente.nombre.lower() == nombre.lower():
                encontrados.append(actual.cliente)
            actual = actual.siguiente
        return encontrados

    def buscar_por_dni(self, dni):         # buscar_por_dni: O(n)
        actual = self.cabeza
        while actual is not None:
            if actual.cliente.dni == dni:
                return actual.cliente
            actual = actual.siguiente
        return None

    def mostrar(self):                     # mostrar: O(n) -> recorre desde la cabeza
        clientes, actual = [], self.cabeza
        while actual is not None:
            clientes.append(actual.cliente)
            actual = actual.siguiente
        return clientes


def prueba_lista():
    """Caso de prueba: agregar, buscar por nombre y recorrer."""
    lista = ListaClientes()
    assert lista.agregar(Cliente("111", "Ana"))
    assert lista.agregar(Cliente("222", "Luis"))
    assert not lista.agregar(Cliente("111", "Otra"))      # DNI repetido
    assert [c.dni for c in lista.buscar_por_nombre("luis")] == ["222"]
    assert lista.buscar_por_nombre("Zoe") == []
    assert [c.nombre for c in lista.mostrar()] == ["Ana", "Luis"]
    print("[OK] Prueba de LISTA ENLAZADA")


if __name__ == "__main__":
    prueba_lista()
