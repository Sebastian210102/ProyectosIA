import numpy as np
import matplotlib.pyplot as plt

# Datos iniciales
puntos = np.array([
    [-3, -3], [-3, -2], [-3, -1], [-3, 1], [-2, -1], 
    [-2, 1], [-2, 4], [-1, -2], [1, -1], [1, 1], 
    [1, 2], [2, -2], [2, 2], [2, 3]
])

# Centroides iniciales
centroides = [np.array([-1, 2]), np.array([4, 0])]

# Función para calcular la distancia euclidiana
def calcular_distancia(punto, centroide):
    return np.sqrt(np.sum((punto - centroide) ** 2))

# Función para asignar cada punto a su cluster más cercano
def asignar_puntos(puntos, centroides):
    clusters = [[] for _ in centroides]
    resultados = []
    for punto in puntos:
        distancias = [calcular_distancia(punto, centroide) for centroide in centroides]
        cluster = np.argmin(distancias)
        clusters[cluster].append(punto)
        resultados.append(cluster)
    return clusters, resultados

# Función para recalcular los centroides
def recalcular_centroides(clusters):
    nuevos_centroides = []
    for cluster in clusters:
        if len(cluster) > 0:
            nuevos_centroides.append(np.mean(cluster, axis=0))
        else:
            nuevos_centroides.append(np.zeros(len(clusters[0][0])))  # Centroides vacíos a 0
    return nuevos_centroides

# Función para verificar si los centroides han cambiado
def checar_centroides_diferentes(centroides, nuevos_centroides):
    for c1, c2 in zip(centroides, nuevos_centroides):
        if not np.allclose(c1, c2):  # Si no son iguales
            return True
    return False

# Función principal
def kmedias(puntos, centroides_iniciales, max_iter=50):
    centroides = centroides_iniciales
    iteraciones = []
    
    for iteracion in range(max_iter):
        print(f"\nIteración {iteracion + 1}:")

        # Asignar puntos a clusters
        clusters, asignaciones = asignar_puntos(puntos, centroides)
        print(f"Asignaciones: {asignaciones}")

        # Recalcular centroides
        nuevos_centroides = recalcular_centroides(clusters)
        print(f"Centroides actuales: {centroides}")
        print(f"Nuevos centroides: {nuevos_centroides}")

        # Guardar información de la iteración
        iteraciones.append({
            "iteracion": iteracion + 1,
            "clusters": clusters,
            "centroides": centroides
        })

        # Verificar si los centroides no cambian
        if not checar_centroides_diferentes(centroides, nuevos_centroides):
            print("\n¡Convergencia alcanzada!")
            break

        # Actualizar centroides
        centroides = nuevos_centroides
    
    return iteraciones, centroides, asignaciones

# Llamada al algoritmo
iteraciones, centroides_finales, asignaciones_finales = kmedias(puntos, centroides)

# Mostrar primeras 3 iteraciones
print("\n=== PRIMERAS 3 ITERACIONES ===")
for i in range(min(3, len(iteraciones))):
    print(f"Iteración {i + 1}:")
    print(f"Clusters: {iteraciones[i]['clusters']}")
    print(f"Centroides: {iteraciones[i]['centroides']}")

# Mostrar resultados finales
print("\n=== RESULTADO FINAL ===")
print(f"Centroides finales: {centroides_finales}")
print(f"Asignaciones finales: {asignaciones_finales}")

# Graficar puntos y centroides
def graficar_puntos(puntos, asignaciones, centroides, titulo):
    colores = ['r', 'g', 'b']
    for i, punto in enumerate(puntos):
        plt.scatter(punto[0], punto[1], c=colores[asignaciones[i]], s=50)
    for i, centroide in enumerate(centroides):
        plt.scatter(centroide[0], centroide[1], c=colores[i], marker='x', s=200)
    plt.title(titulo)
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.grid()
    plt.show()

# Graficar los datos iniciales
graficar_puntos(puntos, [0]*len(puntos), centroides, "Datos iniciales con centroides")

# Graficar resultado final
graficar_puntos(puntos, asignaciones_finales, centroides_finales, "Resultado final")

