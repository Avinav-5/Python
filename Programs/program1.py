b = int(input("enter the range 1 "))
c = int(input("Enter the range 2 "))
for i in range(b,c+1):
    j=2;
    f=0;
    while(j<10):
       if(i%j==0):
          f=1;
       j=j+1;

    if(f==0):
       print(i)



