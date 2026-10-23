#Method 1
#print factorial of 5
num=5
factorial=1
for i in range(1,num+1):
    factorial=i*factorial
print("Factorial of",num ,"is" ,factorial)

#Method 2
fact=1
for i in range(1,6):
    fact=fact*i
print(fact)
