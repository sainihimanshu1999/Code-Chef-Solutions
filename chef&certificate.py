n,m,k=map(int,input().split())
count=0
for x in range(n):
	l=list(map(int,input().split()))
	a=l.pop(k)
	if sum(l)>=m and a<=10:
		count+=1
print(count)