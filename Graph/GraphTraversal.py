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


if __name__ == '__main__':
    g = Graph(4)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    g.add_edge(2, 3)
    g.add_edge(3, 3)
    print(g)
    g.dfs(0)
    g.bfs(2)
