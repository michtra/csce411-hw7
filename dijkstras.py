# Dijkstra's according to CLRS with path reconstruction
import heapq  # min heap module


def dijkstra(graph, start):
    # initialize distances to infinity
    distances = {}
    for vertex in graph:
        distances[vertex] = float('infinity')
    distances[start] = 0

    # parent dictionary
    parent = {}
    for vertex in graph:
        parent[vertex] = None

    # S = set of fully visited vertices
    S = set()

    # Q = priority queue of vertices
    Q = []
    for vertex in graph:
        # (distance, vertex) pairs in the heap
        heapq.heappush(Q, (distances[vertex], vertex))

    # while not empty, poll the priority queue
    while Q:
        # EXTRACT-MIN
        min_distance, u = heapq.heappop(Q)

        # skip if already fully visited
        if u in S:
            continue

        S.add(u)

        # neighbors of u
        for v, weight in graph[u]:
            # skip if fully visited
            if v in S:
                continue

            # calculate possible shorter distance
            distance = distances[u] + weight

            # RELAX if a shorter path is found
            if distance < distances[v]:
                distances[v] = distance
                parent[v] = u
                # Add updated vertex with new priority
                heapq.heappush(Q, (distance, v))

    # now we construct the paths
    # we know that there is guaranteed a path from 1 to each exit node
    # thus we don't have to worry about that case
    paths = {}
    for vertex in graph:
        # path to start is just itself
        if vertex == start:
            paths[vertex] = [start]
            continue

        # create an empty path for the current vertex
        path = []
        current = vertex

        # builds each path in reverse by traversing through parent
        while current != start:
            path.append(current)
            current = parent[current]

        # add start vertex to complete the path (printing purposes)
        path.append(start)
        # reverse to get the correct order
        path.reverse()
        paths[vertex] = path
    return distances, paths


# Builds undirected graph
# tuples: (u, v, weight)
def build_graph(edges):
    graph = {}

    for u, v, weight in edges:
        # if they don't have edges yet
        if u not in graph:
            graph[u] = []
        if v not in graph:
            graph[v] = []

        # add edges
        graph[u].append((v, weight))
        graph[v].append((u, weight))

    return graph


def solve():
    edges = [
        ("1", "2", 1),
        ("1", "11", 1),
        ("2", "3", 1),
        ("2", "21", 1),
        ("3", "8", 2),
        ("3", "4", 1),
        ("4", "5", 1),
        ("5", "7", 1),
        ("5", "6", 2),
        ("5", "22", 1),
        ("6", "7", 1),
        ("7", "8", 1),
        ("8", "9", 1),
        ("9", "10", 1),
        ("9", "19", 1),
        ("10", "11", 1),
        ("10", "18", 2),
        ("11", "12", 2),
        ("11", "17", 1),
        ("12", "13", 2),
        ("13", "14", 2),
        ("13", "21", 1),
        ("14", "15", 1),
        ("14", "16", 1),
        ("14", "20", 1),
        ("16", "17", 2),
        ("17", "18", 2),
        ("18", "19", 2),
        ("20", "21", 2),
        ("20", "22", 1),
        ("21", "22", 2)
    ]

    graph = build_graph(edges)
    start = '1'  # start from vertex 1

    distances, paths = dijkstra(graph, start)

    # find distances to specific vertices
    target_vertices = ['6', '8', '9', '15', '16', '22']

    print(f"Distances from {start}:")
    minimum_distance = float('inf')
    exit_vertex = None
    for vertex in target_vertices:
        path = paths[vertex]
        print(f"{vertex}: {distances[vertex]} (Path: {', '.join(path)})")
        if distances[vertex] < minimum_distance:
            minimum_distance = distances[vertex]
            exit_vertex = vertex
    print()
    print(f"Exit vertex: {exit_vertex}")
    print(f"Path: {', '.join(paths[exit_vertex])}")


if __name__ == "__main__":
    solve()
