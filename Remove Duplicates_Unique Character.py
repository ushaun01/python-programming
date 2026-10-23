a="My name is usha"

#approach1
b=set(a)
print(b)

# #approach2
d={}
for i in a:
    if i!=" ":
        if i not in d:
            d[i]=1
        else:
         d[i]=d[i]+1

for i,j in d.items():
    if j==1:
        print(i,end=" ")
        # print(i)

