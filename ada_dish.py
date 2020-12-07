t = int(input())
for i in range(t):
    n = int(input())
    if(1<=n<=4):
        b1= 0
        b2 =0
        c = [int(j) for j in input().split()][:n]
        c.sort()
        if(c[0]>=1 and c[n-1]<=5):
            for k in range(n-1,-1,-1):
                if(b1<b2):
                    b1=b1+c[k]
                else:
                    b2=b2+c[k]
            print(max(b1,b2))