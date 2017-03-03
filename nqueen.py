def is_safe(board, x, y, c):
    for p in [board[i] for i in range(0, c)]:
        if p[0] == x or p[1] == y or x + y == p[0] + p[1] or x - y == p[0] - p[1]:
            return False

    return True


def nqueen_rec(board, n, c):
    if c == n:
        print(board)
    else:
        for x in range(0, n):
            if is_safe(board, x, c, c):
                board[c] = (x, c)
                nqueen_rec(board, n, c + 1)


def nqueen_rec_driver(n):
    nqueen_rec([(-1, x) for x in range(0, n)], n, 0)


def nqueen_nrec(n):
    c = 0
    step = [0 for x in range(0, n + 1)]
    board = [(x, x) for x in range(0, n)]

    while c != -1:
        if c == n:
            print(board)
            c -= 1
            step[c] += 1
        elif step[c] == n:
            c -= 1
            step[c] += 1
        elif is_safe(board, step[c], c, c):
            board[c] = (step[c], c)
            c += 1
            step[c] = 0
        else:
            step[c] += 1


def test(f, n):
    f(n)


tn = 15
print("recursive:")
test(nqueen_rec_driver, tn)
print("non recursive:")
test(nqueen_nrec, tn)
