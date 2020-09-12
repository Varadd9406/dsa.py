from collections import deque


class TreeNode:
    def __init__(self, node_data):
        self.data = node_data
        self.right = None
        self.left = None
        self.p = None


def inorder(x):
    if x is not None:
        inorder(x.left)
        print(x.data, end=" ")
        inorder(x.right)


def preorder(x):
    if x is not None:
        print(x.data, end=' ')
        preorder(x.left)
        preorder(x.right)


def postorder(x):
    if x is not None:
        postorder(x.left)
        postorder(x.right)
        print(x.data, end=' ')


def levelOrder(x):
    if x is not None:
        q = deque()
        q.append(x)
        while len(q) != 0:
            t = q.popleft()
            print(t.data, end=" ")
            if t.left is not None:
                q.append(t.left)
            if t.right is not None:
                q.append(t.right)


def topView(x):  ##NotComplete
    d = x.data
    t = x
    ar1 = []
    ar2 = []
    i = 0
    while x is not None:
        if i != 0:
            ar1.append(x.data)
        x = x.left
        i += 1
    i = 0
    while t is not None:
        if i != 0:
            ar2.append(t.data)
        t = t.right
        i += 1
    s = ''
    for i in ar1[::-1]:
        s += str(i) + ' '
    s += str(d) + ' '
    for i in ar2:
        s += str(i) + ' '
    print(s)


def checkBST(x):
    f = True
    l = -10000000000
    u = 10000000000
    if x is not None:
        q = deque()
        q.append([x, l, u])
        while len(q) != 0:
            a = q.popleft()
            t = a[0]
            if t.left is not None:
                if not t.data > t.left.data or not (a[1] < t.data < a[2]):
                    f = False
                    break
                q.append([t.left, a[1], t.data])
            if t.right is not None:
                if not t.data < t.right.data or not (a[1] < t.data < a[2]):
                    f = False
                    break
                q.append([t.right, t.data, a[2]])
    return f


def search(x, key):
    if x is None or x.data == key:
        return x
    else:
        if key < x.data:
            return search(x.left, key)
        else:
            return search(x.right, key)


def height(x):
    if x is None:
        return 0
    else:
        l = height(x.left)
        r = height(x.right)
        if l > r:
            return l + 1
        else:
            return r + 1


def tree_minimum(x):
    while x.left is not None:
        x = x.left
    return x


def tree_maximum(x):
    while x.right is not None:
        x = x.right
    return x


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


t = BinarySearchTree()
n = int(input())
ls = list(map(int, input().split()))
for i in ls:
    t.bstInsert(i)
##preorder(t.root)
##print()
##postorder(t.root)
##print()
levelOrder(t.root)
print(checkBST(t.root))
