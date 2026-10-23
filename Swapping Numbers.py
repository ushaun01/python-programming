#Method 1
num1=100
num2=250

num=num1
num1=num2
num2=num

print("Value 0f num1",num1)
print("Value 0f num2",num2)

# #method 2 :Taking input from users
num1=input("Enter the value num1:")
num2=input("Enter the value num2:")

num=num1
num1=num2
num2=num

print(num1)
print(num2)

#method 3
num1=254
num2=246
num1, num2 = num2, num1      #swap statement
print(num1)
print(num2)