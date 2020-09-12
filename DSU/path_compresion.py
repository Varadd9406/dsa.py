def make_set(v):
	parent[v] = v


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
		parent[b] = a


n = int(input())

parent = [None] * n
