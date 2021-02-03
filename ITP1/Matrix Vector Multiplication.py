n, m = map(int, input().split())

A = [list(map(int, input().split())) for i in range(n)]
b = [int(input()) for i in range(m)]

for i in range(n):
    ans = 0
    for j in range(m):
        ans += A[i][j] * b[j]
    print(ans)

# A = []
# b = []
#
# for i in range(n):
#     A.append([int(s) for s in input().split()])
#
# for i in range(m):
#     b.append([int(input())])
#
# for i in range(n):
#     sum = 0
#     for j in range(m):
#         sum += A[i][j] * b[j][0]
#     print(sum)