import math

a, b, C = map(float, input().split())
S =  0.5 * a * b * math.sin(C * math.pi / 180)
L = a + b + (a ** 2 + b ** 2 - 2 * a * b * math.cos(C * math.pi / 180)) ** 0.5
h = 2 * S / a

print("{} {} {}".format(S, L, h))