a=int(input("a value:"))
b=int(input("b value:"))
option=input("ENter option: (add/sub/mul/div)")
if(option=="add"):
    print(a+b)
elif(option=="sub"):
    print(a-b)
elif(option=="mul"):
    print(a*b)
elif(option=="div"):
    print(a/b)
else:
    print("invalid")
