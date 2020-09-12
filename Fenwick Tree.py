def getNext(num):
    return num + (num & (-num))


def getParent(num):
    return num - (num & (-num))


def getSum(ftree, index):
    s = 0
    i = index + 1
    while i > 0:
        s += ftree[i]
        i = getParent(i)
    return s


ls = list(map(int, input().split()))
n = len(ls)
fenwickTree = [0] * (n + 1)
for i in range(1, n + 1):
    j = i
    while j <= n:
        fenwickTree[j] += ls[i - 1]
        j = getNext(j)
print(getSum(fenwickTree, 2))
