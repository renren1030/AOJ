while True:
    n, x = map(int, input().split())
    if n == x == 0:
        break

    cnt = 0

    for a in range(1, x // 3):
        for b in range(a + 1, x // 2):
            c = x - a - b
            if b < c <= n:
                cnt += 1

    print(cnt)