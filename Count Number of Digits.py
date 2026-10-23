#Approach:1
num=123456
count=0
while num>0:
    num=num//10
    count=count+1

print(count)

#Approach:2
num=1235
con=str(num)
print(len(con))