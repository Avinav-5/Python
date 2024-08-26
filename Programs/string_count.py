a=input("enter a string ")
b=int(input("enter the number "))

value=a.split()
m=[]

for i in value:
    if(len(i)>b):
        m.append(i)
            
print(m)
