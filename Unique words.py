a="Python is easy and Python is powerful language"
word=a.split()
d={}
for i in word:
    if i!= " ":
        if i not in d:
            d[i]=1
        else:
            d[i]=d[i]+1

for i,j in d.items():
    if j==1:
        print(i)