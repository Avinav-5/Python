a=[1,2,3,4,5,6]
b=int(input("Enter the number to search "))
for i in a :
    if(a[i]==b):
        flag = 1
        break
    else:
        flag = 0
if(flag==1):
    print("Elemnt found at ",i)
else:
     print("Elemnt not found ")
