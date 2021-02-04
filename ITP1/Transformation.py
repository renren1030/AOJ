str = input()
n = int(input())

for i in range(n):
    line = input().split()
    a = line[0]
    b = int(line[1])
    c = int(line[2]) + 1

    if a == "replace":
        str = str[:b] + line[3] + str[c:]
    elif a == "reverse":
        str = str[:b] + str[b:c][::-1] + str[c:]
    else:
        print(str[b:c])