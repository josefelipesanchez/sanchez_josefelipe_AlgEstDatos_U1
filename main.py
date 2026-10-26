"""main.py - Gestión de turnos del taller CarUPS (pila + cola + lista enlazada)."""

from pila import Pila, prueba_pila
from cola import Cola, prueba_cola
from lista import ListaClientes, Cliente, prueba_lista

clientes = ListaClientes()   # R3: clientes registrados
turnos = Cola()              # R2: turnos en orden de llegada (FIFO)
historial = Pila()           # R1: acciones para deshacer (LIFO)


def pedir_texto(mensaje):
    """Pide un texto y repite la pregunta si viene vacío."""
    while True:
        valor = input(mensaje).strip()
        if valor:
            return valor
        print("  El valor no puede estar vacío.")


def pedir_dni():
    while True:
        dni = pedir_texto("DNI: ")
        if dni.isdigit():
            return dni
        print("  El DNI debe contener solo números.")


def registrar_cliente():
    cliente = Cliente(pedir_dni(), pedir_texto("Nombre: "))
    if clientes.agregar(cliente):
        print(f"  Cliente registrado: {cliente}")
    else:
        print("  Ya existe un cliente con ese DNI.")


def buscar_cliente():
    encontrados = clientes.buscar_por_nombre(pedir_texto("Nombre a buscar: "))
    if encontrados:
        for c in encontrados:
            print("  Encontrado:", c)
    else:
        print("  No se encontró ningún cliente con ese nombre.")


def mostrar_clientes():
    lista = clientes.mostrar()
    if not lista:
        print("  No hay clientes registrados.")
    for i, c in enumerate(lista, 1):
        print(f"  {i}. {c}")


def solicitar_turno():
    dni = pedir_dni()
    cliente = clientes.buscar_por_dni(dni)
    if cliente is None:                      # cliente nuevo: se registra al vuelo
        cliente = Cliente(dni, pedir_texto("Cliente nuevo. Nombre: "))
        clientes.agregar(cliente)
    turnos.enqueue(cliente)
    historial.push(("REGISTRAR", cliente))   # se guarda la acción para poder deshacerla
    print(f"  Turno #{turnos.tamano} registrado para {cliente}")


def atender():
    cliente = turnos.dequeue()
    if cliente is None:
        print("  No hay turnos en espera.")
        return
    historial.push(("ATENDER", cliente))
    print(f"  Atendiendo a {cliente}")


def mostrar_cola():
    espera = turnos.recorrer()
    if not espera:
        print("  La cola de turnos está vacía.")
    for i, c in enumerate(espera, 1):
        print(f"  {i}. {c}")


def deshacer():
    accion = historial.pop()                 # LIFO: siempre la acción más reciente
    if accion is None:
        print("  No hay acciones para deshacer.")
        return
    tipo, cliente = accion
    if tipo == "REGISTRAR":
        turnos.quitar_ultimo()               # el turno recién creado está al final
        print(f"  Deshecho: se canceló el turno de {cliente}")
    else:
        turnos.enqueue_frente(cliente)       # vuelve al frente, donde estaba
        print(f"  Deshecho: {cliente} regresa al frente de la cola")


def ver_historial():
    acciones = historial.recorrer()
    if not acciones:
        print("  Historial vacío.")
    for tipo, cliente in acciones:
        print(f"  {tipo}: {cliente}")


def ejecutar_pruebas():
    prueba_pila()
    prueba_cola()
    prueba_lista()


OPCIONES = {
    "1": ("Registrar cliente", registrar_cliente),
    "2": ("Buscar cliente por nombre", buscar_cliente),
    "3": ("Mostrar clientes registrados", mostrar_clientes),
    "4": ("Solicitar turno", solicitar_turno),
    "5": ("Atender siguiente cliente", atender),
    "6": ("Mostrar cola de turnos", mostrar_cola),
    "7": ("Deshacer última acción", deshacer),
    "8": ("Ver historial de acciones", ver_historial),
    "9": ("Ejecutar pruebas", ejecutar_pruebas),
    "0": ("Salir", None),
}


def main():
    while True:
        print("\n=== TALLER CarUPS - GESTIÓN DE TURNOS ===")
        for clave, (texto, _) in OPCIONES.items():
            print(f"{clave}. {texto}")
        opcion = input("Elija una opción: ").strip()
        if opcion == "0":
            print("Hasta pronto.")
            break
        if opcion in OPCIONES:
            OPCIONES[opcion][1]()
        else:
            print("  Opción no válida.")


if __name__ == "__main__":
    main()
