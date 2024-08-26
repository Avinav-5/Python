# Enter a list and check wheather it is prime or not if prime then print correct else find sum of list and if it is prime then print correct else not correct

a=[]
m=0;
flag=0
b=int(input("enter the size "))
for i in range(b):
    c=int(input("enter the value "))
    a.append(c)

for i in a:
    for j in range(2,11):
        if(i==j):
            continue
        if(i%j==0):
            flag=1
if(flag==1):
    for i in a:
        m=m+i
    for j in range(2,11):
        if(m%j==0):
            print("not correct")
        else:
            print("correct")
        
else:
    print("correct")
  
            
