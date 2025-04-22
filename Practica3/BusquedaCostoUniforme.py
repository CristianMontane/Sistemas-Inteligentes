def ucs_search(initial_state, goal_state, graph):
    # Cola para el fringe (frontera de búsqueda)
    fringe = [(initial_state, [], 0)]  # (estado, camino, costo_acumulado)
    # Diccionario para almacenar el costo óptimo conocido hasta cada estado
    cost_so_far = {initial_state: 0}
    iteration = 0
    
    while fringe:
        iteration += 1
        print(f"\nIteración {iteration}")
        
        # Ordenar el fringe por costo y, en caso de empate, por etiqueta
        fringe.sort(key=lambda x: (x[2], x[0]))

        print(f"Fringe actual: {[node for node in fringe]}")  # Muestra estado y costo
        
        
        # Extraer el nodo con menor costo (y en caso de empate, con menor etiqueta)
        current_state, path, cost = fringe.pop(0)
        
        print(f"Explorando estado: {current_state} con costo {cost}")
        
        # Verificar si hemos llegado al objetivo
        if current_state == goal_state:
            return path + [current_state], cost
        
        # Obtener todas las acciones posibles desde el estado actual
        actions = graph[current_state]
        
        for next_state, action_cost in actions:
            new_cost = cost + action_cost
            
            # Si es un nuevo estado o hemos encontrado un camino de menor costo
            if next_state not in cost_so_far or new_cost < cost_so_far[next_state]:
                cost_so_far[next_state] = new_cost
                fringe.append((next_state, path + [current_state], new_cost))
                print(f"  Añadido/Actualizado en fringe: {next_state} con costo {new_cost}")
            else:
                print(f"  {next_state} ya tiene un camino de menor costo ({cost_so_far[next_state]})")
    
    # Si la cola se vacía sin encontrar una solución
    return None, 0

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
path, total_cost = ucs_search(initial_state, goal_state, graph)

# Mostrar resultado
if path:
    print("\nCamino encontrado:", ' -> '.join(path))
    print("Costo total:", total_cost)
else:
    print("\nNo se encontró una solución")