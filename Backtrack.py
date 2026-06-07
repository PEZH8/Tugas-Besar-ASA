graph = {
    'A': [('B', 1)],
    'B': [('C', 1), ('J', 1)],
    'C': [('D', 2)],
    'D': [('E', 3)],
    'E': [('F', 2)],
    'F': [('G', 4), ('K', 1)],
    'G': [('H', 1), ('L', 1)],
    'H': [],
    'J': [('B', 2)],
    'K': [('C', 3)],
    'L': [('F', 2)]
}

node_description = {
    'A': 'Isi Google Form',
    'B': 'Generate Surat',
    'C': 'Tanda Tangan Mahasiswa',
    'D': 'Dosen Pembimbing',
    'E': 'Koordinator PKL',
    'F': 'Ketua Departemen',
    'G': 'Dekanat',
    'H': 'Surat Izin Keluar',
    'J': 'Revisi Generate Surat',
    'K': 'Revisi Departemen',
    'L': 'Revisi Dekanat'
}

best_path = []
best_cost = float('inf')
visited_nodes = 0


def backtracking(node, goal, path, cost):
    global best_path, best_cost, visited_nodes

    visited_nodes += 1
    path.append(node)

    if node == goal:
        if cost < best_cost:
            best_cost = cost
            best_path = path.copy()
    else:
        for neighbor, weight in graph[node]:
            if neighbor not in path:
                backtracking(neighbor, goal, path, cost + weight)

    path.pop()  


start_node = 'A'
goal_node = 'H'

backtracking(start_node, goal_node, [], 0)

print("\n===== BACKTRACKING RESULT =====\n")

print("Path :")
print(" -> ".join(best_path))

print("\nDetail Path :")
for node in best_path:
    print(f"  {node} = {node_description[node]}")

print("\nTotal Cost :", best_cost)
print("Visited Nodes :", visited_nodes)