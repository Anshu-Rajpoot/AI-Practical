from queue import PriorityQueue

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[] for _ in range(vertices)]

    def add_edge(self, u, v, w):
        self.graph[u].append((v, w))
        self.graph[v].append((u, w))

    def prim_mst(self):
        visited = [False] * self.V
        min_heap = PriorityQueue()
        min_heap.put((0, 0))
        cost = 0
        while not min_heap.empty():
            w, u = min_heap.get()
            if visited[u]:
                continue
            visited[u] = True
            cost += w
            for v, weight in self.graph[u]:
                if not visited[v]:
                    min_heap.put((weight, v))
        return cost

# Example usage
g = Graph(4)
g.add_edge(0, 1, 1)
g.add_edge(0, 2, 2)
g.add_edge(1, 2, 3)
g.add_edge(1, 3, 4)
mst_cost = g.prim_mst()
print("Minimum Spanning Tree Cost:", mst_cost)
