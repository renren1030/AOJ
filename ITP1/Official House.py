houses = [[[0 for r in range(10)] for f in range(3)] for b in range(4)]

n = int(input())

for i in range(n):
    b, f, r, v = map(int, input().split())
    houses[b - 1][f - 1][r - 1] += v

for i in range(4):
    for j in range(3):
        for k in range(10):
            print(" {}".format(houses[i][j][k]), end="")
        print()
    if i != 3:
        print("#"*20)
