#find the highest number
num=[1,25,36,85,45,84]
num.sort()
print(num[-1])

#find the second-highest number
a=[710,201,896,200,325]
a.sort(reverse=True)
print(a[1])

#using for loop
a=[720,201,896,200,325]
maximum=a[0]

for i in range(1,len(a)):
    if a[i]>maximum:
        maximum=a[i]
print(maximum)