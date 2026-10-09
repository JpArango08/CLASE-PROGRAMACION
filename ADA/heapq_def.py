import heapq

# ============================================================
# HEAPQ
# ============================================================
# heapq permite trabajar con "montículos" (heaps).
# Por defecto, Python usa un MIN-HEAP:
# el elemento más pequeño siempre queda en la posición [0].

# ------------------------------------------------------------
# 1. CREAR UN HEAP
# ------------------------------------------------------------

heap = []

# Agregar elementos al heap
heapq.heappush(heap, 5)
heapq.heappush(heap, 2)
heapq.heappush(heap, 8)
heapq.heappush(heap, 1)

print(heap)
# El menor elemento siempre está en heap[0]


# ------------------------------------------------------------
# 2. heappush()
# ------------------------------------------------------------
# Agrega un elemento manteniendo la estructura del heap.

heapq.heappush(heap, 3)


# ------------------------------------------------------------
# 3. heappop()
# ------------------------------------------------------------
# Elimina y devuelve el elemento MÁS PEQUEÑO.

menor = heapq.heappop(heap)

print(menor)
# 1


# ------------------------------------------------------------
# 4. heap[0]
# ------------------------------------------------------------
# Permite consultar el elemento más pequeño SIN eliminarlo.

print(heap[0])


# ------------------------------------------------------------
# 5. heapify()
# ------------------------------------------------------------
# Convierte una lista normal en un heap.
# Es más eficiente que hacer muchos heappush().

numeros = [5, 2, 8, 1, 3]

heapq.heapify(numeros)

print(numeros)

# Ahora numeros funciona como un min-heap.


# ------------------------------------------------------------
# 6. heappushpop()
# ------------------------------------------------------------
# Agrega un elemento y después elimina el menor.
# Puede ser más eficiente que hacer push + pop por separado.

resultado = heapq.heappushpop(numeros, 10)


# ------------------------------------------------------------
# 7. heapreplace()
# ------------------------------------------------------------
# Elimina primero el menor y después agrega el nuevo elemento.

resultado = heapq.heapreplace(numeros, 7)


# ------------------------------------------------------------
# 8. nsmallest()
# ------------------------------------------------------------
# Obtiene los N elementos más pequeños.

numeros = [8, 3, 10, 1, 5, 2]

print(heapq.nsmallest(3, numeros))
# [1, 2, 3]


# ------------------------------------------------------------
# 9. nlargest()
# ------------------------------------------------------------
# Obtiene los N elementos más grandes.

print(heapq.nlargest(3, numeros))
# [10, 8, 5]


# ============================================================
# MAX-HEAP
# ============================================================
# heapq no tiene un max-heap tradicional directamente.
# Podemos simularlo usando números negativos.

max_heap = []

heapq.heappush(max_heap, -10)
heapq.heappush(max_heap, -5)
heapq.heappush(max_heap, -20)

# El número más negativo representa el número más grande.

mayor = -heapq.heappop(max_heap)

print(mayor)
# 20


# ============================================================
# EJEMPLO PRÁCTICO: PRIORIDADES
# ============================================================

tareas = []

# (prioridad, tarea)
heapq.heappush(tareas, (2, "Estudiar Python"))
heapq.heappush(tareas, (1, "Entregar trabajo"))
heapq.heappush(tareas, (3, "Jugar"))

# La prioridad 1 sale primero.

print(heapq.heappop(tareas))
# (1, 'Entregar trabajo')