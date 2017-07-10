import random
from functools import total_ordering
from queue import Queue


def least_partitioning_sum_k(l, k):
    # original array
    print(l)

    # build accumulative array
    acc = [sum(l[0:end + 1]) for end in range(0, len(l))]
    print("acc:\t", acc)

    # build lookup table
    lookup = dict()
    for i in range(0, len(acc)):
        if acc[i] in lookup:
            lookup[acc[i]].insert(0, i)
        else:
            lookup[acc[i]] = [i]
    print("lup:\t", lookup)

    # visited table
    visited = [False] * len(l)

    # tree elements
    @total_ordering
    class Node:
        def __init__(self, p, ind, m):
            self.prev = p
            self.index = ind
            self.max = m

        def __lt__(self, other):
            return other.get_index < self.index

    # shortest path search
    q = Queue()
    q.put_nowait(Node(None, 0, k))

    last = None

    while not q.empty():
        n = q.get_nowait()

        if visited[n.get_index]:
            continue
        visited[n.get_index] = True

        # try if we can close the set from here
        if acc[len(l) - 1] <= n.max:
            last = Node(n, len(l), -1)
            break

        for index in sorted([index for v in lookup.keys() if v <= n.max for index in lookup[v]]):
            q.put_nowait(Node(n, index + 1, acc[index] + k))

    # build output sequence
    indices = []
    while last is not None:
        indices.append(last.index)
        last = last.prev
    indices.reverse()

    res = []
    for a, b in zip(indices, indices[1:]):
        res.append(l[a:b])
    return res


def test(n, k):
    arr = [random.randint(-10, 20) for i in range(0, n)]
    for l in least_partitioning_sum_k(arr, k):
        print(l, " sum = ", sum(l))
