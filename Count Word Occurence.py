a="i am red i am usha"
b=a.split()
print(b)
d={}
for i in b:
    if i !=" ":
        if i not in d:
            d[i]=1
        else:
            d[i]=d[i]+1
print(d)