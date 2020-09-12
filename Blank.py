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
                if not t.val > t.left.val or not (a[1] < t.left.val < a[2]):
                    if e1 is None:
                        e1 = t
                    else:
                        e2 = t
                        break
                q.append([t.left, a[1], t.val])
            if t.right is not None:
                if not t.val < t.right.val or not (a[1] < t.right.val < a[2]):
                    if e1 is None:
                        e1 = t
                    else:
                        e2 = t
                        break
                q.append([t.right, t.val, a[2]])
    e1.left, e2.left = e1.left, e2.left
    e1.right, e2.right = e1.right, e2.right
    e1.val, e2.val = e1.val, e2.val