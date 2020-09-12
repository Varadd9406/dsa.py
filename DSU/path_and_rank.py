def make_set(v):
	parent[v] = v
	depth[v] = 1


def find_set(v):
	if v == parent[v]:
		return v
	else:
		parent[v] = find_set(parent[v])
		return parent[v]


def union_set(a, b):
	a = find_set(a)
	b = find_set(b)
	if a != b:
		if depth[a] < depth[b]:
			a, b = b, a
		parent[b] = a
		depth[a] += depth[b]


n = int(input())

parent = [None] * n
depth = [1] * n
