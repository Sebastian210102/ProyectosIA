import heapq

# Mapa de Rumania representado como un grafo
mapa_rumania = {
    'Oradea': [('Zerind', 71), ('Sibiu', 151)],
    'Zerind': [('Oradea', 71), ('Arad', 75)],
    'Arad': [('Zerind', 75), ('Sibiu', 140), ('Timisoara', 118)],
    'Timisoara': [('Arad', 118), ('Lugoj', 111)],
    'Lugoj': [('Timisoara', 111), ('Mehadia', 70)],
    'Mehadia': [('Lugoj', 70), ('Drobeta', 75)],
    'Drobeta': [('Mehadia', 75), ('Craiova', 120)],
    'Craiova': [('Drobeta', 120), ('Rimnicu Vilcea', 146), ('Pitesti', 138)],
    'Sibiu': [('Oradea', 151), ('Arad', 140), ('Fagaras', 99), ('Rimnicu Vilcea', 80)],
    'Rimnicu Vilcea': [('Sibiu', 80), ('Craiova', 146), ('Pitesti', 97)],
    'Fagaras': [('Sibiu', 99), ('Bucharest', 211)],
    'Pitesti': [('Rimnicu Vilcea', 97), ('Craiova', 138), ('Bucharest', 101)],
    'Bucharest': [('Fagaras', 211), ('Pitesti', 101), ('Giurgiu', 90)],
    'Giurgiu': [('Bucharest', 90)],
    # Otras ciudades...
}

def busqueda_uniforme(origen, destino, grafo):
    # Cola de prioridad
    cola = [(0, origen, [])]  # (costo acumulado, ciudad actual, camino recorrido)
    visitados = set()  # Para marcar ciudades ya visitadas

    while cola:
        # Obtener la ciudad con el menor costo acumulado
        costo, ciudad_actual, camino = heapq.heappop(cola)

        # Si ya visitamos esta ciudad, la saltamos
        if ciudad_actual in visitados:
            continue

        # Añadir la ciudad actual al camino recorrido
        camino = camino + [ciudad_actual]

        # Mostrar el progreso paso a paso
        print(f"Visitando {ciudad_actual} con costo acumulado {costo}")

        # Marcar la ciudad como visitada
        visitados.add(ciudad_actual)

        # Si llegamos al destino, terminar
        if ciudad_actual == destino:
            print(f"Camino óptimo encontrado: {' -> '.join(camino)} con un costo total de {costo} km")
            return camino, costo

        # Expandir la ciudad actual a sus vecinas
        for vecino, distancia in grafo.get(ciudad_actual, []):
            if vecino not in visitados:
                # Agregar la ciudad vecina a la cola con su costo actualizado
                heapq.heappush(cola, (costo + distancia, vecino, camino))

    # Si no se encuentra un camino, regresar None
    print("No se encontró una trayectoria.")
    return None

# Ejemplo de uso
origen = 'Arad'
destino = 'Bucharest'
camino_optimo, costo_total = busqueda_uniforme(origen, destino, mapa_rumania)
