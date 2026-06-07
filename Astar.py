import heapq

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

heuristic = {
    'A': 13,
    'B': 12,
    'C': 11,
    'D': 9,
    'E': 6,
    'F': 5,
    'G': 1,
    'H': 0,
    'J': 13,
    'K': 12,
    'L': 7
}

best_path = []
best_cost = float('inf')
visited_nodes = 0


def astar(start, goal):
    global best_path, best_cost, visited_nodes

    # (f = g + h, g, node, path)
    queue = [(heuristic[start], 0, start, [start])]

    while queue:
        f, g, node, path = heapq.heappop(queue)
        visited_nodes += 1

        if node == goal:
            best_cost = g
            best_path = path
            return

        for neighbor, weight in graph[node]:
            if neighbor not in path:
                new_g = g + weight
                new_f = new_g + heuristic[neighbor]
                heapq.heappush(queue, (new_f, new_g, neighbor, path + [neighbor]))


start_node = 'A'
goal_node = 'H'

astar(start_node, goal_node)

print("\n===== A* RESULT =====\n")

print("Path :")
print(" -> ".join(best_path))

print("\nDetail Path :")
for node in best_path:
    print(f"  {node} = {node_description[node]}")

print("\nTotal Cost :", best_cost)
print("Visited Nodes :", visited_nodes)