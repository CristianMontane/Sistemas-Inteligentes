def dfs_search(initial_state, goal_state, graph):
    # Pila para el fringe: (estado, camino, costo_acumulado)
    fringe = [(initial_state, [], 0)]
    reached = set()       # ¡No marcamos aún el inicial!
    iteration = 0

    while fringe:
        iteration += 1
        print(f"Iteración {iteration}")
        print(f"Fringe actual: {[n[0] for n in fringe]}")

        # Extraemos LIFO
        current_state, path, cost = fringe.pop()
        print(f"Explorando estado: {current_state}")

        # Ahora marcamos al desapilar
        if current_state not in reached:
            reached.add(current_state)
        else:
            # Si ya lo habíamos marcado, lo saltamos
            print(f"  {current_state} ya fue explorado, ignorado")
            continue

        # Verificamos meta
        if current_state == goal_state:
            print("\n¡Objetivo alcanzado!")
            print("Camino:", ' -> '.join(path + [current_state]))
            print("Costo total:", cost)
            return path + [current_state], cost

        # Expandimos sucesores en orden inverso
        actions = graph[current_state]
        sorted_actions = sorted(actions, key=lambda x: x[0], reverse=True)

        for next_state, action_cost in sorted_actions:
            if next_state not in reached:
                fringe.append((next_state,
                               path + [current_state],
                               cost + action_cost))
                print(f"  Añadido a fringe: {next_state}")
            else:
                print(f"  {next_state} ya fue explorado, ignorado")

    print("\nNo se encontró una solución")
    return None, None

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
path, total_cost = dfs_search(initial_state, goal_state, graph)

# Mostrar resultado
if path:
    print("\nCamino encontrado:", ' -> '.join(path))
    print("Costo total:", total_cost)
else:
    print("\nNo se encontró una solución")