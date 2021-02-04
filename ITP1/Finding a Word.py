cnt = 0
s = input().lower()

while True:
    t = input()
    if t == "END_OF_TEXT":
        break
    cnt += t.lower().split().count(s)

print(cnt)