list = []

for i in range(0,10):
    list.append(input("add a number"))

largest = list[0]

for x in list:
    if x > largest:
        largest = x

print (largest)