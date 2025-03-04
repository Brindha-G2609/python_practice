"""class goa:
    drink=""
    def party(self):
        print("lets party")
    def beach(self):
        print("Enjoy")
rames=goa()
suresh=goa()
rames.party()"""


class laptop:
    def __init__(self):
        self.brand=""
        self.price=""
        self.processor=""
        self.ram=""
    def display(self):
        print("brand:",self.brand)
        print("price:",self.price)
        print("processor:",self.processor)
        print("Ram:",self.ram)
for i in range(3):
    lap=input("enter lap:")
    lap=laptop()
    #dell=laptop()
    #lenovo=laptop()
    lap.brand=input("brand:")
    lap.price= int(input("price:"))
    lap.processor=input("processor:")
    lap.ram=input("Ram:")
    lap.display()
    
"""hp.price="40000"
hp.processor="ryzen"
hp.ram="8gb"
lenovo.price="30000"
lenovo.processor="i3"
lenovo.ram="4gb

print("DELL:\n______\nprice:",dell.price,"\nprocessor:",dell.processor,"\nRam:",dell.ram)
print("\nHP:\n______\nprice:",hp.price,"\nprocessor:",hp.processor,"\nRam:",hp.ram)

print("\nlenovo:\n______\nprice:",lenovo.price,"\nprocessor:",lenovo.processor,"\nRam:",lenovo.ram)

"""
