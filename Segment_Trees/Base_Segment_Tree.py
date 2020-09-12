from math import log, ceil
from sys import maxsize


def fast_exp_pow(num, pw):
	if pw == 1:
		return num
	evener = 1
	if pw % 2 == 1:
		evener = num
	return evener * fast_exp_pow(num, pw // 2) ** 2


def nearestPowOf2(num):
	x = log(num, 2)
	if int(x) == x:
		return num
	else:
		return fast_exp_pow(2, ceil(x))


def constructSegmentTree(arr, segTree, low, high, pos):
	if low == high:
		segTree[pos] = arr[low]
	else:
		mid = (low + high) // 2
		constructSegmentTree(arr, segTree, low, mid, 2 * pos + 1)
		constructSegmentTree(arr, segTree, mid + 1, high, 2 * pos + 2)
		segTree[pos] = max(segTree[2 * pos + 1], segTree[2 * pos + 2])


def rangeMaxQuery(segTree, qlow, qhigh, low, high, pos):
	if qlow <= low and qhigh >= high:
		return segTree[pos]
	elif qlow > high or qhigh < low:
		return -maxsize
	mid = (low + high) // 2
	return max(rangeMaxQuery(segTree, qlow, qhigh, low, mid, 2 * pos + 1),
	           rangeMaxQuery(segTree, qlow, qhigh, mid + 1, high, 2 * pos + 2))


def update_segtree(segtree, index, newval, low, high, pos):
	if low == high:
		segtree[pos] = newval
	else:
		mid = (low + high) // 2
		if index <= mid:
			update_segtree(segtree, index, newval, low, mid, pos * 2 + 1)
		else:
			update_segtree(segtree, index, newval, mid + 1, high, pos * 2 + 2)
		segtree[pos] = max(segtree[2 * pos + 1], segtree[2 * pos + 2])


n = int(input())
ls = list(map(int, input().split()))
segmentTree = [-maxsize] * (2 * nearestPowOf2(n) - 1)
constructSegmentTree(ls, segmentTree, 0, n - 1, 0)
for qs in range(int(input())):
	l, r = map(int, input().split())
	print(rangeMaxQuery(segmentTree, l - 1, r - 1, 0, n - 1, 0)[0])
