a=int(input("enter the number:"))
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
        i=i+1