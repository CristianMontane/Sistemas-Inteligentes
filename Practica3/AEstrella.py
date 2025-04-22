def a_star_search(initial_state, goal_state, graph, heuristics):
    # Fringe (frontera de búsqueda) como lista para ordenarla como cola de prioridad
    fringe = [(initial_state, [], 0, heuristics[initial_state])]  # (estado, camino, costo_g, f=g+h)
    
    # Diccionario para almacenar el costo óptimo conocido hasta cada estado
    cost_so_far = {initial_state: 0}
    
    # Contador de iteraciones para mostrar el estado del fringe
    iteration = 0
    
    while fringe:
        iteration += 1
        print(f"\nIteración {iteration}")
        # Ordenar el fringe por f(n) = g(n) + h(n) y, en caso de empate, por etiqueta
        fringe.sort(key=lambda x: (x[3], x[0]))
        print(f"Fringe actual: {[(node[0], node[2], node[3]) for node in fringe]}")  # (estado, g, f)
        
        
        # Extraer el nodo con menor f(n) (y en caso de empate, con menor etiqueta)
        current_state, path, cost_g, cost_f = fringe.pop(0)
        
        print(f"Explorando estado: {current_state} con g={cost_g}, f={cost_f}")
        
        # Verificar si hemos llegado al objetivo
        if current_state == goal_state:
            return path + [current_state], cost_g
        
        # Obtener todas las acciones posibles desde el estado actual
        actions = graph[current_state]
        
        for next_state, action_cost in actions:
            # Calcular el nuevo costo g hasta este estado
            new_cost_g = cost_g + action_cost
            
            # Si es un nuevo estado o hemos encontrado un camino de menor costo
            if next_state not in cost_so_far or new_cost_g < cost_so_far[next_state]:
                # Actualizar el costo conocido hasta este estado
                cost_so_far[next_state] = new_cost_g
                
                # Calcular f(n) = g(n) + h(n)
                cost_f = new_cost_g + heuristics[next_state]
                
                # Añadir al fringe
                fringe.append((next_state, path + [current_state], new_cost_g, cost_f))
                print(f"  Añadido/Actualizado en fringe: {next_state} con g={new_cost_g}, f={cost_f}")
            else:
                print(f"  {next_state} ya tiene un camino de menor costo (g={cost_so_far[next_state]})")
    
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

# Valores heurísticos
heuristics = {
    'A': 8, 'B': 3, 'C': 2, 'D': 4, 'E': 10, 
    'F': 10, 'G': 13, 'H': 12, 'I': 0, 'J': 0
}

# Ejecutar la búsqueda
initial_state = 'A'
goal_state = 'J'
path, total_cost = a_star_search(initial_state, goal_state, graph, heuristics)

# Mostrar resultado
if path:
    print("\nCamino encontrado:", ' -> '.join(path))
    print("Costo total:", total_cost)
else:
    print("\nNo se encontró una solución")