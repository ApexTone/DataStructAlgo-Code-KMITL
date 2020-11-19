import sys


class Graph:
    def __init__(self, node=10):  # using adj matrix as representation
        self.graph = []
        if node <= 0:
            print("Negative number is not acceptable: Change to default value (10)")
            node = 10
        for i in range(node):
            self.graph.append([0]*node)

    def add_edge(self, start, end, weight=1, bidirectional=False):
        if (start < 0 or start >= len(self.graph)) or (end < 0 or end >= len(self.graph)):
            print("Index Out Of Bound")
            return
        self.graph[start][end] = weight
        if bidirectional:
            self.graph[end][start] = weight

    def __str__(self):
        out = ""
        for i in range(len(self.graph)):
            out += str(self.graph[i]) + "\n"
        return out

    def __dfs(self, vertex, visited):
        print(vertex, end=" ")
        visited.add(vertex)
        for i in range(len(self.graph[vertex])):
            if i not in visited and self.graph[vertex][i] > 0:
                self.__dfs(i, visited)

    def dfs(self, start=0):
        visited = set()
        # self.__dfs(start, visited)
        """
        stack = [start]
        visited.add(start)
        while len(stack) > 0:
            vertex = stack.pop()
            print(vertex, end=" ")
            for i in range(len(self.graph[vertex])):
                if i not in visited and self.graph[vertex][i] > 0:
                    stack.append(i)
                    visited.add(i)
        """
        print()

    def bfs(self, start=0):
        visited = set()
        queue = [start]
        visited.add(start)
        while len(queue) > 0:
            vertex = queue.pop(0)
            print(vertex, end=" ")
            for i in range(len(self.graph[vertex])):
                if i not in visited and self.graph[vertex][i] > 0:
                    queue.append(i)
                    visited.add(i)
        print()

    def min_distance(self, dist, visited):
        minimum = sys.maxsize  # max int
        min_index = 0
        for vertex in range(len(self.graph)):
            if dist[vertex] < minimum and vertex not in visited:
                minimum = dist[vertex]
                min_index = vertex
        return min_index

    def dijkstra(self, start=0):  # can't process negative edge
        dist = [sys.maxsize] * len(self.graph)
        dist[start] = 0
        visited = set()
        for vertex in range(len(self.graph)):
            u = self.min_distance(dist, visited)  # find node with shortest path
            visited.add(u)

            for v in range(len(self.graph)):
                # if there's a path to this vertex v and it's not visited yet and there's an even shorter path
                if self.graph[u][v] > 0 and v not in visited and dist[v] > dist[u] + self.graph[u][v]:
                    dist[v] = dist[u] + self.graph[u][v]

        print(f"Shortest path from {start}")
        for vertex in range(len(self.graph)):
            print(vertex, dist[vertex])
        print('-'*30)

    def floyd_warshall(self):
        dist = self.graph.copy()
        for i in range(len(dist)):
            for j in range(len(dist)):
                if dist[i][j] == 0:
                    dist[i][j] = sys.maxsize
        for i in range(len(dist)):
            dist[i][i] = 0

        for k in range(len(self.graph)):
            for i in range(len(self.graph)):
                for j in range(len(self.graph)):
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
        for row in range(len(dist)):
            print(dist[row])
        return dist


if __name__ == '__main__':
    g = Graph(9)
    g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
               [4, 0, 8, 0, 0, 0, 0, 11, 0],
               [0, 8, 0, 7, 0, 4, 0, 0, 2],
               [0, 0, 7, 0, 9, 14, 0, 0, 0],
               [0, 0, 0, 9, 0, 10, 0, 0, 0],
               [0, 0, 4, 14, 10, 0, 2, 0, 0],
               [0, 0, 0, 0, 0, 2, 0, 1, 6],
               [8, 11, 0, 0, 0, 0, 1, 0, 7],
               [0, 0, 2, 0, 0, 0, 6, 7, 0]
               ]
    g.dijkstra(0)

    g.graph = [[0, 0, -2, 0],
                [4, 0, 3, 0],
                [0, 0, 0, 2],
                [0, -1, 0, 0]]
    g.floyd_warshall()
