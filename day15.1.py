from collections import defaultdict, Counter, deque

with open("day15.input.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]

risks = {}
len_y = len(lines)
len_x = len(lines[0])

for y in range(len_y):
    for x in range(len_x):
        risks[(x, y)] = int(lines[y][x])


def get_neighbors(coord):
    x, y = coord
    neighbors = []
    if x > 0:
        neighbors.append((x - 1, y))
    if x < len_x - 1:
        neighbors.append((x + 1, y))
    if y > 0:
        neighbors.append((x, y - 1))
    if y < len_y - 1:
        neighbors.append((x, y + 1))

    return neighbors


#  1  function Dijkstra(Graph, source):
def find_shortest_path(graph, start):
    unvisited_nodes = {}
    distances = {}
    previous = {}

    for coord in graph:
        distances[coord] = 99999999999
        previous[coord] = None
        unvisited_nodes[coord] = 1

    distances[start] = 0

    while unvisited_nodes:
        u = min(unvisited_nodes, key=distances.get)
        del unvisited_nodes[u]

        for neighbor in [n for n in get_neighbors(u) if n in unvisited_nodes]:
            alt = distances[u] + graph[neighbor]
            if alt < distances[neighbor]:
                distances[neighbor] = alt
                previous[neighbor] = u

    return distances, previous


print(find_shortest_path(risks, (0, 0))[0])
