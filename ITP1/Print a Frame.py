while True:
    h,w = map(int, input().split())
    if h == 0 and w == 0:break
    for j in range(h):
        for i in range(w):
            if (i+j)%2 == 0:
                print("#", end="")
            else:
                print(".", end="")
        print()
    print()