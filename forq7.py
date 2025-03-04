"""a=[]
print("Enter elements:")
for i in range(10):
    num=int(input("element"+str(i)))
    a.append(num)
print(a)
sum=0
c=0
for i in a:
    sum=sum+i
    c=c+1
print("sum:",sum)
print("avg:",sum/c)

for i in a:
    print(i*i*i)
    
for i in range(1,5):
    for j in range(i):
        print("*",end="")
    print("\n")"""
    
for i in range(1,5):
    for j in range(1,i+1):
        print(j,end="")
    print("\n")
