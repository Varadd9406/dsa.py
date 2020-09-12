from collections import deque


class Graph:
	def __init__(self, No_of_nodes):
		self.n = No_of_nodes
		self.adj = [[] for i in range(self.n)]
		self.lift = [[None for i in range(4)] for i in range(self.n)]
		self.depth = [None] * self.n

	def addEdge(self, a, b):
		self.adj[a].append(b)
		self.adj[b].append(a)

	def binary_lifting(self, root):
		q = deque([[root, None]])
		while len(q):
			elem = q.popleft()
			for i in self.adj[elem[0]]:
				if i == elem[1]:
					continue
				q.append([i, elem[0]])
				self.lift[i][0] = elem[0]
		for exp in range(1, 4):
			for node in range(self.n):
				if self.lift[node][exp - 1] is not None:
					self.lift[node][exp] = self.lift[self.lift[node][exp - 1]][exp - 1]
		print(self.lift)

	def queryForLifting(self, node, up):
		i = 0
		while up >= 1:
			if up % 2 == 1:
				node = self.lift[node][i]
			up //= 2
			i += 1
		return node

	def BFSForDepth(self, root):
		q = deque([[root, None]])
		self.depth[root] = 0
		while len(q):
			elem = q.popleft()
			for i in self.adj[elem[0]]:
				if i == elem[1]:
					continue
				q.append([i, elem[0]])
				self.depth[i] = self.depth[elem[0]] + 1

	def LCA(self, node1, node2):  # call BFSForDepth and binaryLifting first
		if self.depth[node1] > self.depth[node2]:
			node1 = self.queryForLifting(node1, self.depth[node1] - self.depth[node2])
		elif self.depth[node2] > self.depth[node1]:
			node2 = self.queryForLifting(node2, self.depth[node2] - self.depth[node1])
		else:
			return node1
		low = 0
		high = self.depth[node1]
		ans = -1
		while low <= high:
			mid = (low + high) // 2
			if self.queryForLifting(node1, mid) == self.queryForLifting(node2, mid):
				high = mid - 1
				ans = self.queryForLifting(node1, mid)
			else:
				low = mid + 1
		return ans


g = Graph(9)
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(2, 3)
g.addEdge(2, 4)
g.addEdge(3, 5)
g.addEdge(3, 6)
g.addEdge(3, 7)
g.addEdge(7, 8)
g.binary_lifting(0)
g.BFSForDepth(0)
for i in range(8):
	print(i+1,9,'->',g.LCA(i,8)+1)