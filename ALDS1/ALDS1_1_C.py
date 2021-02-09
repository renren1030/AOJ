import math

def isPrime(x):
	for i in range(2,int(math.sqrt(x))+1):
		if x%i == 0:
			return False
	return True

n=int(input())
ans=0
for i in range(n):
	x=int(input())
	if isPrime(x):
		ans+=1
print(ans)