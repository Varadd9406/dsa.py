def max_crossing_subarray(arr, mid, low, high):
    ls = -10000000000
    sm = 0
    max_right = 0
    max_left = 0
    for i in range(low, mid, -1):
        sm += arr[i]
        if sm > ls:
            ls = sm
            max_left = i
    rs = -10000000000
    sm = 0
    for i in range(mid, high+1):
        sm += arr[i]
        if sm > ls:
            rs = sm
            max_right = i
    return max_left, max_right, ls + rs


def max_subarray(arr, low, high):
    if high == low:
        return low, high, arr[low]
    else:
        mid = (low + high) // 2
        left_low, left_high, left_sum = max_subarray(arr, low, mid)
        right_low, right_high, right_sum = max_subarray(arr, mid + 1, high)
        cross_low, cross_high, cross_sum = max_crossing_subarray(arr, mid, low, high)
        if left_sum >= right_sum and left_sum >= cross_sum:
            return left_low, left_high, left_sum
        elif right_sum >= left_sum and right_sum >= cross_sum:
            return right_low, right_high, right_sum
        else:
            return cross_low, cross_high, cross_sum


def maxCrossingSum(arr, l, m, h):
    # Include elements on left of mid.
    sm = 0
    left_sum = -10000

    for i in range(m, l - 1, -1):
        sm = sm + arr[i]

        if (sm > left_sum):
            left_sum = sm

            # Include elements on right of mid
    sm = 0
    right_sum = -10000
    for i in range(m + 1, h + 1):
        sm = sm + arr[i]

        if (sm > right_sum):
            right_sum = sm

            # Return sum of elements on left and right of mid
    return left_sum + right_sum


# Returns sum of maxium sum subarray in aa[l..h]
def maxSubArraySum(arr, l, h):
    # Base Case: Only one element
    if (l == h):
        return arr[l]

        # Find middle point
    m = (l + h) // 2

    # Return maximum of following three possible cases
    # a) Maximum subarray sum in left half
    # b) Maximum subarray sum in right half
    # c) Maximum subarray sum such that the
    #     subarray crosses the midpoint
    return max(maxSubArraySum(arr, l, m),
               maxSubArraySum(arr, m + 1, h),
               maxCrossingSum(arr, l, m, h))


ls = [1, 2, 4, 5, 2, 1, 423, 42, 34, 32, 4, 2345, 24, 12, 3, 13124, 24, 14, 1, 4, 234, 3, 43, 4, 34, 23, 32, 3, 425, 25,
      25, 2, 5, 25, 2, 35, 2, 5, 235, 23]
print(max_crossing_subarray(ls, len(ls) // 2, 0, len(ls)))
