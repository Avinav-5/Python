print("Number from 10 to 1 : ")
for num in range(10,0,-1):
    print(num)

print("------------------------------")
print("prime number from 2 to 50 : ")
for num in range(2,51):
    for i in range(2,num):
        if num % i==0:
            break
    else:
        print(num,end = " ")
