n = int(input())

h = n // 3600
m = n % 3600//60
s = n % 60

# print("{}:{}:{}".format(h,m,s))
print(f"{h}:{m}:{s}")