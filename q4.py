#get the input for variable name,score,department
#get score for 100
#divide 100/10
name=input()
print("Enter score 100 or below")
score=int(input())
if score>100:
 print("invalid")
else:
 s=score/10
 department=input()
 print("my name is",name)
 print("my score is",s)
 print("my department is",department)
print("pass")#test case
