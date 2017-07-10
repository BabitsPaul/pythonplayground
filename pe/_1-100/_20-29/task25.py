def search(n):
    i = 1
    f1 = 0
    f2 = 1

    while 1:
        if len(str(f2)) >= n:
            return i

        tmp = f2
        f2 += f1
        f1 = tmp

        i += 1


print(search(1000))