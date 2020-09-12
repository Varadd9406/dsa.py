def insertion_sort(arr):
    ar = arr.copy()
    for j in range(1, len(ar)):
        key = ar[j]
        i = j - 1
        while i >= 0 and ar[i] > key:
            ar[i + 1] = ar[i]
            i -= 1
        ar[i + 1] = key
    return ar


def merge(arr1, arr2):
    i = j = 0
    ar = []
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            ar.append(arr1[i])
            i += 1
        else:
            ar.append(arr2[j])
            j += 1
    while i < len(arr1):
        ar.append(arr1[i])
        i += 1
    while j < len(arr2):
        ar.append(arr2[j])
        j += 1
    return ar


def merge_sort(arr):
    n = len(arr)
    if n > 1:
        l = arr[:n // 2]
        r = arr[n // 2:]
        return merge(merge_sort(l), merge_sort(r))
    else:
        return arr


def tim_sort(arr):
    n = len(arr)
    run = 32
    ls = []
    for i in range(0, n, run):
        
