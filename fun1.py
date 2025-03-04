"""+-def printrange(c,d):
    for i in range(c,d):
        print(i)

a=int(input("a:"))
b=int(input("b:"))
printrange(a,b)"""

"""s_username="Emc"
s_password="123"


def validate(sname,spass,name,passwd):
    if(sname==name and spass==passwd):
        return True
    else:
        return False


uname=input("Enter username:")
password=input("Enter Password:")
a=validate(s_username,s_password,uname,password)
if a==True:
    print("correct")
else:
    print("not correct")"""

def add(v1,v2):
    return v1+v2

a=int(input("a:"))
b=int(input("b:"))
c=int(input("c:"))
ans=add(a,b)*c
print(ans)
