"""i=10
while(i<=200):
    print(i,end=",")
    i=i+10
i=10
while(i>=1):
    print(i,end="'")
    i=i-1
sum=1
num=int(input("enter the number:"))
while(num!=0):
    sum=sum*num
    num=num-1
print(sum)
a=[1,2,3,4,5,6]
a.insert(0,11)
a.append(7)
#a.pop(3)list

b=[45,89,100]
a.extend(b)
print(a)
a=(1,2,3,4)
b=list(a)
#tuple
b.pop()
print(a)
print(b)"""

a={1,2,3,4}
a.add(10)
a.remove(4)
a.pop()
print(a)
