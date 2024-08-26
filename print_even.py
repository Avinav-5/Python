#create a new list from existing list by removing all the odd list

a=[]
m=[]
b=int(input("enter the size of list "))
for i in range(b):
    c=int(input("enter the value "))
    a.append(c)

for j in a:
    if(j % 2==0):
        m.append(j)

print(m)
        
