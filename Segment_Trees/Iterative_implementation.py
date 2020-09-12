from sys import stdin, stdout


def build(segtree):
	for i in range(n - 1, 0, -1):
		segtree[i] = segtree[i <<1] + segtree[i << 1 | 1]


def modify(segtree, p, val):
	p += n
	segtree[p] = val
	while p > 1:
		segtree[p >> 1] = segtree[p] + segtree[p ^ 1]
		p >>= 1


def query(segtree, l, r):  # [l,r)
	res = 0
	l += n
	r += n
	while l < r:
		if l & 1:
			res += segtree[l]
			l += 1
		if r & 1:
			r -= 1
			res += segtree[r]
		l>>=1
		r>>=1
	return res


fullans = ''
n, q = map(int, stdin.readline().split())
ls = list(map(int, stdin.readline().split()))
T = [0] * (2 * n+1)
for i in range(n):
	T[n + i] = ls[i]
build(T)
for qs in range(q):
	typ, l, r = map(int, stdin.readline().split())
	if typ == 1:
		modify(T, l - 1, r)
	else:
		fullans += f"{query(T, l - 1, r)}\n"
stdout.write(fullans)
