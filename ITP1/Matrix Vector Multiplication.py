n, m = map(int, input().split())

A = []
b = []

for i in range(n):
    A.append([int(s) for s in input().split()])

for i in range(m):
    b.append([int(input())])

for i in range(n):
    sum = 0
    for j in range(m):
        sum += A[i][j] * b[j][0]
    print(sum)