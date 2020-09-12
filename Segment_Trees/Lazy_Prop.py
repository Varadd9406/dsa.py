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
		segTree[pos] = min(segTree[2 * pos + 1], segTree[2 * pos + 2])


def rangeMinQuery(segTree, lazy, qlow, qhigh, low, high, pos):
	if lazy[pos] != 0:
		segTree[pos] += lazy[pos]
		if low != high:
			lazy[2 * pos + 1] = lazy[pos]
			lazy[2 * pos + 2] = lazy[pos]
		lazy[pos] = 0
	if qlow <= low and qhigh >= high:
		return segTree[pos]
	elif qlow > high or qhigh < low:
		return maxsize
	mid = (low + high) // 2
	return min(rangeMinQuery(segTree, lazy, qlow, qhigh, low, mid, 2 * pos + 1),
	           rangeMinQuery(segTree, lazy, qlow, qhigh, mid + 1, high, 2 * pos + 2))


def update_seg_tre_lazy(segTree, lazy, qlow, qhigh, delta, low, high, pos):
	if lazy[pos] != 0:
		segTree[pos] += lazy[pos]
		if low != high:
			lazy[2 * pos + 1] = lazy[pos]
			lazy[2 * pos + 2] = lazy[pos]
		lazy[pos] = 0
	if qlow > high or qhigh < low:  # No overlap
		return
	if qlow <= low and qhigh <= high:  # Total Overlap
		segTree[pos] += delta
		if low != high:
			lazy[2 * pos + 1] += delta
			lazy[2 * pos + 2] += delta
		return
	mid = (low + high) // 2
	update_seg_tre_lazy(segTree, lazy, qlow, qhigh, delta, qlow, mid, pos * 2 + 1)
	update_seg_tre_lazy(segTree, lazy, qlow, qhigh, delta, mid + 1, qhigh, pos * 2 + 2)
	segTree[pos] = min(segTree[2 * pos + 1], segTree[2 * pos + 2])


n = int(input())
ls = list(map(int, input().split()))
segmentTree = [maxsize] * (2 * nearestPowOf2(n) - 1)
lazy = [0] * (2 * nearestPowOf2(n) - 1)

constructSegmentTree(ls, segmentTree, 0, n - 1, 0)
for qs in range(int(input())):
	l, r = map(int, input().split())
	print(rangeMinQuery(segmentTree, lazy, l - 1, r - 1, 0, n - 1, 0))
