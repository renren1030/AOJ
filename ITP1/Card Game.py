n = int(input())
T = 0
H = 0



for i in range(n):
    a, b = input().split()
    if a > b:
        T += 3
    elif a < b:
        H += 3
    else:
        H += 1
        T += 1

print(T,H)