# CarUPS – Gestión de turnos (Unidad 1)

Programa de consola en Python que gestiona los turnos de atención del taller **CarUPS**
integrando tres estructuras lineales implementadas desde cero con nodos: **pila**, **cola** y **lista enlazada**.

## Cómo ejecutarlo

Requiere Python 3.8 o superior. No usa librerías externas.

```bash
python main.py            # menú de consola
python pila.py            # prueba de la pila
python cola.py            # prueba de la cola
python lista.py           # prueba de la lista
```

Las tres pruebas también se ejecutan desde el menú (opción 9).

## Estructuras

| Archivo | Estructura | Requerimiento | Uso en el programa |
|---|---|---|---|
| `pila.py` | Pila (LIFO) con nodos y referencia al tope | R1 | Historial de acciones; `pop` deshace la última acción |
| `cola.py` | Cola (FIFO) sobre lista enlazada con `head` y `tail` | R2 | Turnos en orden de llegada |
| `lista.py` | Lista simplemente enlazada con `cabeza` | R3 | Clientes registrados (DNI y nombre) |
| `main.py` | Menú de consola | – | Integra las tres estructuras |

**Pila (R1).** LIFO es adecuado porque la acción que se deshace es siempre la más reciente.
**Cola (R2).** Con `tail`, `enqueue` no recorre la lista; con `head`, `dequeue` retira el primero: ambas son O(1).
**Lista (R3).** Cada nodo guarda un `Cliente` y apunta al siguiente; se recorre desde la cabeza.

### Cómo se deshace cada acción

- `REGISTRAR` (solicitar turno): se quita el último nodo de la cola. El cliente sigue en la lista de registrados.
- `ATENDER`: el cliente vuelve al frente de la cola (`enqueue_frente`).

## Tabla de complejidades

| Estructura | Operación | Complejidad | Justificación |
|---|---|---|---|
| Pila | `push` | O(1) | Solo crea un nodo y actualiza el tope |
| Pila | `pop` | O(1) | Solo retira el tope |
| Pila | `peek` | O(1) | Lee el tope sin recorrer |
| Cola | `enqueue` | O(1) | `tail` da acceso directo al final |
| Cola | `dequeue` | O(1) | `head` da acceso directo al frente |
| Cola | `enqueue_frente` | O(1) | Inserta antes de `head` |
| Cola | `quitar_ultimo` | O(n) | Sin enlace al anterior: se recorre hasta el penúltimo |
| Lista | `agregar` | O(n) | Valida DNI único y llega al final recorriendo |
| Lista | `buscar_por_nombre` | O(n) | Peor caso recorre todos los nodos |
| Lista | `mostrar` | O(n) | Visita cada nodo una vez |
