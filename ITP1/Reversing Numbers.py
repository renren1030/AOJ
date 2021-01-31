n = int(input())
list = list(map(int, input().split()))
list.reverse()
for i in range(n):
    if i >= 1:
        print(" ", end="")
    print(list[i], end="")
print()