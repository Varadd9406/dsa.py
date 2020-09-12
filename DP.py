def memoized_cut_rod(p, n):
    dp = []
    for i in range(n + 1):
        dp.append(-10000000000)
    return memoized_cut_rod_aux(p, n, dp)


def memoized_cut_rod_aux(p, n, dp):
    if dp[n] >= 0:
        return dp[n]
    if n == 0:
        q = 0
    else:
        q = -10000000000
        for i in range(1, n + 1):
            q = max(q, p[i] + memoized_cut_rod_aux(p, n - i, dp))
    dp[n] = q
    return q


def cut_rod(p, n):
    if n == 0:
        return 0
    else:
        q = -10000000000
        for i in range(1, n + 1):
            q = max(q, p[i] + cut_rod(p, n - i))
        return q


def bottom_up_cut_rod(p, n):
    r = [0] * (n + 1)
    r[0] = 0
    for j in range(1, n + 1):
        q = -10000000000
        for i in range(1, j + 1):
            q = max(q, p[i] + r[j - i])
        r[j] = q
    return r[n]


for _ in range(int(input())):
    ls = [5, 4, 2, 2, 2]
    n = len(ls)
    p = [0]
    sm = 0
    i = 0
    while i < n:
        sm += ls[i]
        p.append(sm)
        i += 1
    print(p)
    print(cut_rod(p, 3))
    print(memoized_cut_rod(p, 3))
    print(bottom_up_cut_rod(p,3))