a={
    "name":"brc",
    "age":"22",
    "sec":"a",
    "sub":["dsa","os"]}
print(a.keys())
print(a.values())
a["age"]=21
a.update({"name":"brinc"})
a.pop("sub")
del a
print(a)
