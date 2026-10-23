#append value by append method and find smallest value 2,18,9,23,65,55
a=[]
a.append(2)
a.append(18)
a.append(9)
a.append(25)
a.append(65)
a.append(55)
print(a)
a.sort()
print(a[0])


#using for loop
a=[720,201,896,200,325]
min=a[0]

for i in range(1,len(a)):
    if a[i]<min:
        min=a[i]
print(min)