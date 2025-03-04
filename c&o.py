class student:
    def __init__(self):
        self.name="hm"
        self.regno="123"
    def display(self):
        print("name:",self.name)
        print("regno:",self.regno)

s1=student()
print(s1.name)
print(s1.regno)
s1.display()
