a="usha umesh nazare"
#output=ahsu hsemu erazan

b=a.split(" ")
print(b)
result=[]
for i in b:
    result.append(i[::-1])
print(result)
c=" ".join(result)
print(c)