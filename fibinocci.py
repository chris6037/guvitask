a=int(input("enter the number:"))
D=[{}];
i=0
first=0
second=1
while(i<a):
    if(i>a):
        next=i
    else:
        next=first+second;
        first= second;
        second=next;
        print(next)
        D.append(next)
        print(D)
        i=i+1
