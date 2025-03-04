m1=int(input("Enter mark1:"))
m2=int(input("Enter mark2:"))
m3=int(input("Enter mark3:"))
m4=int(input("Enter mark4:"))
m5=int(input("Enter mark5:"))
tot=m1+m2+m3+m4+m5
avg=tot/5
if avg<35:
    print("additional class is required")
else:
    print("you are good to go")


