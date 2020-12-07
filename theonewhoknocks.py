# cook your dish here
t=int(input())
while (t!=0):
    x,y=input().split()
    x = int(x)
    y = int(y)
    difference = abs(x-y)
    if(x>y):
        if(difference%2 == 0):
            print(1)
        else:
            print(2)
    elif(x<y):
        if(difference%2!=0):
            print(1)
        elif(difference%4==0):
            print(3)
        else:
            print(2)
    else:
        print(0)
        
    t= t-1