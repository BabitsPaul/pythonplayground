def minima(arr):
    result = []
    min_index = 0

    for i in range(1, len(arr)):
        if arr[i] < arr[i - 1] and arr[i] < arr[i + 1]:
            result.append((arr[min_index], min_index, i - min_index))
            min_index = i

    # last element
    result.append((arr[min_index], min_index, len(arr) - min_index))

    print("Min: ", result)

    return result


def maxima(arr):
    result = []

    for m in minima(arr):
        max_index = m[1]

        for i in range(m[1] + 1, m[1] + m[2]):
            if arr[max_index] < arr[i]:
                max_index = i

        result.append((arr[max_index], max_index, m))

    print("Max: ", result)

    return result


def max_dist_min_max(arr):
    longest_seq = max(maxima(arr), key=lambda s: s[1] - s[2][1] + 1)

    return arr[longest_seq[2][1]:longest_seq[1] + 1]


test_in = [-1,12,1,2,3,4,5,6,7]
print(max_dist_min_max(test_in))
