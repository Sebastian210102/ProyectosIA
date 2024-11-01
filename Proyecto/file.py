import heapq

# Mapa de Rumania representado como un grafo
mapa_rumania = {
    'Oradea': [('Zerind', 71), ('Sibiu', 151)],
    'Zerind': [('Oradea', 71), ('Arad', 75)],
    'Arad': [('Zerind', 75), ('Sibiu', 140), ('Timisoara', 118)],
    'Timisoara': [('Arad', 118), ('Lugoj', 111)],
    'Lugoj': [('Timisoara', 111), ('Mehadia', 70)],
    'Mehadia': [('Lugoj', 70), ('Dobreta', 75)],
    'Dobreta': [('Mehadia', 75), ('Craiova', 120)],
    'Craiova': [('Dobreta', 120), ('Rimnicu Vilcea', 146), ('Pitesti', 138)],
    'Sibiu': [('Oradea', 151), ('Arad', 140), ('Fagaras', 99), ('Rimnicu Vilcea', 80)],
    'Rimnicu Vilcea': [('Sibiu', 80), ('Craiova', 146), ('Pitesti', 97)],
    'Fagaras': [('Sibiu', 99), ('Bucharest', 211)],
    'Pitesti': [('Rimnicu Vilcea', 97), ('Craiova', 138), ('Bucharest', 101)],
    'Bucharest': [('Fagaras', 211), ('Pitesti', 101), ('Giurgiu', 90), ('Urziceni',85)],
    'Giurgiu': [('Bucharest', 90)],
    'Urziceni': [('Hirsova', 98), ('Vaslui', 142)],
    'Hirsova' : [('Urziceni', 98), ('Eforie', 86)],
    'Eforie' : [('Hirsova', 86)],
    'Vaslui' : [('Urziceni', 142), ('Iasi', 92)],
    'Iasi' : [('Vaslui', 92), ('Neamt', 87)],
}

def busqueda_uniforme(origen, destino, grafo):
    # Cola de prioridad
    cola = [(0, origen, [])]  # (costo acumulado, ciudad actual, camino recorrido)
    visitados = set()  # Para marcar ciudades ya visitadas
    rutas_fallidas = set()  # Almacena ciudades de las que no se puede avanzar sin retroceder

    while cola:
        # Obtener la ciudad con el menor costo acumulado
        costo, ciudad_actual, camino = heapq.heappop(cola)

        # Si ya visitamos esta ciudad o es una ruta fallida, la saltamos
        if ciudad_actual in visitados or ciudad_actual in rutas_fallidas:
            continue

        # Añadir la ciudad actual al camino recorrido
        camino = camino + [ciudad_actual]

        # Mostrar el progreso paso a paso
        print(f"Visitando {' - '.join(camino)} con costo acumulado {costo}")

        # Marcar la ciudad como visitada
        visitados.add(ciudad_actual)

        # Si llegamos al destino, terminar
        if ciudad_actual == destino:
            print(f"Camino óptimo encontrado: {' -> '.join(camino)} con un costo total de {costo} km")
            return camino, costo

        # Obtener ciudades vecinas no visitadas
        vecinos_no_visitados = [vecino for vecino, _ in grafo.get(ciudad_actual, []) if vecino not in visitados]

        # Si no hay vecinos no visitados, marca como ruta fallida y continúa
        if not vecinos_no_visitados:
            print(f"No hay más opciones desde {ciudad_actual}, retrocediendo.")
            rutas_fallidas.add(ciudad_actual)
            continue

        # Expandir la ciudad actual a sus vecinos no visitados
        for vecino, distancia in grafo.get(ciudad_actual, []):
            if vecino not in visitados and vecino not in rutas_fallidas:
                # Agregar la ciudad vecina a la cola con su costo actualizado
                heapq.heappush(cola, (costo + distancia, vecino, camino))

    # Si no se encuentra un camino, regresar None
    print("No se encontró una trayectoria.")
    return None




origen = input("Elige tu ciudad origen: ")
destino = input("Elige tu ciudad destino: ")
camino_optimo, costo_total = busqueda_uniforme(origen, destino, mapa_rumania)
