score=int(input("Enter the score out of 100"))
if score>100:
    print("INVALID")
    score=int(input("Enter the score out of 100"))
    
if score<35:
    print("poor student")
elif score>35 and score<70:
        print("average student")
else:
     print("good student")
        
    
