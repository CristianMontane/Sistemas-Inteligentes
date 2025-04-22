from collections import deque

def bfs_search(initial_state, goal_state, graph):
    # Cola para el fringe (frontera de búsqueda)
    fringe = deque([(initial_state, [], 0)])  # (estado, camino, costo_acumulado)
    reached = set([initial_state])
    iteration = 0
    
    while fringe:
        iteration += 1
        print(f"Iteración {iteration}")
        print(f"Fringe actual: {[node[0] for node in fringe]}")
        
        # Extraer el nodo de la cola 
        current_state, path, cost = fringe.popleft()
        print(f"Explorando estado: {current_state}")
        
        # Verificar si hemos llegado al objetivo
        if current_state == goal_state:
            return path + [current_state], cost
        
        # Obtener todas las acciones posibles desde el estado actual
        actions = graph[current_state]
        
        # Ordenamos las acciones para que se encole de la mas péqueña a la mas grande
        sorted_actions = sorted(actions, key=lambda x: x[0])
        
        # Se desempaquyeta la tupla y se separa la letra del costo 
        for next_state, action_cost in sorted_actions:
            # Verificar si el estado ya ha sido alcanzado (prevención de ciclos)
            if next_state not in reached:
                # Añadir el nuevo estado directamente a la cola
                fringe.append((next_state, path + [current_state], cost + action_cost))
                # Marcar el estado como alcanzado
                reached.add(next_state)
                print(f"  Añadido a fringe: {next_state}")
            else:
                print(f"  {next_state} ya explorado, ignorado")
      
    # Si la cola se vacía sin encontrar una solución
    return 0

# Definir el grafo del problema
graph = {
    'A': [('B', 4), ('E', 2), ('H', 3)],
    'B': [('C', 4), ('D', 2), ('E', 1), ('G', 4), ('I', 5)],
    'C': [('E', 1), ('F', 3), ('G', 3), ('I', 2)],
    'D': [('A', 3), ('C', 2), ('E', 5), ('F', 4), ('H', 5)],
    'E': [('D', 5)],
    'F': [('B', 4), ('H', 5)],
    'G': [('H', 1)],
    'H': [('F', 4), ('G', 2)],
    'I': [('C', 5), ('G', 1), ('H', 4), ('J', 1)],
    'J': []
}

# Ejecutar la búsqueda
initial_state = 'A'
goal_state = 'J'
path, total_cost = bfs_search(initial_state, goal_state, graph)

# Mostrar resultado
if path:
    print("\nCamino encontrado:", ' -> '.join(path))
    print("Costo total:", total_cost)
else:
    print("\nNo se encontró una solución")