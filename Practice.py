from collections import deque


class TreeNode:
    def __init__(self, node_data):
        self.data = node_data
        self.right = None
        self.left = None
        self.p = None


def swap(x, key, y):
    if x is None or x.data == key:
        return x
    else:
        if key < x.data:
            return swap(x.left, key)
        else:
            return search(x.right, key)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def bstInsert(self, data):
        if self.root:
            node = self.root
            n = TreeNode(data)
            while node:
                if data >= node.data:
                    if node.right is not None:
                        node = node.right
                    else:
                        break
                else:
                    if node.left is not None:
                        node = node.left
                    else:
                        break
            if data >= node.data:
                node.right = n
            else:
                node.left = n
        else:
            node = TreeNode(data)
            self.root = node


def recoverBST(x):
    f = True
    l = -10000000000
    u = 10000000000
    e1 = None
    e2 = None
    if x is not None:
        q = deque()
        q.append([x, l, u])
        while len(q) != 0:
            a = q.popleft()
            t = a[0]
            if t.left is not None:
                if not t.data > t.left.data or not (a[1] < t.left.data < a[2]):
                    if e1 is None:
                        e1 = t
                    else:
                        e2 = t
                        break
                q.append([t.left, a[1], t.data])
            if t.right is not None:
                if not t.data < t.right.data or not (a[1] < t.right.data < a[2]):
                    if e1 is None:
                        e1 = t
                    else:
                        e2 = t
                        break
                q.append([t.right, t.data, a[2]])



t = BinarySearchTree()
n = int(input())
arr = list(map(int, input().split()))
