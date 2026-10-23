#without space

a="India is my country"
d={}

for i in a:
    if i!=' ':
        if i not in d:
            d[i]=1
        else:
            d[i]=d[i]+1
print(d)