c=0
for i in range(1,101):
    if i%3==0 and i%5==0:
        c=c+1
        print(i)
print("count:",c)
