from collections import deque
from sys import maxsize
from copy import deepcopy


class Graph:
    def __init__(self, No_of_nodes):
        self.n = No_of_nodes
        self.adj = [[] for i in range(self.n)]

    def addEdge(self, a, b, w):
        self.adj[a].append([b, w])

    def BFS(self, start):
        visited = [False] * self.n
        que = deque()
        que.append(start)
        visited[start] = True
        ans = ''
        while que:
            s = que.popleft()
            ans += str(s) + ' '
            for i in self.adj[s]:
                if not visited[i[0]]:
                    que.append(i[0])
                    visited[i[0]] = True
        return ans

    def DFS(self, start):
        ans = ''
        visited = [False] * self.n
        stack = [start]
        while len(stack):
            s = stack.pop()
            if not visited[s]:
                ans += str(s) + ' '
                visited[s] = True
            for node in self.adj[s]:
                if not visited[node[0]]:
                    stack.append(node[0])
        return ans

    def bellmanFord(self, start):
        distance = [maxsize for i in range(self.n)]
        distance[start] = 0
        for i in range(self.n - 1):
            for j in range(self.n):
                a = j
                for k in self.adj[j]:
                    b, w = k
                    distance[b] = min(distance[b], distance[a] + w)
        return distance

    def dijkstra(self, start):
        distance = [maxsize for i in range(self.n)]
        distance[start] = 0
        q = deque()
        q.append(start)
        while len(q) != 0:
            a = q.pop()
            for u in self.adj[a]:
                b, w = u
                if distance[a] + w < distance[b]:
                    distance[b] = distance[a] + w
                    q.append(b)
        return distance

    def topological_sort_util(self, node, stack, visited):
        visited[node] = True
        for i in self.adj[node]:
            if not visited[i[0]]:
                self.topological_sort_util(i[0], stack, visited)
        stack.append(node)

    def topological_sort(self):
        stack = []
        visited = [False] * self.n
        for i in range(self.n):
            if not visited[i]:
                self.topological_sort_util(i, stack, visited)
        return stack[::-1]


def matrixToGraph(ls) -> Graph:
    n = len(ls[0])
    m = len(ls)
    g = Graph(n * m)

    for row in range(m):
        for col in range(n):
            if ls[row][col] == 1:
                continue
            if row < m - 1:
                if ls[row + 1][col] == 0:
                    g.addEdge(col + row * n, col + (row + 1) * n, 1)
                    g.addEdge(col + (row + 1) * n, col + row * n, 1)
            if col < n - 1:
                if ls[row][col + 1] == 0:
                    g.addEdge(col + row * n, col + 1 + (row * n), 1)
                    g.addEdge(col + 1 + (row * n), col + row * n, 1)
    return g


g = Graph(6)
g.addEdge(0, 1, 1)
g.addEdge(1, 2, 1)
g.addEdge(2, 5, 1)
g.addEdge(3, 0, 1)
g.addEdge(3, 4, 1)
g.addEdge(4, 2, 1)
g.addEdge(4, 1, 1)
print(g.topological_sort())
