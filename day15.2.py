from collections import defaultdict, Counter, deque

with open("day15.input.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]

risks = {}
len_y = len(lines)
len_x = len(lines[0])

for y in range(len_y):
    for x in range(len_x):
        for i in range(5):
            for j in range(5):
                risk = int(lines[y][x]) + i + j
                if risk > 9:
                    risk %= 9

                risks[(i * len_x + x, j * len_y + y)] = risk
# for y in range(len_y):
#     for x in range(len_x):
#         risks[(x, y)] = int(lines[y][x])


def get_neighbors(coord):
    x, y = coord
    neighbors = []
    if x > 0:
        neighbors.append((x - 1, y))
    if x < len_x * 5 - 1:
        neighbors.append((x + 1, y))
    if y > 0:
        neighbors.append((x, y - 1))
    if y < len_y * 5 - 1:
        neighbors.append((x, y + 1))

    return neighbors


#  procedure Shortest-Path-Faster-Algorithm(G, s)
def find_shortest_path(graph, s):
    d = {}
    Q = deque()
    # for each vertex v ≠ s in V(G)
    for v in graph:
        if v == s:
            continue
        # d(v) := ∞
        d[v] = 999999999
    # d(s) := 0
    d[s] = 0
    # push s into Q
    Q.append(s)
    # while Q is not empty do
    while Q:
        # print(Q)
        # u := poll Q
        u = Q.popleft()
        # for each edge (u, v) in E(G) do
        for v in get_neighbors(u):
            # if d(u) + w(u, v) < d(v) then
            if d[u] + graph[v] < d[v]:
                # d(v) := d(u) + w(u, v)
                d[v] = d[u] + graph[v]
                #  if v is not in Q then
                if v not in Q:
                    #  push v into Q
                    Q.append(v)
    return d


print(find_shortest_path(risks, (0, 0)))
