import collections


def min_sliding(arr, w):
    q = collections.deque()

    for i in range(len(arr)):
        while q and q[0] <= i - w:
            q.popleft()

        while q and arr[i] <= arr[q[-1]]:
            q.pop()

        q.append(i)
        yield q[0]


def gain(arr, w):
    q_min = collections.deque()
    q_max = collections.deque()
    d = 0
    a = 0
    b = 0

    for i in range(len(arr)):
        while q_min and q_min[0] <= i - w:
            q_min.popleft()

        while q_min and arr[i] <= arr[q_min[-1]]:
            q_min.pop()

        while q_max and q_max[0] <= i - w:
            q_max.popleft()

        while q_max and arr[i] >= arr[q_max[-1]]:
            q_max.pop()

        q_min.append(i)
        q_max.append(i)

        if abs(d) < abs(arr[q_min[0]] - arr[i]):
            a = q_min[0]
            b = i
            d = arr[b] - arr[a]

        if abs(d) < abs(arr[q_max[0]] - arr[i]):
            a = q_max[0]
            b = i
            d = arr[b] - arr[a]

    return d, a, b


def gain_brute(arr, w):
    return max([(arr[j] - arr[i], i, j) for i in range(len(arr)) for j in range(i, min(i + w, len(arr)))], key=lambda p: p[0])

    #   0   1   2   3   4   5   6   7   8   9  10  11
inp = [49, 51, 45, 42, 42, 46, 49, 49, 50, 53, 54, 60]
    # [ 0,  0,  2,  3,  4,  4,  4,  4,  5,  7,  7,  8]
    # [ 3,  4,  4,  4,  4,  5,  7,  7] min
    # [ 1,  1,  5,  6,  7,  8,  8,  8] max
print(gain(inp, 4))
