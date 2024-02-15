name = None

dict = {}

while name != "no":
    name = input("enter employee name")
    
    if name != "no":
        salary = input("input salary")
        dict[name] = salary
    
print(dict)