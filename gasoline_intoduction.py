t=int(input())# cook your dish here
for i in range(t):
    x=int(input())
    c=[int(j) for j in input().split()][:x]
    a=0
    b=c[0]
    while(b!=0 and a!=(x-1)):
        a=a+1
        b=b+(c[a]-1)
    print(b+a)