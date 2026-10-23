a="I live in peth vadgaon"
d={}
for i in a:
    if i!=" ":
        if i not in d:
            d[i]=1
        else:
            d[i]=d[i]+1
for i,j in d.items():
    if j!=1:
        print(i,end=" ")